#!/usr/bin/env python3
"""Final verification that all truncation functions have been updated"""

import os
import re

def check_file(filepath, file_description):
    """Check a file for the new truncation string"""
    print(f"\n{'='*60}")
    print(f"Checking: {file_description}")
    print(f"File: {filepath}")
    print('='*60)

    with open(filepath, 'r') as f:
        content = f.read()

    # Check for new string
    new_string = 'This is so long, truncating.'
    old_string_single = "'...'"
    old_string_double = '"..."'

    has_new = new_string in content
    has_old_single = old_string_single in content
    has_old_double = old_string_double in content

    if has_new:
        print(f"✓ New truncation string found: '{new_string}'")
    else:
        print(f"✗ New truncation string NOT found: '{new_string}'")

    if has_old_single or has_old_double:
        print(f"✗ Old truncation string still present: '...'")
        # Show context
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if "'...'" in line or '"..."' in line:
                print(f"  Line {i}: {line.strip()}")
    else:
        print(f"✓ Old truncation string removed")

    # Show the relevant function
    print("\n--- Relevant code ---")
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        if new_string in line:
            # Show context (3 lines before and after)
            start = max(0, i - 4)
            end = min(len(lines), i + 3)
            for j in range(start, end):
                marker = ">>>" if j == i - 1 else "   "
                print(f"{marker} {j+1:3d}: {lines[j]}")

    return has_new and not has_old_single and not has_old_double

# Check both files
files_to_check = [
    ('/timotejKralik__testing-web-project/apps/frontend/utils/index.ts',
     'Main truncate utility function'),
    ('/timotejKralik__testing-web-project/apps/frontend/components/article/Content.tsx',
     'Article content trimming function')
]

all_passed = True
for filepath, description in files_to_check:
    if os.path.exists(filepath):
        passed = check_file(filepath, description)
        all_passed = all_passed and passed
    else:
        print(f"\n✗ File not found: {filepath}")
        all_passed = False

print("\n" + "="*60)
if all_passed:
    print("✓✓✓ ALL CHECKS PASSED ✓✓✓")
    print("All truncation functions have been successfully updated!")
else:
    print("✗✗✗ SOME CHECKS FAILED ✗✗✗")
    print("Please review the output above.")
print("="*60)

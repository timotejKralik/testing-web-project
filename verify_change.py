#!/usr/bin/env python3
"""Verify that the truncate function has been updated correctly"""

import re

# Read the file
with open('/timotejKralik__testing-web-project/apps/frontend/utils/index.ts', 'r') as f:
    content = f.read()

# Check if the new truncation string is present
if 'This is so long, truncating.' in content:
    print("✓ SUCCESS: The truncation string has been changed to 'This is so long, truncating.'")

    # Verify the old string is not present
    if "'...'" not in content and '"..."' not in content:
        print("✓ SUCCESS: The old truncation string '...' has been removed")
    else:
        # Check if it's in the truncate function specifically
        truncate_func_match = re.search(r'export function truncate\([^)]+\)\s*{[^}]+}', content, re.DOTALL)
        if truncate_func_match:
            truncate_func = truncate_func_match.group(0)
            if "'...'" in truncate_func or '"..."' in truncate_func:
                print("✗ WARNING: The old truncation string '...' is still in the truncate function")
            else:
                print("✓ SUCCESS: The old truncation string '...' is not in the truncate function")

    # Display the truncate function
    print("\n--- Current truncate function ---")
    truncate_func_match = re.search(r'export function truncate\([^)]+\)\s*{[^}]+};?', content, re.DOTALL)
    if truncate_func_match:
        print(truncate_func_match.group(0))

else:
    print("✗ FAILURE: The truncation string has NOT been changed to 'This is so long, truncating.'")
    print("\n--- Current file content ---")
    print(content)

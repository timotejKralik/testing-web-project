#!/usr/bin/env python3
"""Test script to verify truncate function behavior"""

# Simulate the truncate function - BEFORE change
def truncate_before(string, max_length):
    if len(string) > max_length:
        return string[:max_length - 1] + '...'
    return string

# Simulate the truncate function - AFTER change
def truncate_after(string, max_length):
    if len(string) > max_length:
        return string[:max_length - 1] + 'This is so long, truncating.'
    return string

# Test cases
test_cases = [
    {"input": "This is a very long string that needs to be truncated", "max_length": 20},
    {"input": "Short", "max_length": 20},
    {"input": "Exactly twenty chars", "max_length": 20},
    {"input": "A" * 100, "max_length": 50}
]

print("=== BEFORE (using '...') ===")
for idx, test in enumerate(test_cases, 1):
    result = truncate_before(test["input"], test["max_length"])
    input_display = test["input"][:50] + ('...' if len(test["input"]) > 50 else '')
    print(f"Test {idx}:")
    print(f"  Input: \"{input_display}\"")
    print(f"  Max Length: {test['max_length']}")
    print(f"  Result: \"{result}\"")
    print(f"  Result Length: {len(result)}")
    print()

print("\n=== AFTER (using 'This is so long, truncating.') ===")
for idx, test in enumerate(test_cases, 1):
    result = truncate_after(test["input"], test["max_length"])
    input_display = test["input"][:50] + ('...' if len(test["input"]) > 50 else '')
    print(f"Test {idx}:")
    print(f"  Input: \"{input_display}\"")
    print(f"  Max Length: {test['max_length']}")
    print(f"  Result: \"{result}\"")
    print(f"  Result Length: {len(result)}")
    print()

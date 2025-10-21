#!/usr/bin/env python3
"""Test script to verify truncation behavior"""

def truncate_current(string, max_length):
    """Current implementation with '...'"""
    return string[:max_length - 1] + '...' if len(string) > max_length else string

def truncate_new(string, max_length):
    """New implementation with 'This is so long, truncating.'"""
    if len(string) <= max_length:
        return string

    truncation_text = "This is so long, truncating."

    # If max_length is smaller than or equal to truncation text length,
    # just return the truncation text truncated to max_length
    if max_length <= len(truncation_text):
        return truncation_text[:max_length]

    # Otherwise, truncate the original string and add the truncation text
    return string[:max_length - len(truncation_text)] + truncation_text

# Test cases
test_cases = [
    {
        "input": "This is a short string",
        "max_length": 50,
        "description": "Short string (no truncation needed)"
    },
    {
        "input": "This is a very long string that should definitely be truncated because it exceeds the maximum length",
        "max_length": 30,
        "description": "Long string (truncation needed)"
    },
    {
        "input": "Exactly thirty characters long",
        "max_length": 30,
        "description": "String exactly at max length"
    },
    {
        "input": "Exactly thirty-one characters!!",
        "max_length": 30,
        "description": "String one character over max length"
    },
    {
        "input": "This is a test string for meta description that is longer than 155 characters and should be truncated properly to fit within the meta description length limit",
        "max_length": 155,
        "description": "Meta description length test"
    },
    {
        "input": "This is a string that needs truncation",
        "max_length": 25,
        "description": "Max length smaller than truncation text"
    },
    {
        "input": "This is a string that needs truncation",
        "max_length": 28,
        "description": "Max length equal to truncation text length"
    }
]

print("Testing truncation function:")
print("=" * 60)

for i, test_case in enumerate(test_cases):
    print(f"\nTest {i + 1}: {test_case['description']}")
    print(f"Input: \"{test_case['input']}\"")
    print(f"Max length: {test_case['max_length']}")
    print(f"Input length: {len(test_case['input'])}")

    # Test current implementation
    result_current = truncate_current(test_case['input'], test_case['max_length'])
    print(f"Current result: \"{result_current}\"")
    print(f"Current result length: {len(result_current)}")

    # Test new implementation
    result_new = truncate_new(test_case['input'], test_case['max_length'])
    print(f"New result: \"{result_new}\"")
    print(f"New result length: {len(result_new)}")

    # Check if truncation was needed
    if len(test_case['input']) > test_case['max_length']:
        print("✓ Truncation was applied")
    else:
        print("✓ No truncation needed")
#!/usr/bin/env python3
"""Final test to verify the TypeScript implementation matches our logic"""

def truncate_typescript_implementation(string, max_length):
    """Exact implementation matching the TypeScript code"""
    if len(string) <= max_length:
        return string

    truncation_text = "This is so long, truncating."

    # If maxLength is smaller than or equal to truncation text length,
    # just return the truncation text truncated to maxLength
    if max_length <= len(truncation_text):
        return truncation_text[:max_length]

    # Otherwise, truncate the original string and add the truncation text
    return string[:max_length - len(truncation_text)] + truncation_text

# Test cases that cover various scenarios
test_cases = [
    # Basic functionality
    ("Short text", 50, "Short text"),  # No truncation needed
    ("This is a very long text that needs to be truncated", 30, "ThThis is so long, truncating."),  # Normal truncation

    # Edge cases
    ("Text", 28, "Text"),  # Shorter than max length, no truncation
    ("This is exactly 29 characters!", 28, "This is so long, truncating."),  # Longer than max length, needs truncation
    ("This is a long text that needs truncation", 10, "This is so"),  # Max length smaller than truncation text

    # Meta description scenario (155 chars)
    ("This is a test string for meta description that is longer than 155 characters and should be truncated properly to fit within the meta description length limit", 155, "This is a test string for meta description that is longer than 155 characters and should be truncated properly to fit within thThis is so long, truncating."),

    # Boundary conditions
    ("A" * 200, 50, "A" * 22 + "This is so long, truncating."),
    ("", 10, ""),  # Empty string
    ("This is a long string", 1, "T"),  # Single character max length
]

print("Final verification of TypeScript implementation:")
print("=" * 60)

all_passed = True
for i, (input_str, max_len, expected) in enumerate(test_cases):
    result = truncate_typescript_implementation(input_str, max_len)
    passed = result == expected
    all_passed = all_passed and passed

    status = "✓ PASS" if passed else "✗ FAIL"
    print(f"\nTest {i + 1}: {status}")
    print(f"Input: \"{input_str[:50]}{'...' if len(input_str) > 50 else ''}\"")
    print(f"Max length: {max_len}")
    print(f"Expected: \"{expected}\"")
    print(f"Got:      \"{result}\"")
    print(f"Expected length: {len(expected)}, Got length: {len(result)}")

    if not passed:
        print("❌ MISMATCH!")

print(f"\n{'='*60}")
print(f"Overall result: {'✓ ALL TESTS PASSED' if all_passed else '✗ SOME TESTS FAILED'}")

# Verify truncation text length
truncation_text = "This is so long, truncating."
print(f"\nTruncation text: \"{truncation_text}\"")
print(f"Truncation text length: {len(truncation_text)} characters")
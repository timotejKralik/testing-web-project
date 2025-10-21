#!/usr/bin/env python3
"""Edge case testing for the truncation implementation"""

def truncate(string, max_length):
    """Final implementation matching TypeScript code"""
    if len(string) <= max_length:
        return string

    truncation_text = "This is so long, truncating."

    # If maxLength is smaller than or equal to truncation text length,
    # just return the truncation text truncated to maxLength
    if max_length <= len(truncation_text):
        return truncation_text[:max_length]

    # Otherwise, truncate the original string and add the truncation text
    return string[:max_length - len(truncation_text)] + truncation_text

def test_edge_cases():
    """Test various edge cases"""
    print("Edge Case Testing")
    print("=" * 50)

    # Test cases with edge conditions
    edge_cases = [
        # Basic cases
        ("", 0, ""),  # Empty string, zero length
        ("", 10, ""),  # Empty string, positive length
        ("A", 1, "A"),  # Single char, exact length
        ("AB", 1, "T"),  # Two chars, max length 1

        # Boundary cases around truncation text length (28)
        ("A" * 27, 28, "A" * 27),  # 27 chars, max 28 - no truncation
        ("A" * 28, 28, "A" * 28),  # 28 chars, max 28 - no truncation
        ("A" * 29, 28, "This is so long, truncating."),  # 29 chars, max 28 - truncation
        ("A" * 30, 28, "This is so long, truncating."),  # 30 chars, max 28 - truncation

        # Cases where max_length < truncation text length AND input > max_length
        ("Long text that needs truncation", 1, "T"),
        ("Long text that needs truncation", 5, "This "),
        ("Long text that needs truncation", 10, "This is so"),
        ("Long text that needs truncation", 27, "This is so long, truncating"),

        # Cases where max_length = truncation text length
        ("Long text that needs truncation", 28, "This is so long, truncating."),

        # Cases where max_length > truncation text length
        ("Long text that needs truncation", 29, "LThis is so long, truncating."),
        ("Long text that needs truncation for sure and more text", 50, "Long text that needs tThis is so long, truncating."),

        # Meta description length (155)
        ("A" * 154, 155, "A" * 154),  # No truncation needed
        ("A" * 155, 155, "A" * 155),  # Exactly at limit
        ("A" * 156, 155, "A" * 127 + "This is so long, truncating."),  # Needs truncation

        # Very long strings
        ("A" * 1000, 100, "A" * 72 + "This is so long, truncating."),
        ("A" * 1000, 50, "A" * 22 + "This is so long, truncating."),
    ]

    all_passed = True

    for i, (input_str, max_len, expected) in enumerate(edge_cases):
        result = truncate(input_str, max_len)
        passed = result == expected and len(result) <= max_len

        if not passed:
            all_passed = False
            print(f"❌ Test {i+1} FAILED:")
            truncated_input = input_str[:30] + ('...' if len(input_str) > 30 else '')
            print(f"   Input: '{truncated_input}'")
            print(f"   Max length: {max_len}")
            print(f"   Expected: '{expected}'")
            print(f"   Got: '{result}'")
            print(f"   Expected length: {len(expected)}")
            print(f"   Got length: {len(result)}")
            print()
        else:
            print(f"✅ Test {i+1} PASSED: max_len={max_len}, result_len={len(result)}")

    print(f"\n{'='*50}")
    if all_passed:
        print("🎉 ALL EDGE CASE TESTS PASSED!")
    else:
        print("❌ SOME EDGE CASE TESTS FAILED!")

    return all_passed

def test_consistency():
    """Test that the function is consistent and predictable"""
    print("\nConsistency Testing")
    print("=" * 50)

    # Test that results are always <= max_length when truncation occurs
    test_strings = [
        "Short",
        "Medium length string",
        "This is a very long string that definitely needs truncation",
        "A" * 100,
        "A" * 1000,
    ]

    max_lengths = [1, 5, 10, 28, 29, 50, 100, 155, 200]

    all_consistent = True

    for string in test_strings:
        for max_len in max_lengths:
            result = truncate(string, max_len)

            # Check that result length never exceeds max_length
            if len(result) > max_len:
                print(f"❌ CONSISTENCY VIOLATION:")
                truncated_string = string[:30] + ('...' if len(string) > 30 else '')
                print(f"   Input: '{truncated_string}'")
                print(f"   Max length: {max_len}")
                print(f"   Result length: {len(result)} (EXCEEDS MAX!)")
                all_consistent = False

            # Check that if input <= max_len, result == input
            if len(string) <= max_len and result != string:
                print(f"❌ CONSISTENCY VIOLATION:")
                print(f"   Input: '{string}' (length {len(string)})")
                print(f"   Max length: {max_len}")
                print(f"   Expected: '{string}'")
                print(f"   Got: '{result}'")
                all_consistent = False

    if all_consistent:
        print("✅ All consistency checks passed!")
    else:
        print("❌ Consistency violations found!")

    return all_consistent

if __name__ == "__main__":
    edge_passed = test_edge_cases()
    consistency_passed = test_consistency()

    print(f"\n{'='*60}")
    print("FINAL SUMMARY:")
    print(f"Edge cases: {'✅ PASSED' if edge_passed else '❌ FAILED'}")
    print(f"Consistency: {'✅ PASSED' if consistency_passed else '❌ FAILED'}")
    print(f"Overall: {'🎉 ALL TESTS PASSED!' if edge_passed and consistency_passed else '❌ SOME TESTS FAILED!'}")
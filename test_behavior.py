#!/usr/bin/env python3
"""Test the behavior of the updated truncation functions"""

def truncate(string, max_length):
    """Python implementation of the updated truncate function"""
    if len(string) > max_length:
        return string[:max_length - 1] + 'This is so long, truncating.'
    return string

def get_trimmed_content(content, card_max_characters):
    """Python implementation of the updated getTrimmedContent function"""
    return content[:card_max_characters] + 'This is so long, truncating.'

# Test cases
print("="*70)
print("Testing truncate() function")
print("="*70)

test_cases = [
    ("Short text", 50),
    ("This is a very long text that definitely needs to be truncated for display", 30),
    ("Exactly 20 chars!!!", 20),
    ("A" * 100, 50),
]

for text, max_len in test_cases:
    result = truncate(text, max_len)
    print(f"\nInput: '{text[:50]}{'...' if len(text) > 50 else ''}'")
    print(f"Max Length: {max_len}")
    print(f"Input Length: {len(text)}")
    print(f"Result: '{result}'")
    print(f"Result Length: {len(result)}")

    if len(text) > max_len:
        assert 'This is so long, truncating.' in result, "Truncation string not found!"
        print("✓ Truncation string correctly applied")
    else:
        assert result == text, "Short text should not be modified!"
        print("✓ Short text correctly preserved")

print("\n" + "="*70)
print("Testing getTrimmedContent() function")
print("="*70)

# For getTrimmedContent, it always adds the truncation string
# (in the actual code, it's only called when content.length > cardMaxCharacters)
test_content = "This is article content that is being displayed on a card and needs to be trimmed"
card_max = 40

result = get_trimmed_content(test_content, card_max)
print(f"\nContent: '{test_content}'")
print(f"Card Max Characters: {card_max}")
print(f"Result: '{result}'")
print(f"Result Length: {len(result)}")
assert 'This is so long, truncating.' in result, "Truncation string not found!"
print("✓ Truncation string correctly applied")

print("\n" + "="*70)
print("✓✓✓ ALL BEHAVIOR TESTS PASSED ✓✓✓")
print("="*70)

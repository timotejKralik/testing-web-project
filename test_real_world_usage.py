#!/usr/bin/env python3
"""
Test real-world usage scenarios for the truncation functions
"""

def truncate(string, max_length):
    """Simulates the updated truncate function from utils/index.ts"""
    if len(string) > max_length:
        return string[:max_length - 1] + 'This is so long, truncating.'
    return string

# Simulate META_DESCRIPTION_MAX_LENGTH (common value is 160)
META_DESCRIPTION_MAX_LENGTH = 160

def get_meta_description_from_content(content):
    """Simulates getMetaDescriptionFromContent from utils/index.ts"""
    # In real code, this would parse HTML and get text content
    # For testing, we'll just use the content as-is
    return truncate(content, META_DESCRIPTION_MAX_LENGTH)

print("="*80)
print("REAL-WORLD USAGE TEST: Meta Description Generation")
print("="*80)

# Test case 1: Short meta description (no truncation needed)
short_content = "This is a short article about web development."
result1 = get_meta_description_from_content(short_content)
print(f"\nTest 1: Short content")
print(f"Input: '{short_content}'")
print(f"Result: '{result1}'")
print(f"Truncated: {len(result1) > len(short_content)}")
assert result1 == short_content, "Short content should not be truncated"
print("✓ PASS")

# Test case 2: Long meta description (needs truncation)
long_content = ("This is a very long article about web development, JavaScript, TypeScript, "
                "React, Next.js, and many other modern web technologies. It covers topics "
                "like state management, server-side rendering, static site generation, and more. "
                "This content is definitely longer than 160 characters.")
result2 = get_meta_description_from_content(long_content)
print(f"\nTest 2: Long content")
print(f"Input length: {len(long_content)} characters")
print(f"Result: '{result2}'")
print(f"Result length: {len(result2)} characters")
assert 'This is so long, truncating.' in result2, "Long content should include truncation string"
assert len(result2) > META_DESCRIPTION_MAX_LENGTH, "Result includes original content + truncation string"
print("✓ PASS")

# Test case 3: Content exactly at the limit
exact_content = "A" * META_DESCRIPTION_MAX_LENGTH
result3 = get_meta_description_from_content(exact_content)
print(f"\nTest 3: Content exactly at limit ({META_DESCRIPTION_MAX_LENGTH} chars)")
print(f"Input length: {len(exact_content)} characters")
print(f"Result length: {len(result3)} characters")
print(f"Truncated: {len(result3) > len(exact_content)}")
assert result3 == exact_content, "Content at exact limit should not be truncated"
print("✓ PASS")

# Test case 4: Content just over the limit
over_content = "A" * (META_DESCRIPTION_MAX_LENGTH + 1)
result4 = get_meta_description_from_content(over_content)
print(f"\nTest 4: Content just over limit ({META_DESCRIPTION_MAX_LENGTH + 1} chars)")
print(f"Input length: {len(over_content)} characters")
print(f"Result: '{result4[:50]}...'")
print(f"Result length: {len(result4)} characters")
assert 'This is so long, truncating.' in result4, "Content over limit should be truncated"
print("✓ PASS")

print("\n" + "="*80)
print("REAL-WORLD USAGE TEST: Article Card Content Trimming")
print("="*80)

def get_trimmed_content(content, card_max_characters):
    """Simulates getTrimmedContent from components/article/Content.tsx"""
    return content[:card_max_characters] + 'This is so long, truncating.'

# This function is only called when content.length > cardMaxCharacters
CARD_MAX_CHARACTERS = 200

article_content = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                  "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                  "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
                  "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
                  "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")

result5 = get_trimmed_content(article_content, CARD_MAX_CHARACTERS)
print(f"\nTest 5: Article card preview")
print(f"Full article length: {len(article_content)} characters")
print(f"Card max characters: {CARD_MAX_CHARACTERS}")
print(f"Preview: '{result5[:100]}...'")
print(f"Preview length: {len(result5)} characters")
assert 'This is so long, truncating.' in result5, "Article preview should include truncation string"
print("✓ PASS")

print("\n" + "="*80)
print("✓✓✓ ALL REAL-WORLD USAGE TESTS PASSED ✓✓✓")
print("="*80)
print("\nSummary:")
print("- Meta descriptions are properly truncated with the new string")
print("- Article card previews are properly truncated with the new string")
print("- Short content is not unnecessarily truncated")
print("- The new truncation string 'This is so long, truncating.' is correctly applied")

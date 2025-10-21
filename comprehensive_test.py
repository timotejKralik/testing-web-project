#!/usr/bin/env python3
"""Comprehensive test to verify all truncation changes are working correctly"""

def truncate_new_implementation(string, max_length):
    """New truncate implementation matching the TypeScript code"""
    if len(string) <= max_length:
        return string

    truncation_text = "This is so long, truncating."

    # If maxLength is smaller than or equal to truncation text length,
    # just return the truncation text truncated to maxLength
    if max_length <= len(truncation_text):
        return truncation_text[:max_length]

    # Otherwise, truncate the original string and add the truncation text
    return string[:max_length - len(truncation_text)] + truncation_text

def test_utils_truncate():
    """Test the utils/index.ts truncate function"""
    print("Testing utils/index.ts truncate function:")
    print("-" * 40)

    test_cases = [
        ("Short text", 50),
        ("This is a very long text that needs to be truncated for sure", 30),
        ("Meta description test that is longer than 155 characters and should be truncated properly to fit within the meta description length limit for SEO purposes", 155),
        ("Edge case", 10),
        ("", 20),
    ]

    for text, max_len in test_cases:
        result = truncate_new_implementation(text, max_len)
        truncated_text = text[:50] + ('...' if len(text) > 50 else '')
        print(f"Input: '{truncated_text}'")
        print(f"Max length: {max_len}")
        print(f"Result: '{result}'")
        print(f"Result length: {len(result)}")
        truncated_status = 'Yes' if len(text) > max_len else 'No'
        print(f"Truncated: {truncated_status}")
        print()

def test_article_content_truncate():
    """Test the article content truncation (now using utils function)"""
    print("Testing article content truncation:")
    print("-" * 40)

    # Simulate the article content truncation
    def get_trimmed_content(content, card_max_characters):
        return truncate_new_implementation(content, card_max_characters)

    test_cases = [
        ("This is a short article content", 100),
        ("This is a very long article content that should be truncated when displayed on cards because it exceeds the maximum character limit set for card previews", 50),
        ("Another long article with lots of content that needs to be truncated properly", 30),
    ]

    for content, max_chars in test_cases:
        result = get_trimmed_content(content, max_chars)
        truncated_content = content[:50] + ('...' if len(content) > 50 else '')
        print(f"Content: '{truncated_content}'")
        print(f"Max chars: {max_chars}")
        print(f"Result: '{result}'")
        print(f"Result length: {len(result)}")
        truncated_status = 'Yes' if len(content) > max_chars else 'No'
        print(f"Truncated: {truncated_status}")
        print()

def test_meta_description():
    """Test meta description truncation"""
    print("Testing meta description truncation:")
    print("-" * 40)

    META_DESCRIPTION_MAX_LENGTH = 155

    def get_meta_description_from_content(content):
        # Simulate removing HTML tags (simplified)
        text_content = content.replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>', '')
        return truncate_new_implementation(text_content, META_DESCRIPTION_MAX_LENGTH)

    test_cases = [
        "<p>This is a short meta description</p>",
        "<p>This is a very long meta description that contains a lot of text and should be truncated to fit within the 155 character limit that is recommended for SEO purposes and search engine display</p>",
        "<p><strong>Bold text</strong> with more content that goes on and on and should definitely be truncated because it's way too long for a meta description and would be cut off in search results</p>",
    ]

    for content in test_cases:
        result = get_meta_description_from_content(content)
        truncated_html = content[:50] + ('...' if len(content) > 50 else '')
        print(f"HTML content: '{truncated_html}'")
        print(f"Meta description: '{result}'")
        print(f"Length: {len(result)}")
        within_limit = 'Yes' if len(result) <= META_DESCRIPTION_MAX_LENGTH else 'No'
        print(f"Within limit: {within_limit}")
        print()

def main():
    print("Comprehensive Test of Truncation Changes")
    print("=" * 60)
    print()

    test_utils_truncate()
    test_article_content_truncate()
    test_meta_description()

    print("Summary:")
    print("- Changed truncation string from '...' to 'This is so long, truncating.'")
    print("- Updated utils/index.ts truncate function")
    print("- Updated article content truncation to use utils function")
    print("- All truncation now uses consistent logic and string")
    print("- Edge cases handled (when max length < truncation text length)")

if __name__ == "__main__":
    main()
def truncate(string, max_length):
    truncation_string = "This is so long, truncating."
    return string[:max_length - len(truncation_string)] + truncation_string if len(string) > max_length else string

# Test cases
test_cases = [
    "This is a short string",
    "This is a very long string that should definitely be truncated because it exceeds the maximum length",
    "Just about to be truncated string that is right at the limit of being truncated",
    "",  # Empty string edge case
    "A"   # Single character edge case
]

# Test each case with different max lengths
print("Testing with different max lengths:")
for max_len in [20, 50, 100]:
    print(f"\n=== Max length: {max_len} ===")
    for s in test_cases:
        print(f"\nOriginal ({len(s)} chars): \"{s}\"")
        truncated = truncate(s, max_len)
        print(f"Truncated ({len(truncated)} chars): \"{truncated}\"")
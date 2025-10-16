def truncate(string, max_length):
    truncation_string = 'This is so long, truncating.'
    return string[:max_length - len(truncation_string)] + truncation_string if len(string) > max_length else string

# Test cases
test_cases = [
    "This is a short string",
    "This is a very long string that should definitely be truncated because it exceeds the maximum length",
    "Just about to be truncated string that is right at the limit of being cut off",
    "",  # Empty string edge case
    "A"   # Single character edge case
]

# Test each case
for s in test_cases:
    print(f"\nOriginal ({len(s)} chars): '{s}'")
    print(f"Truncated (max 50): '{truncate(s, 50)}'")
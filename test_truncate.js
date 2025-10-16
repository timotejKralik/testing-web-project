// Recreate the truncate function in plain JavaScript for testing
function truncate(string, maxLength) {
    const truncationString = "This is so long, truncating.";
    return (string.length > maxLength) ? string.slice(0, maxLength - truncationString.length) + truncationString : string;
}

// Test cases
const testCases = [
    "This is a short string",
    "This is a very long string that should definitely be truncated because it exceeds the maximum length",
    "Just about to be truncated string that is right at the limit of being truncated",
    "",  // Empty string edge case
    "A"   // Single character edge case
];

// Test each case with different max lengths
console.log("Testing with different max lengths:");
[20, 50, 100].forEach(maxLen => {
    console.log(`\n=== Max length: ${maxLen} ===`);
    testCases.forEach(str => {
        console.log(`\nOriginal (${str.length} chars): "${str}"`);
        console.log(`Truncated: "${truncate(str, maxLen)}"`);
    });
});
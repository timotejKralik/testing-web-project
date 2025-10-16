// Test script to verify truncate function behavior

// Simulate the truncate function - BEFORE change
function truncate_before(string, maxLength) {
  return (string.length > maxLength) ? string.slice(0, maxLength - 1) + '...' : string;
}

// Simulate the truncate function - AFTER change
function truncate_after(string, maxLength) {
  return (string.length > maxLength) ? string.slice(0, maxLength - 1) + 'This is so long, truncating.' : string;
}

// Test cases
const testCases = [
  { input: "This is a very long string that needs to be truncated", maxLength: 20 },
  { input: "Short", maxLength: 20 },
  { input: "Exactly twenty chars", maxLength: 20 },
  { input: "A".repeat(100), maxLength: 50 }
];

console.log("=== BEFORE (using '...') ===");
testCases.forEach((test, idx) => {
  const result = truncate_before(test.input, test.maxLength);
  console.log(`Test ${idx + 1}:`);
  console.log(`  Input: "${test.input.substring(0, 50)}${test.input.length > 50 ? '...' : ''}"`);
  console.log(`  Max Length: ${test.maxLength}`);
  console.log(`  Result: "${result}"`);
  console.log(`  Result Length: ${result.length}`);
  console.log();
});

console.log("\n=== AFTER (using 'This is so long, truncating.') ===");
testCases.forEach((test, idx) => {
  const result = truncate_after(test.input, test.maxLength);
  console.log(`Test ${idx + 1}:`);
  console.log(`  Input: "${test.input.substring(0, 50)}${test.input.length > 50 ? '...' : ''}"`);
  console.log(`  Max Length: ${test.maxLength}`);
  console.log(`  Result: "${result}"`);
  console.log(`  Result Length: ${result.length}`);
  console.log();
});

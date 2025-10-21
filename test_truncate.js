// Test script to verify truncation behavior
const { truncate } = require('./apps/frontend/utils/index.ts');

// Test cases
const testCases = [
  {
    input: "This is a short string",
    maxLength: 50,
    description: "Short string (no truncation needed)"
  },
  {
    input: "This is a very long string that should definitely be truncated because it exceeds the maximum length",
    maxLength: 30,
    description: "Long string (truncation needed)"
  },
  {
    input: "Exactly thirty characters long",
    maxLength: 30,
    description: "String exactly at max length"
  },
  {
    input: "Exactly thirty-one characters!",
    maxLength: 30,
    description: "String one character over max length"
  }
];

console.log("Testing truncation function:");
console.log("=" * 50);

testCases.forEach((testCase, index) => {
  console.log(`\nTest ${index + 1}: ${testCase.description}`);
  console.log(`Input: "${testCase.input}"`);
  console.log(`Max length: ${testCase.maxLength}`);
  console.log(`Input length: ${testCase.input.length}`);

  try {
    const result = truncate(testCase.input, testCase.maxLength);
    console.log(`Result: "${result}"`);
    console.log(`Result length: ${result.length}`);
  } catch (error) {
    console.log(`Error: ${error.message}`);
  }
});
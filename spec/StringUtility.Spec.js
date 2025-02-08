// Import the functions
const { capitalize, reverseString } = require('../src/stringUtils.js');

describe('capitalize function', () => {
  it('should capitalize "hello" to "Hello"', () => {
    expect(capitalize("hello")).toBe("Hello");
  });

  it('should return an empty string for an empty input', () => {
    expect(capitalize("")).toBe("");
  });

  it('should capitalize a single character "a" to "A"', () => {
    expect(capitalize("a")).toBe("A");
  });
});

describe('reverseString function', () => {
  it('should reverse "hello" to "olleh"', () => {
    expect(reverseString("hello")).toBe("olleh");
  });

  it('should return an empty string for an empty input', () => {
    expect(reverseString("")).toBe("");
  });

  it('should return "madam" for the palindrome "madam"', () => {
    expect(reverseString("madam")).toBe("madam");
  });
});

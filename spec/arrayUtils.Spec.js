// Import the function to test
const { getElement } = require('../src/arrayUtils.js');

describe('getElement function', () => {
  // Test for valid index values
  it('should return the element at a valid index', () => {
    const arr = [10, 20, 30, 40, 50];
    expect(getElement(arr, 0)).toBe(10); // First element
    expect(getElement(arr, 2)).toBe(30); // Middle element
    expect(getElement(arr, 4)).toBe(50); // Last element
  });

  // Test for negative index
  it('should throw an error for negative index', () => {
    const arr = [10, 20, 30];
    expect(() => getElement(arr, -1)).toThrowError("Index out of bounds");
  });

  // Test for out-of-range index
  it('should throw an error for out-of-range index', () => {
    const arr = [10, 20, 30];
    expect(() => getElement(arr, 3)).toThrowError("Index out of bounds"); // Index is equal to array length
    expect(() => getElement(arr, 100)).toThrowError("Index out of bounds"); // Index far out of range
  });

  // Test for edge cases
  it('should handle an empty array by throwing an error', () => {
    const arr = [];
    expect(() => getElement(arr, 0)).toThrowError("Index out of bounds");
  });
});

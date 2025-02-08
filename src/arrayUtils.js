function getElement(arr, index) {
    if (index < 0 || index >= arr.length) {
      throw new Error("Index out of bounds");
    }
    return arr[index];
  }
  
  // Export the function
  module.exports = { getElement };
  
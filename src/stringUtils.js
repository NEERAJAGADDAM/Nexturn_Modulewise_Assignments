// stringUtils.js

// Correct the code and write it together
function capitalize(word) {
    if (!word) return "";
    return word[0].toUpperCase() + word.slice(1);
  }
  
  function reverseString(str) {
    return str.split("").reverse().join("");
  }
  
  // Export the functions
  module.exports = { capitalize, reverseString };
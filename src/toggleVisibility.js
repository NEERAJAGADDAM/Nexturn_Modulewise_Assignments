function toggleVisibility(element) {
    // Check if display is "none" or not set (empty string), and toggle accordingly
    if (element.style.display === "none" || element.style.display === "") {
      element.style.display = "block";
    } else {
      element.style.display = "none";
    }
  }
  
  // Export the function
  module.exports = { toggleVisibility };
  
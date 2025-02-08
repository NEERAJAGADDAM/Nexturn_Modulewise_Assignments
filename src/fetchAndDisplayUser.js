async function fetchAndDisplayUser(apiService, userId, element) {
    try {
      const user = await apiService.getUser(userId); // Fetch user data
      if (!user.name) throw new Error("Invalid user data");
      element.textContent = `Hello, ${user.name}`; // Update element text
    } catch (error) {
      element.textContent = error.message; // Set error message
    }
  }
  
  module.exports = { fetchAndDisplayUser }; // Export the function
  
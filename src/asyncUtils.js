function delayedGreeting(name, delay) {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(`Hello, ${name}!`);
      }, delay);
    });
  }
  
  // Export the function
  module.exports = { delayedGreeting };
  
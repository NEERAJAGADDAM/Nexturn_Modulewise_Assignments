function sendNotification(notificationService, message) {
    if (!message) {
      return "Failed to Send"; // Don't call send() if no message is provided
    }
  
    const status = notificationService.send(message);
    return status ? "Notification Sent" : "Failed to Send";
  }
  
  // Export the function
  module.exports = { sendNotification };
  
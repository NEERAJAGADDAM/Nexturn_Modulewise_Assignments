// Import the function to test
const { sendNotification } = require('../src/notificationService.js');

describe('sendNotification function', () => {
  let notificationService;

  beforeEach(() => {
    notificationService = {
      send: jasmine.createSpy('send'),
    };
  });
  

  it('should return "Notification Sent" when notification is successfully sent', () => {
    // Mock the send method to simulate success
    notificationService.send.and.returnValue(true);

    const message = "Test message";
    const result = sendNotification(notificationService, message);

    expect(notificationService.send).toHaveBeenCalledWith(message); // Ensure send() is called with the message
    expect(result).toBe("Notification Sent");
  });

  it('should return "Failed to Send" when notification sending fails', () => {
    // Mock the send method to simulate failure
    notificationService.send.and.returnValue(false);

    const message = "Test message";
    const result = sendNotification(notificationService, message);

    expect(notificationService.send).toHaveBeenCalledWith(message); // Ensure send() is called with the message
    expect(result).toBe("Failed to Send");
  });

  it('should not call send() if no message is provided', () => {
    const result = sendNotification(notificationService, null);
  
    // Ensure send() is not called
    expect(notificationService.send).not.toHaveBeenCalled();
  
    // Ensure the correct return value
    expect(result).toBe("Failed to Send");
  });
  
});

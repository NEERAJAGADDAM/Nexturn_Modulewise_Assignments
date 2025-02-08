const { toggleVisibility } = require('../src/toggleVisibility.js');

describe('toggleVisibility function', () => {
  let element;

  beforeEach(() => {
    // Create a real DOM element
    element = document.createElement('div');
    element.style.display = "block"; // Set initial display value
    spyOnProperty(element.style, 'display', 'set').and.callThrough(); // Spy on the setter for display
  });

  it('should set display to "none" if initially "block"', () => {
    toggleVisibility(element);

    // Check if the display property was updated
    expect(element.style.display).toBe("none");
  });

  it('should set display to "block" if initially "none"', () => {
    element.style.display = "none"; // Set initial state to "none"

    toggleVisibility(element);

    // Check if the display property was updated
    expect(element.style.display).toBe("block");
  });

  it('should call the setter for display property', () => {
    toggleVisibility(element);

    // Verify the spy on the setter was called
    expect(Object.getOwnPropertyDescriptor(element.style, 'display').set).toHaveBeenCalled();
  });
});

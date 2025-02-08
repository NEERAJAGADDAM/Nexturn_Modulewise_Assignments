// Import the function to test
const { delayedGreeting } = require('../src/asyncUtils.js');

describe('delayedGreeting function', () => {
  beforeEach(() => {
    jasmine.clock().install(); // Install Jasmine's mock clock
  });

  afterEach(() => {
    jasmine.clock().uninstall(); // Uninstall the mock clock after each test
  });

  it('should resolve with the correct greeting message', (done) => {
    const name = 'John';
    const delay = 1000;

    delayedGreeting(name, delay).then((message) => {
      expect(message).toBe(`Hello, ${name}!`);
      done(); // Indicate that the async test is complete
    });

    jasmine.clock().tick(delay); // Simulate the passage of time
  });

  it('should respect the specified delay', (done) => {
    const name = 'Jane';
    const delay = 2000;
  
    let isResolved = false;
    
    delayedGreeting(name, delay).then(() => {
      isResolved = true;
      expect(isResolved).toBe(true);
      done(); // Complete the async test
    });
  
    // Simulate time before the delay
    jasmine.clock().tick(delay - 1);
    expect(isResolved).toBe(false); // Should not resolve before delay
  
    // Simulate the remaining time
    jasmine.clock().tick(1); // Advance time to complete the delay
  });
  

  it('should not resolve before the specified delay', () => {
    const name = 'Doe';
    const delay = 3000;

    const promise = delayedGreeting(name, delay);

    let isResolved = false;
    promise.then(() => {
      isResolved = true;
    });

    jasmine.clock().tick(delay - 1); // Simulate time just before the delay ends
    expect(isResolved).toBe(false);

    jasmine.clock().tick(1); // Complete the remaining time
    return promise; // Return the promise to let Jasmine wait for it to resolve
  });
});

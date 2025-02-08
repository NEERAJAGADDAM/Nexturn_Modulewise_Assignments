const { fetchAndDisplayUser } = require('../src/fetchAndDisplayUser');

describe('fetchAndDisplayUser', () => {
  let mockApiService;
  let element;

  beforeEach(() => {
    mockApiService = {
      getUser: jasmine.createSpy('getUser').and.returnValue(Promise.resolve({ name: "John Doe" })),
    };

    // Mock DOM element
    element = document.createElement('div');
  });

  it('should set the correct textContent', async () => {
    await fetchAndDisplayUser(mockApiService, 1, element);

    expect(element.textContent).toBe("Hello, John Doe");
  });
});

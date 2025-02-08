const { JSDOM } = require('jsdom');

const dom = new JSDOM('<!DOCTYPE html><html><body></body></html>');

global.document = dom.window.document;
global.window = dom.window;

// Optionally set up other globals like navigator
global.navigator = dom.window.navigator;

console.log("JSDOM initialized successfully");

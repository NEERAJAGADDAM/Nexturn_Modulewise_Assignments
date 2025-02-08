export default {
  spec_dir: "spec",
  spec_files: [
    "**/*[sS]pec.?(m)js"
  ],
  helpers: [
    "../setup/jsdomSetup.js" // Path to the JSDOM setup file
  ],
  env: {
    stopSpecOnExpectationFailure: false,
    random: true,
    forbidDuplicateNames: true
  }
};


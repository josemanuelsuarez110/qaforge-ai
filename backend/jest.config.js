export default {
  testEnvironment: "node",
  transform: {},
  collectCoverageFrom: [
    "src/**/*.js",
    "!src/server.js"
  ],
  testMatch: [
    "tests/**/*.test.js"
  ]
};

export default {
  testEnvironment: "node",
  transform: {},
  roots: ["<rootDir>/tests"],
  collectCoverageFrom: [
    "src/**/*.js",
    "!src/server.js"
  ],
  testMatch: [
    "**/*.test.js"
  ]
};

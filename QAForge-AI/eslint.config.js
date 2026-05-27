module.exports = {
  languageOptions: {
    parser: require('@typescript-eslint/parser'),
    parserOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
    },
  },
  plugins: {
    '@typescript-eslint': require('@typescript-eslint/eslint-plugin'),
  },
  rules: {
    // Example rule: enforce consistent indentation
    'indent': ['error', 2],
    // Example rule: enforce semicolons
    'semi': ['error', 'always'],
    // Example rule: enforce quotes
    'quotes': ['error', 'single'],
    // Example rule: enforce trailing commas
    'comma-dangle': ['error', 'always-multiline'],
    // Example rule: enforce no console.log in production
    'no-console': ['error', { allow: ['warn', 'error'] }],
  },
};
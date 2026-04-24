import jwt from "jsonwebtoken";
import logger from "../../utils/logger.js";

export const login = async (req, res) => {
  try {
    const { email, password } = req.body;

    // Mock validation (replace with DB query in production)
    if (!email || !password) {
      return res.status(400).json({ error: "Email and password required" });
    }

    // Generate JWT
    const token = jwt.sign(
      { userId: "123", email, role: "admin" },
      process.env.JWT_SECRET || "secret-key",
      { expiresIn: "24h" }
    );

    logger.info(`User logged in: ${email}`);

    res.json({
      message: "Login successful",
      token,
      user: { userId: "123", email, role: "admin" }
    });
  } catch (error) {
    logger.error("Login error:", error.message);
    res.status(500).json({ error: error.message });
  }
};

export const register = async (req, res) => {
  try {
    const { email, password, name } = req.body;

    if (!email || !password || !name) {
      return res
        .status(400)
        .json({ error: "Email, password, and name required" });
    }

    // Mock registration (replace with DB insert in production)
    const token = jwt.sign(
      { userId: "new-user", email, role: "user" },
      process.env.JWT_SECRET || "secret-key",
      { expiresIn: "24h" }
    );

    logger.info(`User registered: ${email}`);

    res.json({
      message: "Registration successful",
      token,
      user: { userId: "new-user", email, name, role: "user" }
    });
  } catch (error) {
    logger.error("Registration error:", error.message);
    res.status(500).json({ error: error.message });
  }
};

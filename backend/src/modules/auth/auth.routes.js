import express from "express";
import jwt from "jsonwebtoken";
import { env } from "../../config/env.js";

const router = express.Router();

router.post("/login", (req, res) => {
  const { email } = req.body;

  if (!email) {
    return res.status(400).json({ error: "Email is required" });
  }

  const token = jwt.sign(
    {
      sub: email,
      role: "tester"
    },
    env.jwtSecret,
    { expiresIn: "1h" }
  );

  return res.json({ token });
});

export default router;

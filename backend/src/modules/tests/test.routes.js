import express from "express";
import { createTestRun } from "./test.controller.js";

const router = express.Router();

router.get("/", (_req, res) => {
  res.json({
    testRuns: [
      {
        id: "run_001",
        name: "Smoke Suite",
        status: "passed",
        environment: "staging",
        passCount: 24,
        failCount: 1,
        durationMs: 2840
      },
      {
        id: "run_002",
        name: "Regression Suite",
        status: "running",
        environment: "production",
        passCount: 63,
        failCount: 4,
        durationMs: 6120
      },
      {
        id: "run_003",
        name: "Checkout E2E",
        status: "failed",
        environment: "staging",
        passCount: 11,
        failCount: 5,
        durationMs: 4310
      }
    ]
  });
});

router.post("/run", createTestRun);

export default router;

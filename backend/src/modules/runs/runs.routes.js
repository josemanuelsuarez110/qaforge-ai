import express from "express";

const router = express.Router();

router.get("/", (_req, res) => {
  res.json({
    runs: [
      {
        id: "run_demo_001",
        status: "passed",
        projectId: "demo-project",
        durationMs: 2940
      }
    ]
  });
});

export default router;

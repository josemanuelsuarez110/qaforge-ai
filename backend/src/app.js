import express from "express";
import cors from "cors";
import helmet from "helmet";
import { env } from "./config/env.js";
import rateLimiter from "./middleware/rateLimiter.js";
import authRoutes from "./modules/auth/auth.routes.js";
import testRoutes from "./modules/tests/test.routes.js";
import runsRoutes from "./modules/runs/runs.routes.js";
import reportsRoutes from "./modules/reports/reports.routes.js";

const app = express();

app.use(helmet());
app.use(
  cors({
    origin(origin, callback) {
      if (!origin || env.corsOrigins.includes(origin)) {
        return callback(null, true);
      }

      return callback(new Error("Origin not allowed by CORS"));
    },
    methods: ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    credentials: true
  })
);
app.use(express.json());
app.use(rateLimiter);

app.get("/health", (_req, res) => {
  res.json({
    status: "ok",
    service: "qaforge-backend",
    environment: env.nodeEnv
  });
});

app.use("/api/auth", authRoutes);
app.use("/api/tests", testRoutes);
app.use("/api/runs", runsRoutes);
app.use("/api/reports", reportsRoutes);

app.use((err, _req, res, _next) => {
  res.status(500).json({
    error: err.message || "Internal server error"
  });
});

export default app;

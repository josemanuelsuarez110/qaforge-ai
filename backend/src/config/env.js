import dotenv from "dotenv";

dotenv.config();

export const env = {
  nodeEnv: process.env.NODE_ENV || "development",
  port: Number(process.env.PORT || 3001),
  jwtSecret: process.env.JWT_SECRET || "change-me",
  corsOrigins: (process.env.CORS_ORIGINS ||
    "http://localhost:3000,https://qaforge-ai-psi.vercel.app,https://qaforge-r2zgm6zy6-josemanuelsuarez110s-projects.vercel.app")
    .split(",")
    .map(origin => origin.trim())
    .filter(Boolean),
  redis: {
    host: process.env.REDIS_HOST || "127.0.0.1",
    port: Number(process.env.REDIS_PORT || 6379),
    db: Number(process.env.REDIS_DB || 0),
    disabled: process.env.REDIS_DISABLED
      ? process.env.REDIS_DISABLED === "true"
      : true
  },
  supabase: {
    url: process.env.SUPABASE_URL || "",
    anonKey: process.env.SUPABASE_ANON_KEY || ""
  }
};

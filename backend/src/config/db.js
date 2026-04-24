import { createClient } from "@supabase/supabase-js";
import { env } from "./env.js";
import logger from "../utils/logger.js";

let supabase = null;

if (env.supabase.url && env.supabase.anonKey) {
  supabase = createClient(env.supabase.url, env.supabase.anonKey);
} else {
  logger.warn("Supabase credentials are not configured. DB features are running in mock mode.");
}

export default supabase;

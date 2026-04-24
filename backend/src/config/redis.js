import Redis from "ioredis";
import { env } from "./env.js";

let redisConnection = null;

export const isRedisEnabled = () => !env.redis.disabled;

export const getRedisConnection = () => {
  if (!isRedisEnabled()) {
    return null;
  }

  if (!redisConnection) {
    redisConnection = new Redis({
      host: env.redis.host,
      port: env.redis.port,
      db: env.redis.db,
      maxRetriesPerRequest: null
    });
  }

  return redisConnection;
};

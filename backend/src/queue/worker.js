import { Worker } from "bullmq";
import { getRedisConnection, isRedisEnabled } from "../config/redis.js";
import logger from "../utils/logger.js";

const executeTestRun = async job => {
  logger.info("Running test job", {
    jobId: job.id,
    payload: job.data
  });

  await new Promise(resolve => setTimeout(resolve, 3000));

  const result = {
    status: "passed",
    durationMs: 3000,
    completedAt: new Date().toISOString(),
    aiSuggestion: `Consider adding retry coverage for suite "${job.data.testSuite}".`
  };

  logger.info("Test job completed", {
    jobId: job.id,
    result
  });

  return result;
};

if (!isRedisEnabled()) {
  logger.warn("Redis is disabled. Worker is running in dry mode and will not consume BullMQ jobs.");
} else {
  const worker = new Worker("testQueue", executeTestRun, {
    connection: getRedisConnection()
  });

  worker.on("failed", (job, error) => {
    logger.error("Test job failed", {
      jobId: job?.id,
      error: error.message
    });
  });

  worker.on("completed", job => {
    logger.info("Worker acknowledged completed job", {
      jobId: job.id
    });
  });
}

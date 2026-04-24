import { Queue } from "bullmq";
import { getRedisConnection, isRedisEnabled } from "../config/redis.js";

const mockJobs = [];

let queueInstance = null;

const getQueue = () => {
  if (!isRedisEnabled()) {
    return null;
  }

  if (!queueInstance) {
    queueInstance = new Queue("testQueue", {
      connection: getRedisConnection()
    });
  }

  return queueInstance;
};

export const addTestJob = async data => {
  const queue = getQueue();

  if (!queue) {
    const mockJob = {
      id: `mock-${Date.now()}`,
      name: "run-test",
      data,
      queueMode: "mock"
    };

    mockJobs.push(mockJob);
    return mockJob;
  }

  const job = await queue.add("run-test", data, {
    removeOnComplete: 100,
    removeOnFail: 100
  });

  return {
    id: job.id,
    name: job.name,
    data: job.data,
    queueMode: "redis"
  };
};

export const getMockJobs = () => mockJobs;

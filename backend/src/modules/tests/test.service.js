import { addTestJob } from "../../queue/testQueue.js";

export const queueTestRun = async payload => {
  const job = await addTestJob(payload);

  return {
    message: "Test run queued",
    jobId: job.id,
    queueMode: job.queueMode
  };
};

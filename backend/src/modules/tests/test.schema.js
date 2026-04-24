import { z } from "zod";

export const createTestRunSchema = z.object({
  projectId: z.union([z.string(), z.number()]),
  testSuite: z.string().min(1),
  environment: z.string().min(1).default("staging"),
  parallelism: z.number().int().min(1).max(20).default(4),
  triggerSource: z.enum(["manual", "ci", "schedule"]).default("manual")
});

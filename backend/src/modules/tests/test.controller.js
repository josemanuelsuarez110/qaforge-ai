import { createTestRunSchema } from "./test.schema.js";
import { queueTestRun } from "./test.service.js";

export const createTestRun = async (req, res) => {
  try {
    const payload = createTestRunSchema.parse(req.body);
    const result = await queueTestRun(payload);

    return res.status(200).json(result);
  } catch (error) {
    if (error.name === "ZodError") {
      return res.status(400).json({
        error: "Invalid request payload",
        details: error.flatten()
      });
    }

    return res.status(500).json({ error: error.message });
  }
};

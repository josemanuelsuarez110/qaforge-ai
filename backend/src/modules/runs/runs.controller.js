import logger from "../../utils/logger.js";

export const getRuns = async (req, res) => {
  try {
    // Mock data
    const runs = [
      {
        id: 1,
        name: "CI/CD Pipeline - Build 123",
        status: "completed",
        branch: "main",
        commit: "a1b2c3d4",
        passCount: 156,
        failCount: 3,
        skipCount: 2,
        duration: "4m 30s",
        timestamp: "2024-01-15T10:00:00Z"
      },
      {
        id: 2,
        name: "CI/CD Pipeline - Build 124",
        status: "running",
        branch: "develop",
        commit: "e5f6g7h8",
        passCount: 142,
        failCount: 5,
        skipCount: 0,
        duration: "2m 15s",
        timestamp: "2024-01-15T11:00:00Z"
      }
    ];

    res.json({ runs });
  } catch (error) {
    logger.error("Error fetching runs:", error.message);
    res.status(500).json({ error: error.message });
  }
};

export const getRunById = async (req, res) => {
  try {
    const { id } = req.params;

    const run = {
      id: parseInt(id),
      name: "CI/CD Pipeline - Build " + id,
      status: "completed",
      branch: "main",
      commit: "a1b2c3d4",
      passCount: 156,
      failCount: 3,
      duration: "4m 30s",
      tests: [
        {
          name: "Authentication",
          passed: 45,
          failed: 1,
          duration: "1m 20s"
        },
        {
          name: "Payments",
          passed: 62,
          failed: 2,
          duration: "1m 45s"
        },
        {
          name: "Users",
          passed: 49,
          failed: 0,
          duration: "1m 25s"
        }
      ],
      timestamp: "2024-01-15T10:00:00Z"
    };

    res.json(run);
  } catch (error) {
    logger.error("Error fetching run:", error.message);
    res.status(500).json({ error: error.message });
  }
};

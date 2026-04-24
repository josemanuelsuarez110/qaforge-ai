import logger from "../../utils/logger.js";

export const getReports = async (req, res) => {
  try {
    // Mock data
    const reports = [
      {
        id: 1,
        title: "Weekly Test Report - Week 15",
        type: "weekly",
        generatedAt: "2024-01-15T10:00:00Z",
        totalTests: 500,
        passed: 485,
        failed: 12,
        skipped: 3,
        passRate: 97,
        trend: "up"
      },
      {
        id: 2,
        title: "Daily Report - Jan 15",
        type: "daily",
        generatedAt: "2024-01-15T23:59:00Z",
        totalTests: 200,
        passed: 195,
        failed: 4,
        skipped: 1,
        passRate: 97.5,
        trend: "stable"
      }
    ];

    res.json({ reports });
  } catch (error) {
    logger.error("Error fetching reports:", error.message);
    res.status(500).json({ error: error.message });
  }
};

export const getReportById = async (req, res) => {
  try {
    const { id } = req.params;

    const report = {
      id: parseInt(id),
      title: "Weekly Test Report - Week 15",
      type: "weekly",
      generatedAt: "2024-01-15T10:00:00Z",
      summary: {
        totalTests: 500,
        passed: 485,
        failed: 12,
        skipped: 3,
        passRate: 97,
        avgDuration: "2m 30s"
      },
      breakdown: [
        {
          module: "Authentication",
          total: 100,
          passed: 98,
          failed: 2,
          passRate: 98
        },
        {
          module: "Payments",
          total: 150,
          passed: 145,
          failed: 5,
          passRate: 96.67
        },
        {
          module: "Users",
          total: 120,
          passed: 118,
          failed: 2,
          passRate: 98.33
        },
        {
          module: "Notifications",
          total: 130,
          passed: 124,
          failed: 3,
          passRate: 95.38
        }
      ],
      aiSuggestions: [
        "Consider adding tests for edge cases in payment module",
        "Notifications module could benefit from load testing",
        "Add regression tests for recently fixed bugs"
      ]
    };

    res.json(report);
  } catch (error) {
    logger.error("Error fetching report:", error.message);
    res.status(500).json({ error: error.message });
  }
};

export const generateReport = async (req, res) => {
  try {
    const { type, startDate, endDate } = req.body;

    if (!type) {
      return res.status(400).json({ error: "Report type required" });
    }

    logger.info(`Report generation started: ${type}`);

    res.json({
      message: "Report generation queued",
      reportId: "report-" + Date.now(),
      type,
      startDate,
      endDate,
      status: "generating"
    });
  } catch (error) {
    logger.error("Error generating report:", error.message);
    res.status(500).json({ error: error.message });
  }
};

export const getAISuggestions = async (req, res) => {
  try {
    const suggestions = [
      "Añade casos de prueba para flujos de pago extremos",
      "Incluye validación adicional en el módulo de login cuando hay campos vacíos",
      "Genera pruebas de regresión para los últimos bugs críticos resueltos"
    ];

    res.json({
      source: "mock-ai",
      suggestions,
      generatedAt: new Date().toISOString()
    });
  } catch (error) {
    logger.error("Error fetching AI suggestions:", error.message);
    res.status(500).json({ error: error.message });
  }
};

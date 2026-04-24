import express from "express";

const router = express.Router();

router.get("/ai-suggestions", (_req, res) => {
  res.json({
    suggestions: [
      "Agrega casos de retry para autenticacion fallida en mobile.",
      "Crea un smoke test para rollback de pagos cuando falle el proveedor externo.",
      "Incluye cobertura de expiracion de sesion en escenarios de checkout."
    ]
  });
});

router.get("/summary", (_req, res) => {
  res.json({
    passRate: 0.94,
    flakyRate: 0.03,
    averageDurationMs: 3180,
    aiSuggestions: [
      "Add edge-case coverage for login retries",
      "Create smoke tests for payment rollback"
    ]
  });
});

export default router;

import request from "supertest";
import app from "../../src/app.js";

describe("Integration Tests - API", () => {
  test("GET /health should return ok", async () => {
    const res = await request(app).get("/health");

    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty("status");
    expect(res.body.status).toBe("ok");
  });

  test("POST /api/tests/run should queue a test", async () => {
    const res = await request(app)
      .post("/api/tests/run")
      .send({
        projectId: 1,
        testSuite: "smoke",
        name: "Test Run"
      });

    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty("jobId");
    expect(res.body.message).toBe("Test run queued");
  });

  test("POST /api/tests/run should fail without projectId", async () => {
    const res = await request(app)
      .post("/api/tests/run")
      .send({
        testSuite: "smoke"
      });

    expect(res.statusCode).toBe(400);
    expect(res.body).toHaveProperty("error");
  });

  test("GET /api/runs should return run summaries", async () => {
    const res = await request(app).get("/api/runs");

    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty("runs");
    expect(Array.isArray(res.body.runs)).toBe(true);
  });

  test("GET /api/reports/ai-suggestions should return suggestions", async () => {
    const res = await request(app).get("/api/reports/ai-suggestions");

    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty("suggestions");
    expect(Array.isArray(res.body.suggestions)).toBe(true);
  });

  test("POST /api/auth/login should return token", async () => {
    const res = await request(app)
      .post("/api/auth/login")
      .send({
        email: "test@example.com",
        password: "password123"
      });

    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty("token");
  });

  test("GET /api/tests should return test runs", async () => {
    const res = await request(app).get("/api/tests");

    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty("testRuns");
    expect(Array.isArray(res.body.testRuns)).toBe(true);
  });
});

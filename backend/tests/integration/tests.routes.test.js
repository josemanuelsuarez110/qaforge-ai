import request from "supertest";
import app from "../../src/app.js";

describe("POST /api/tests/run", () => {
  it("should create a test run", async () => {
    const response = await request(app).post("/api/tests/run").send({
      projectId: 1,
      testSuite: "smoke",
      environment: "staging",
      parallelism: 3,
      triggerSource: "ci"
    });

    expect(response.statusCode).toBe(200);
    expect(response.body.message).toBe("Test run queued");
    expect(response.body.jobId).toBeDefined();
  });

  it("should validate bad payloads", async () => {
    const response = await request(app).post("/api/tests/run").send({
      projectId: 1
    });

    expect(response.statusCode).toBe(400);
    expect(response.body.error).toBe("Invalid request payload");
  });
});

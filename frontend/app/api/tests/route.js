import { NextResponse } from "next/server";

export async function GET() {
  return NextResponse.json({
    testRuns: [
      {
        id: "run_001",
        name: "Smoke Suite",
        status: "completed",
        passCount: 24,
        failCount: 1,
        duration: "2m 48s",
        createdAt: "2026-04-24T13:05:00.000Z"
      },
      {
        id: "run_002",
        name: "Regression Suite",
        status: "running",
        passCount: 63,
        failCount: 4,
        duration: "6m 12s",
        createdAt: "2026-04-24T13:17:00.000Z"
      },
      {
        id: "run_003",
        name: "Checkout E2E",
        status: "failed",
        passCount: 11,
        failCount: 5,
        duration: "4m 31s",
        createdAt: "2026-04-24T13:28:00.000Z"
      }
    ]
  });
}

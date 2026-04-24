import { NextResponse } from "next/server";
import { hasSupabaseConfig, supabase } from "../../../lib/supabase.js";

export async function GET() {
  if (hasSupabaseConfig) {
    const { data, error } = await supabase
      .from("test_runs")
      .select("id, name, status, pass_count, fail_count, duration, created_at")
      .order("created_at", { ascending: false })
      .limit(10);

    if (!error && data?.length) {
      return NextResponse.json({
        testRuns: data.map(run => ({
          id: run.id,
          name: run.name,
          status: run.status,
          passCount: run.pass_count,
          failCount: run.fail_count,
          duration: run.duration,
          createdAt: run.created_at
        }))
      });
    }
  }

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

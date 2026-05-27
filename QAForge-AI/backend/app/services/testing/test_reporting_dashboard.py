from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
from app.core.supabase_config import supabase_config
from app.core.logging import logger
import json

class TestReportingDashboard:
    def __init__(self):
        self.supabase = supabase_config.get_client()

    async def generate_dashboard_data(self, time_range: str = "7d") -> Dict[str, Any]:
        """
        Generate comprehensive dashboard data for test reporting.

        Args:
            time_range: Time range for data aggregation (e.g., "1d", "7d", "30d")

        Returns:
            Dictionary containing dashboard data
        """
        try:
            # Parse time range
            days = int(time_range[:-1])
            start_date = datetime.utcnow() - timedelta(days=days)

            # Get test execution summary
            execution_summary = await self._get_execution_summary(start_date)

            # Get flaky test statistics
            flaky_tests = await self._get_flaky_test_stats(start_date)

            # Get test history trends
            test_trends = await self._get_test_trends(start_date)

            # Get recent test failures
            recent_failures = await self._get_recent_failures(start_date)

            return {
                "execution_summary": execution_summary,
                "flaky_tests": flaky_tests,
                "test_trends": test_trends,
                "recent_failures": recent_failures,
                "generated_at": datetime.utcnow().isoformat()
            }
        except Exception as e:
            logger.error(f"Failed to generate dashboard data: {str(e)}")
            return {"error": str(e)}

    async def _get_execution_summary(self, start_date: datetime) -> Dict[str, Any]:
        """Get summary of test executions"""
        try:
            response = await self.supabase.table("test_executions") \
                .select("total_tests, passed, failed, flaky, duration") \
                .gte("created_at", start_date.isoformat()) \
                .execute()

            if not response.data:
                return {}

            total_tests = sum(item["total_tests"] for item in response.data)
            passed = sum(item["passed"] for item in response.data)
            failed = sum(item["failed"] for item in response.data)
            flaky = sum(item["flaky"] for item in response.data)
            total_duration = sum(item["duration"] for item in response.data)
            execution_count = len(response.data)

            return {
                "total_tests": total_tests,
                "passed": passed,
                "failed": failed,
                "flaky": flaky,
                "pass_rate": passed / total_tests if total_tests > 0 else 0,
                "average_duration": total_duration / execution_count if execution_count > 0 else 0,
                "execution_count": execution_count
            }
        except Exception as e:
            logger.error(f"Failed to get execution summary: {str(e)}")
            return {}

    async def _get_flaky_test_stats(self, start_date: datetime) -> Dict[str, Any]:
        """Get statistics about flaky tests"""
        try:
            response = await self.supabase.table("flaky_tests") \
                .select("test_id, difference") \
                .gte("created_at", start_date.isoformat()) \
                .execute()

            if not response.data:
                return {}

            flaky_count = len(response.data)
            avg_difference = sum(item["difference"] for item in response.data) / flaky_count if flaky_count > 0 else 0

            return {
                "flaky_count": flaky_count,
                "average_difference": avg_difference,
                "most_flaky_tests": sorted(response.data, key=lambda x: x["difference"], reverse=True)[:5]
            }
        except Exception as e:
            logger.error(f"Failed to get flaky test stats: {str(e)}")
            return {}

    async def _get_test_trends(self, start_date: datetime) -> List[Dict[str, Any]]:
        """Get trends in test execution over time"""
        try:
            response = await self.supabase.table("test_executions") \
                .select("created_at, passed, failed, flaky") \
                .gte("created_at", start_date.isoformat()) \
                .order("created_at", desc=True) \
                .execute()

            if not response.data:
                return []

            # Group by day
            trends = {}
            for item in response.data:
                date = item["created_at"][:10]  # Extract date part
                if date not in trends:
                    trends[date] = {"passed": 0, "failed": 0, "flaky": 0, "count": 0}

                trends[date]["passed"] += item["passed"]
                trends[date]["failed"] += item["failed"]
                trends[date]["flaky"] += item["flaky"]
                trends[date]["count"] += 1

            # Convert to list and sort by date
            return sorted([
                {
                    "date": date,
                    "passed": data["passed"],
                    "failed": data["failed"],
                    "flaky": data["flaky"],
                    "pass_rate": data["passed"] / (data["passed"] + data["failed"]) if (data["passed"] + data["failed"]) > 0 else 0
                }
                for date, data in trends.items()
            ], key=lambda x: x["date"])
        except Exception as e:
            logger.error(f"Failed to get test trends: {str(e)}")
            return []

    async def _get_recent_failures(self, start_date: datetime, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent test failures"""
        try:
            response = await self.supabase.table("test_results") \
                .select("test_id, error, created_at") \
                .eq("status", "failed") \
                .gte("created_at", start_date.isoformat()) \
                .order("created_at", desc=True) \
                .limit(limit) \
                .execute()

            return response.data if response.data else []
        except Exception as e:
            logger.error(f"Failed to get recent failures: {str(e)}")
            return []

test_reporting_dashboard = TestReportingDashboard()
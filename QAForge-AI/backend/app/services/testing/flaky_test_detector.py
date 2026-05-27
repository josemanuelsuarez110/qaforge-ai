from typing import List, Dict, Any
from collections import defaultdict
from app.core.supabase_config import supabase_config
from app.core.logging import logger

class FlakyTestDetector:
    def __init__(self):
        self.supabase = supabase_config.get_client()
        self.threshold = 0.7  # 70% pass rate to consider a test stable

    async def detect_flaky_tests(self, test_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Detect flaky tests based on historical data and current results.

        Args:
            test_results: List of test execution results

        Returns:
            List of detected flaky tests
        """
        flaky_tests = []
        test_stats = defaultdict(lambda: {"passed": 0, "failed": 0, "total": 0})

        # Analyze current test results
        for result in test_results:
            test_id = result.get("test_id")
            if not test_id:
                continue

            if result.get("status") == "passed":
                test_stats[test_id]["passed"] += 1
            else:
                test_stats[test_id]["failed"] += 1
            test_stats[test_id]["total"] += 1

        # Compare with historical data
        for test_id, stats in test_stats.items():
            historical_data = await self._get_historical_test_data(test_id)

            if historical_data:
                historical_pass_rate = historical_data["passed"] / historical_data["total"]
                current_pass_rate = stats["passed"] / stats["total"]

                # Check if the test is flaky
                if abs(historical_pass_rate - current_pass_rate) > self.threshold:
                    flaky_tests.append({
                        "test_id": test_id,
                        "historical_pass_rate": historical_pass_rate,
                        "current_pass_rate": current_pass_rate,
                        "difference": abs(historical_pass_rate - current_pass_rate)
                    })

        # Save flaky test results to Supabase
        if flaky_tests:
            await self._save_flaky_test_results(flaky_tests)

        return flaky_tests

    async def _get_historical_test_data(self, test_id: str) -> Dict[str, int]:
        """
        Retrieve historical test data from Supabase.

        Args:
            test_id: The ID of the test to retrieve data for

        Returns:
            Dictionary containing historical test data
        """
        try:
            response = await self.supabase.table("test_history") \
                .select("status") \
                .eq("test_id", test_id) \
                .execute()

            if not response.data:
                return None

            passed = sum(1 for record in response.data if record["status"] == "passed")
            total = len(response.data)

            return {"passed": passed, "total": total}
        except Exception as e:
            logger.error(f"Failed to retrieve historical test data: {str(e)}")
            return None

    async def _save_flaky_test_results(self, flaky_tests: List[Dict[str, Any]]) -> None:
        """
        Save flaky test results to Supabase.

        Args:
            flaky_tests: List of detected flaky tests
        """
        try:
            data = [{
                "test_id": test["test_id"],
                "historical_pass_rate": test["historical_pass_rate"],
                "current_pass_rate": test["current_pass_rate"],
                "difference": test["difference"],
                "created_at": datetime.utcnow().isoformat()
            } for test in flaky_tests]

            response = await self.supabase.table("flaky_tests").insert(data).execute()
            logger.info(f"Flaky test results saved to Supabase: {response}")
        except Exception as e:
            logger.error(f"Failed to save flaky test results to Supabase: {str(e)}")

flaky_test_detector = FlakyTestDetector()
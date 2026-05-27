from typing import List, Dict, Any, Optional
import asyncio
from datetime import datetime
from app.core.supabase_config import supabase_config
from app.core.logging import logger
from app.services.testing.playwright_service import playwright_service
from app.services.testing.flaky_test_detector import flaky_test_detector

class TestExecutionEngine:
    def __init__(self):
        self.supabase = supabase_config.get_client()
        self.playwright_service = playwright_service
        self.flaky_test_detector = flaky_test_detector

async def execute_tests(self, test_scripts: List[str], parallel: bool = False, max_workers: int = 5) -> Dict[str, Any]:
    """
    Execute a set of test scripts with optional parallel execution.

    Args:
        test_scripts: List of test scripts to execute
        parallel: Whether to execute tests in parallel
        max_workers: Maximum number of parallel workers (only used when parallel=True)

    Returns:
        Dictionary containing overall execution results
    """
    results = {
        "total_tests": len(test_scripts),
        "passed": 0,
        "failed": 0,
        "flaky": 0,
        "test_results": [],
        "start_time": datetime.utcnow().isoformat(),
        "end_time": None,
        "duration": None
    }

    if parallel:
        # Create a semaphore to limit the number of concurrent workers
        semaphore = asyncio.Semaphore(max_workers)

        async def limited_execute(script):
            async with semaphore:
                return await self._execute_single_test(script)

        test_results = await asyncio.gather(
            *[limited_execute(script) for script in test_scripts]
        )
    else:
        test_results = []
        for script in test_scripts:
            result = await self._execute_single_test(script)
            test_results.append(result)

        # Process results
        for result in test_results:
            results["test_results"].append(result)
            if result["status"] == "passed":
                results["passed"] += 1
            elif result["status"] == "failed":
                results["failed"] += 1

        # Detect flaky tests
        flaky_results = await self.flaky_test_detector.detect_flaky_tests(test_results)
        results["flaky"] = len(flaky_results)

        results["end_time"] = datetime.utcnow().isoformat()
        results["duration"] = (datetime.fromisoformat(results["end_time"]) - datetime.fromisoformat(results["start_time"])).total_seconds()

        # Save execution results to Supabase
        await self._save_execution_results(results)

        return results

    async def _execute_single_test(self, test_script: str) -> Dict[str, Any]:
        """Execute a single test script and return results"""
        try:
            result = await self.playwright_service.execute_test(test_script)
            return result
        except Exception as e:
            logger.error(f"Error executing test: {str(e)}")
            return {
                "status": "failed",
                "error": str(e),
                "screenshots": [],
                "videos": [],
                "logs": []
            }

async def _save_execution_results(self, results: Dict[str, Any]) -> None:
    """Save execution results to Supabase"""
    try:
        data = {
            "total_tests": results["total_tests"],
            "passed": results["passed"],
            "failed": results["failed"],
            "flaky": results["flaky"],
            "start_time": results["start_time"],
            "end_time": results["end_time"],
            "duration": results["duration"],
            "test_results": results["test_results"],
            "created_at": datetime.utcnow().isoformat()
        }

        # Save execution summary
        execution_response = await self.supabase.table("test_executions").insert(data).execute()
        execution_id = execution_response.data[0]["id"]

        # Save individual test results
        for test_result in results["test_results"]:
            test_data = {
                "execution_id": execution_id,
                "test_id": test_result.get("test_id"),
                "status": test_result.get("status"),
                "duration": test_result.get("duration"),
                "screenshots": test_result.get("screenshots", []),
                "videos": test_result.get("videos", []),
                "logs": test_result.get("logs", []),
                "error": test_result.get("error"),
                "created_at": datetime.utcnow().isoformat()
            }
            await self.supabase.table("test_results").insert(test_data).execute()

        logger.info(f"Test execution results saved to Supabase with ID: {execution_id}")
    except Exception as e:
        logger.error(f"Failed to save test execution results to Supabase: {str(e)}")

test_execution_engine = TestExecutionEngine()
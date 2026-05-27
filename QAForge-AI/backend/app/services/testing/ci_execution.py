from typing import List, Dict, Any, Optional
from datetime import datetime
import asyncio
from app.core.supabase_config import supabase_config
from app.core.logging import logger
from app.services.testing.test_execution_engine import test_execution_engine

class CIExecution:
    def __init__(self):
        self.supabase = supabase_config.get_client()
        self.test_execution_engine = test_execution_engine

    async def execute_ci_pipeline(self, test_scripts: List[str], pipeline_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a CI pipeline with the given test scripts and configuration.

        Args:
            test_scripts: List of test scripts to execute
            pipeline_config: Configuration for the CI pipeline

        Returns:
            Dictionary containing pipeline execution results
        """
        results = {
            "status": "failed",
            "start_time": datetime.utcnow().isoformat(),
            "end_time": None,
            "duration": None,
            "test_results": [],
            "error": None
        }

        try:
            # Validate pipeline configuration
            self._validate_pipeline_config(pipeline_config)

            # Execute tests
            execution_results = await self.test_execution_engine.execute_tests(
                test_scripts,
                parallel=pipeline_config.get("parallel_execution", False)
            )

            results["test_results"] = execution_results["test_results"]
            results["status"] = "passed" if execution_results["failed"] == 0 else "failed"

            # Save pipeline results to Supabase
            await self._save_pipeline_results(results, pipeline_config)

        except Exception as e:
            results["error"] = str(e)
            logger.error(f"CI pipeline execution failed: {str(e)}")

        results["end_time"] = datetime.utcnow().isoformat()
        results["duration"] = (datetime.fromisoformat(results["end_time"]) - datetime.fromisoformat(results["start_time"])).total_seconds()

        return results

    def _validate_pipeline_config(self, config: Dict[str, Any]) -> None:
        """Validate the CI pipeline configuration"""
        required_fields = ["pipeline_id", "project_id", "trigger"]
        for field in required_fields:
            if field not in config:
                raise ValueError(f"Missing required field in pipeline configuration: {field}")

        # Add default values if not provided
        config.setdefault("parallel_execution", False)
        config.setdefault("max_retries", 3)
        config.setdefault("timeout", 3600)  # 1 hour default timeout

    async def _save_pipeline_results(self, results: Dict[str, Any], config: Dict[str, Any]) -> None:
        """Save CI pipeline results to Supabase"""
        try:
            data = {
                "pipeline_id": config["pipeline_id"],
                "project_id": config["project_id"],
                "trigger": config["trigger"],
                "status": results["status"],
                "start_time": results["start_time"],
                "end_time": results["end_time"],
                "duration": results["duration"],
                "test_count": len(results["test_results"]),
                "failed_tests": sum(1 for r in results["test_results"] if r["status"] == "failed"),
                "created_at": datetime.utcnow().isoformat()
            }

            response = await self.supabase.table("ci_pipelines").insert(data).execute()
            logger.info(f"CI pipeline results saved to Supabase: {response}")
        except Exception as e:
            logger.error(f"Failed to save CI pipeline results to Supabase: {str(e)}")

ci_execution = CIExecution()
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
import asyncio
from app.core.supabase_config import supabase_config
from app.core.logging import logger
from app.services.testing.test_execution_engine import test_execution_engine

class TestScheduler:
    def __init__(self):
        self.supabase = supabase_config.get_client()
        self.test_execution_engine = test_execution_engine
        self.scheduled_tasks = {}
        self.running_tasks = {}

    async def schedule_test(self, test_script: str, schedule_time: datetime, config: Dict[str, Any]) -> str:
        """
        Schedule a test to run at a specific time.

        Args:
            test_script: The test script to execute
            schedule_time: The time to schedule the test
            config: Configuration for the test execution

        Returns:
            The scheduled task ID
        """
        task_id = f"task_{datetime.utcnow().timestamp()}"

        self.scheduled_tasks[task_id] = {
            "test_script": test_script,
            "schedule_time": schedule_time,
            "config": config,
            "status": "scheduled"
        }

        # Calculate delay until scheduled time
        delay = (schedule_time - datetime.utcnow()).total_seconds()
        if delay < 0:
            delay = 0

        # Schedule the task
        asyncio.create_task(self._execute_scheduled_task(task_id, delay))

        logger.info(f"Test scheduled with ID {task_id} to run at {schedule_time}")
        return task_id

    async def _execute_scheduled_task(self, task_id: str, delay: float) -> None:
        """Execute a scheduled task after the specified delay"""
        try:
            await asyncio.sleep(delay)

            task = self.scheduled_tasks.get(task_id)
            if not task:
                return

            self.running_tasks[task_id] = task
            del self.scheduled_tasks[task_id]

            logger.info(f"Executing scheduled test with ID {task_id}")

            # Execute the test
            result = await self.test_execution_engine.execute_tests(
                [task["test_script"]],
                parallel=task["config"].get("parallel", False)
            )

            # Update task status
            self.running_tasks[task_id]["status"] = "completed"
            self.running_tasks[task_id]["result"] = result

            # Save to Supabase
            await self._save_scheduled_task_result(task_id, result)

        except Exception as e:
            logger.error(f"Error executing scheduled task {task_id}: {str(e)}")
            if task_id in self.running_tasks:
                self.running_tasks[task_id]["status"] = "failed"
                self.running_tasks[task_id]["error"] = str(e)

    async def _save_scheduled_task_result(self, task_id: str, result: Dict[str, Any]) -> None:
        """Save scheduled task result to Supabase"""
        try:
            task = self.running_tasks.get(task_id)
            if not task:
                return

            data = {
                "task_id": task_id,
                "test_script": task["test_script"],
                "scheduled_time": task["schedule_time"].isoformat(),
                "execution_time": datetime.utcnow().isoformat(),
                "status": task["status"],
                "result": result,
                "config": task["config"]
            }

            response = await self.supabase.table("scheduled_tasks").insert(data).execute()
            logger.info(f"Scheduled task result saved to Supabase: {response}")
        except Exception as e:
            logger.error(f"Failed to save scheduled task result to Supabase: {str(e)}")

    async def get_scheduled_tasks(self) -> Dict[str, Any]:
        """Get information about all scheduled tasks"""
        return {
            "scheduled": self.scheduled_tasks,
            "running": self.running_tasks
        }

    async def cancel_scheduled_task(self, task_id: str) -> bool:
        """Cancel a scheduled task"""
        if task_id in self.scheduled_tasks:
            del self.scheduled_tasks[task_id]
            logger.info(f"Scheduled task {task_id} cancelled")
            return True
        return False

test_scheduler = TestScheduler()
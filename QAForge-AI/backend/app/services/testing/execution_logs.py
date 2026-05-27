from typing import List, Dict, Any, Optional
from datetime import datetime
import logging
from app.core.supabase_config import supabase_config
from app.core.logging import logger

class ExecutionLogs:
    def __init__(self):
        self.supabase = supabase_config.get_client()
        self.logger = logger

    async def log_execution(self, execution_data: Dict[str, Any]) -> None:
        """
        Log test execution details to Supabase.

        Args:
            execution_data: Dictionary containing execution details
        """
        try:
            data = {
                "execution_id": execution_data.get("execution_id"),
                "test_id": execution_data.get("test_id"),
                "status": execution_data.get("status"),
                "start_time": execution_data.get("start_time"),
                "end_time": execution_data.get("end_time"),
                "duration": execution_data.get("duration"),
                "logs": execution_data.get("logs", []),
                "error": execution_data.get("error"),
                "created_at": datetime.utcnow().isoformat()
            }

            response = await self.supabase.table("execution_logs").insert(data).execute()
            self.logger.info(f"Execution logs saved to Supabase: {response}")
        except Exception as e:
            self.logger.error(f"Failed to save execution logs to Supabase: {str(e)}")

    async def get_execution_logs(self, execution_id: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Retrieve execution logs from Supabase.

        Args:
            execution_id: Optional execution ID to filter by
            limit: Maximum number of records to return

        Returns:
            List of execution log records
        """
        try:
            query = self.supabase.table("execution_logs").select("*").order("created_at", desc=True).limit(limit)

            if execution_id:
                query = query.eq("execution_id", execution_id)

            response = await query.execute()
            return response.data
        except Exception as e:
            self.logger.error(f"Failed to retrieve execution logs from Supabase: {str(e)}")
            return []

    def log_message(self, level: str, message: str, context: Optional[Dict[str, Any]] = None) -> None:
        """
        Log a message with the specified level.

        Args:
            level: Logging level (info, warning, error, debug)
            message: The message to log
            context: Additional context for the log message
        """
        log_method = getattr(self.logger, level.lower(), self.logger.info)
        log_method(message, extra={"context": context})

execution_logs = ExecutionLogs()
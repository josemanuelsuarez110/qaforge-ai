from typing import List, Dict, Any, Optional
from datetime import datetime
from app.core.supabase_config import supabase_config
from app.core.logging import logger

class TestHistory:
    def __init__(self):
        self.supabase = supabase_config.get_client()

    async def save_test_history(self, test_results: Dict[str, Any]) -> None:
        """
        Save test history to Supabase.

        Args:
            test_results: Dictionary containing test execution results
        """
        try:
            data = {
                "test_id": test_results.get("test_id"),
                "status": test_results.get("status"),
                "duration": test_results.get("duration"),
                "screenshots": test_results.get("screenshots", []),
                "videos": test_results.get("videos", []),
                "logs": test_results.get("logs", []),
                "error": test_results.get("error"),
                "created_at": datetime.utcnow().isoformat()
            }

            response = await self.supabase.table("test_history").insert(data).execute()
            logger.info(f"Test history saved to Supabase: {response}")
        except Exception as e:
            logger.error(f"Failed to save test history to Supabase: {str(e)}")

    async def get_test_history(self, test_id: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Retrieve test history from Supabase.

        Args:
            test_id: Optional test ID to filter by
            limit: Maximum number of records to return

        Returns:
            List of test history records
        """
        try:
            query = self.supabase.table("test_history").select("*").order("created_at", desc=True).limit(limit)

            if test_id:
                query = query.eq("test_id", test_id)

            response = await query.execute()
            return response.data
        except Exception as e:
            logger.error(f"Failed to retrieve test history from Supabase: {str(e)}")
            return []

test_history = TestHistory()
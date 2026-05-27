from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.services.testing.test_execution_engine import test_execution_engine
from app.services.testing.test_scheduler import test_scheduler
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/execute", response_model=Dict[str, Any])
async def execute_tests(
    test_scripts: List[str],
    parallel: bool = False,
    max_workers: int = 5,
    current_user: User = Depends(get_current_user)
):
    """
    Execute a set of test scripts.

    Args:
        test_scripts: List of test scripts to execute
        parallel: Whether to execute tests in parallel
        max_workers: Maximum number of parallel workers (only used when parallel=True)

    Returns:
        Dictionary containing execution results
    """
    try:
        results = await test_execution_engine.execute_tests(
            test_scripts,
            parallel=parallel,
            max_workers=max_workers
        )
        return results
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to execute tests: {str(e)}"
        )

@router.post("/schedule", response_model=Dict[str, Any])
async def schedule_test(
    test_script: str,
    schedule_time: datetime,
    config: Dict[str, Any],
    current_user: User = Depends(get_current_user)
):
    """
    Schedule a test to run at a specific time.

    Args:
        test_script: The test script to execute
        schedule_time: The time to schedule the test
        config: Configuration for the test execution

    Returns:
        Dictionary containing the scheduled task information
    """
    try:
        task_id = await test_scheduler.schedule_test(test_script, schedule_time, config)
        return {"task_id": task_id, "status": "scheduled"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to schedule test: {str(e)}"
        )

@router.get("/scheduled", response_model=Dict[str, Any])
async def get_scheduled_tasks(current_user: User = Depends(get_current_user)):
    """
    Get information about all scheduled tasks.

    Returns:
        Dictionary containing information about scheduled tasks
    """
    try:
        return await test_scheduler.get_scheduled_tasks()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get scheduled tasks: {str(e)}"
        )

@router.delete("/scheduled/{task_id}", response_model=Dict[str, Any])
async def cancel_scheduled_task(
    task_id: str,
    current_user: User = Depends(get_current_user)
):
    """
    Cancel a scheduled task.

    Args:
        task_id: The ID of the task to cancel

    Returns:
        Dictionary indicating success or failure
    """
    try:
        success = await test_scheduler.cancel_scheduled_task(task_id)
        if success:
            return {"status": "success", "message": f"Task {task_id} cancelled"}
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task {task_id} not found or already running"
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to cancel task: {str(e)}"
        )
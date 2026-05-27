from playwright.async_api import async_playwright
from typing import Optional, Dict, Any
import asyncio
from app.core.supabase_config import supabase_config
from app.core.logging import logger

class PlaywrightService:
    def __init__(self):
        self.supabase = supabase_config.get_client()

    async def execute_test(self, test_script: str, browser: str = "chromium", options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute a Playwright test script and save results to Supabase.

        Args:
            test_script: The Playwright test script to execute
            browser: The browser to use (chromium, firefox, webkit)
            options: Additional options for test execution

        Returns:
            Dictionary containing test execution results
        """
        results = {
            "status": "failed",
            "screenshots": [],
            "videos": [],
            "logs": [],
            "error": None
        }

        try:
            async with async_playwright() as p:
                browser_type = getattr(p, browser)
                browser_instance = await browser_type.launch(**options or {})

                context = await browser_instance.new_context(
                    record_video_dir="test-results/videos/",
                    record_video_size={"width": 1280, "height": 720}
                )

                page = await context.new_page()
                await page.set_viewport_size({"width": 1280, "height": 720})

                # Execute the test script
                exec(test_script, {'page': page, 'browser': browser_instance, 'context': context})

                # Capture results
                results["status"] = "passed"
                results["screenshots"] = await self._capture_screenshots(page)
                results["videos"] = await self._capture_videos(context)

                await context.close()
                await browser_instance.close()

        except Exception as e:
            results["error"] = str(e)
            logger.error(f"Test execution failed: {str(e)}")

        # Save results to Supabase
        await self._save_test_results(results)

        return results

async def _capture_screenshots(self, page) -> list:
    """Capture screenshots from the page"""
    screenshot_paths = []
    timestamp = int(time.time())

    # Capture full page screenshot
    full_page_path = f"test-results/screenshots/full_page_{timestamp}.png"
    await page.screenshot(path=full_page_path, full_page=True)
    screenshot_paths.append(full_page_path)

    # Capture viewport screenshot
    viewport_path = f"test-results/screenshots/viewport_{timestamp}.png"
    await page.screenshot(path=viewport_path, full_page=False)
    screenshot_paths.append(viewport_path)

    # Capture element screenshot if specified
    if hasattr(page, 'element_to_capture'):
        element_path = f"test-results/screenshots/element_{timestamp}.png"
        await page.element_to_capture.screenshot(path=element_path)
        screenshot_paths.append(element_path)

    return screenshot_paths

async def _capture_videos(self, context) -> list:
    """Capture videos from the context"""
    video_paths = []
    timestamp = int(time.time())

    # Get video path
    video_path = await context.video.path()
    if video_path:
        # Save video with timestamp
        new_video_path = f"test-results/videos/video_{timestamp}.webm"
        os.rename(video_path, new_video_path)
        video_paths.append(new_video_path)

        # Optionally save a thumbnail
        thumbnail_path = f"test-results/videos/thumbnail_{timestamp}.png"
        await context.video.save_as(thumbnail_path)
        video_paths.append(thumbnail_path)

    return video_paths

    async def _save_test_results(self, results: Dict[str, Any]) -> None:
        """Save test results to Supabase"""
        try:
            data = {
                "status": results["status"],
                "screenshots": results["screenshots"],
                "videos": results["videos"],
                "logs": results["logs"],
                "error": results["error"],
                "created_at": datetime.utcnow().isoformat()
            }

            response = await self.supabase.table("test_results").insert(data).execute()
            logger.info(f"Test results saved to Supabase: {response}")
        except Exception as e:
            logger.error(f"Failed to save test results to Supabase: {str(e)}")

playwright_service = PlaywrightService()
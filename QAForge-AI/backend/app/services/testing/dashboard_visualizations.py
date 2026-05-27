from typing import Dict, Any, List
from datetime import datetime, timedelta
import json
from app.core.supabase_config import supabase_config
from app.core.logging import logger
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class DashboardVisualizations:
    def __init__(self):
        self.supabase = supabase_config.get_client()

    async def generate_test_trends_chart(self, time_range: str = "7d") -> Dict[str, Any]:
        """
        Generate a chart showing test trends over time.

        Args:
            time_range: Time range for data aggregation (e.g., "1d", "7d", "30d")

        Returns:
            Dictionary containing chart data and configuration
        """
        try:
            # Parse time range
            days = int(time_range[:-1])
            start_date = datetime.utcnow() - timedelta(days=days)

            # Get test execution data
            response = await self.supabase.table("test_executions") \
                .select("created_at, passed, failed, flaky") \
                .gte("created_at", start_date.isoformat()) \
                .order("created_at", desc=True) \
                .execute()

            if not response.data:
                return {"error": "No test execution data found"}

            # Group data by day
            daily_data = {}
            for item in response.data:
                date = item["created_at"][:10]  # Extract date part
                if date not in daily_data:
                    daily_data[date] = {"passed": 0, "failed": 0, "flaky": 0, "count": 0}

                daily_data[date]["passed"] += item["passed"]
                daily_data[date]["failed"] += item["failed"]
                daily_data[date]["flaky"] += item["flaky"]
                daily_data[date]["count"] += 1

            # Prepare data for chart
            dates = sorted(daily_data.keys())
            passed = [daily_data[date]["passed"] for date in dates]
            failed = [daily_data[date]["failed"] for date in dates]
            flaky = [daily_data[date]["flaky"] for date in dates]

            # Create figure
            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=dates,
                y=passed,
                name='Passed',
                marker_color='rgb(76, 175, 80)'
            ))

            fig.add_trace(go.Bar(
                x=dates,
                y=failed,
                name='Failed',
                marker_color='rgb(244, 67, 54)'
            ))

            fig.add_trace(go.Bar(
                x=dates,
                y=flaky,
                name='Flaky',
                marker_color='rgb(255, 193, 7)'
            ))

            # Update layout
            fig.update_layout(
                barmode='stack',
                title='Test Execution Trends',
                xaxis_title='Date',
                yaxis_title='Number of Tests',
                legend_title='Test Status',
                hovermode='x unified'
            )

            return {
                "chart_type": "bar",
                "data": json.loads(fig.to_json()),
                "description": "This chart shows the distribution of test results over time, including passed, failed, and flaky tests."
            }
        except Exception as e:
            logger.error(f"Failed to generate test trends chart: {str(e)}")
            return {"error": str(e)}

    async def generate_test_status_pie_chart(self, time_range: str = "7d") -> Dict[str, Any]:
        """
        Generate a pie chart showing the current test status distribution.

        Args:
            time_range: Time range for data aggregation (e.g., "1d", "7d", "30d")

        Returns:
            Dictionary containing chart data and configuration
        """
        try:
            # Parse time range
            days = int(time_range[:-1])
            start_date = datetime.utcnow() - timedelta(days=days)

            # Get test execution summary
            response = await self.supabase.table("test_executions") \
                .select("passed, failed, flaky") \
                .gte("created_at", start_date.isoformat()) \
                .execute()

            if not response.data:
                return {"error": "No test execution data found"}

            # Calculate totals
            total_passed = sum(item["passed"] for item in response.data)
            total_failed = sum(item["failed"] for item in response.data)
            total_flaky = sum(item["flaky"] for item in response.data)

            # Create figure
            fig = go.Figure(data=[go.Pie(
                labels=['Passed', 'Failed', 'Flaky'],
                values=[total_passed, total_failed, total_flaky],
                hole=0.3,
                marker_colors=['rgb(76, 175, 80)', 'rgb(244, 67, 54)', 'rgb(255, 193, 7)']
            )])

            # Update layout
            fig.update_layout(
                title='Current Test Status Distribution',
                annotations=[dict(text=f'Total Tests: {total_passed + total_failed + total_flaky}',
                                x=0.5, y=0.5, font_size=14, showarrow=False)]
            )

            return {
                "chart_type": "pie",
                "data": json.loads(fig.to_json()),
                "description": "This pie chart shows the current distribution of test results, including passed, failed, and flaky tests."
            }
        except Exception as e:
            logger.error(f"Failed to generate test status pie chart: {str(e)}")
            return {"error": str(e)}

    async def generate_flaky_tests_bar_chart(self, time_range: str = "7d") -> Dict[str, Any]:
        """
        Generate a bar chart showing the most flaky tests.

        Args:
            time_range: Time range for data aggregation (e.g., "1d", "7d", "30d")

        Returns:
            Dictionary containing chart data and configuration
        """
        try:
            # Parse time range
            days = int(time_range[:-1])
            start_date = datetime.utcnow() - timedelta(days=days)

            # Get flaky test data
            response = await self.supabase.table("flaky_tests") \
                .select("test_id, difference") \
                .gte("created_at", start_date.isoformat()) \
                .order("difference", desc=True) \
                .limit(10) \
                .execute()

            if not response.data:
                return {"error": "No flaky test data found"}

            # Prepare data for chart
            test_ids = [item["test_id"] for item in response.data]
            differences = [item["difference"] for item in response.data]

            # Create figure
            fig = go.Figure(data=[go.Bar(
                x=test_ids,
                y=differences,
                marker_color='rgb(255, 193, 7)'
            )])

            # Update layout
            fig.update_layout(
                title='Most Flaky Tests',
                xaxis_title='Test ID',
                yaxis_title='Difference in Pass Rate',
                hovermode='x unified'
            )

            return {
                "chart_type": "bar",
                "data": json.loads(fig.to_json()),
                "description": "This bar chart shows the most flaky tests based on the difference in pass rate between historical data and current results."
            }
        except Exception as e:
            logger.error(f"Failed to generate flaky tests bar chart: {str(e)}")
            return {"error": str(e)}

dashboard_visualizations = DashboardVisualizations()
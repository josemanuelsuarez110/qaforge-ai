import time
from datetime import datetime
from typing import Dict, Any
import psycopg2
from psycopg2 import OperationalError
from app.core.connection_utils import database_connection

class HealthMonitor:
    def __init__(self):
        self.last_check = None
        self.status = "unknown"
        self.error = None

    def check_database_health(self) -> Dict[str, Any]:
        try:
            session = database_connection.get_session()
            session.execute("SELECT 1")
            session.close()
            self.status = "healthy"
            self.error = None
            self.last_check = datetime.utcnow()
            return {
                "status": self.status,
                "last_check": self.last_check.isoformat(),
                "error": self.error
            }
        except OperationalError as e:
            self.status = "unhealthy"
            self.error = str(e)
            self.last_check = datetime.utcnow()
            return {
                "status": self.status,
                "last_check": self.last_check.isoformat(),
                "error": self.error
            }
        except Exception as e:
            self.status = "error"
            self.error = str(e)
            self.last_check = datetime.utcnow()
            return {
                "status": self.status,
                "last_check": self.last_check.isoformat(),
                "error": self.error
            }

    def get_health_status(self) -> Dict[str, Any]:
        return {
            "status": self.status,
            "last_check": self.last_check.isoformat() if self.last_check else None,
            "error": self.error
        }

health_monitor = HealthMonitor()
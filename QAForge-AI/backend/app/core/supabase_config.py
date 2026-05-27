import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class SupabaseConfig:
    def __init__(self):
        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_KEY")
        self.supabase_client = self._create_client()

    def _create_client(self) -> Client:
        if not self.supabase_url or not self.supabase_key:
            raise ValueError("Supabase URL and Key must be set in environment variables")
        return create_client(self.supabase_url, self.supabase_key)

    def get_client(self) -> Client:
        return self.supabase_client

    def configure_auth(self):
        """Configure Supabase authentication"""
        self.supabase_client.auth.set_auth(self.supabase_url, self.supabase_key)
        self.supabase_client.auth.set_persist_session_callback(self._persist_session)
        self.supabase_client.auth.set_session_callback(self._handle_session)

    def _persist_session(self, session):
        """Persist session logic"""
        # Implement session persistence logic here
        pass

    def _handle_session(self, session):
        """Handle session logic"""
        # Implement session handling logic here
        pass

supabase_config = SupabaseConfig()
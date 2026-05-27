from supabase import Client

class RowLevelSecurity:
    def __init__(self, supabase_client: Client):
        self.supabase_client = supabase_client

    def enable_row_level_security(self, table_name: str):
        # Enable row-level security for the specified table
        self.supabase_client.rpc('enable_row_level_security', {'table_name': table_name})

    def set_row_level_policy(self, table_name: str, policy_name: str, policy_definition: str):
        # Set a row-level security policy for the specified table
        self.supabase_client.rpc('set_row_level_policy', {
            'table_name': table_name,
            'policy_name': policy_name,
            'policy_definition': policy_definition
        })

    def disable_row_level_security(self, table_name: str):
        # Disable row-level security for the specified table
        self.supabase_client.rpc('disable_row_level_security', {'table_name': table_name})
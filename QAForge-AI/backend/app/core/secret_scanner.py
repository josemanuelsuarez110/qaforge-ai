import re

class SecretScanner:
    def __init__(self):
        self.patterns = {
            "api_key": r"API_KEY\s*=\s*['\"][a-zA-Z0-9_-]{32,45}['\"]",
            "password": r"PASSWORD\s*=\s*['\"][^'\"]{8,}['\"]",
            "private_key": r"-----BEGIN (RSA|DSA|EC|OPENSSH) PRIVATE KEY-----"
        }

    def scan_file(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            for secret_type, pattern in self.patterns.items():
                if re.search(pattern, content):
                    return f"Found {secret_type} in {file_path}"
        return "No secrets found"
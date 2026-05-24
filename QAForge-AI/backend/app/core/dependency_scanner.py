import subprocess

class DependencyScanner:
    def scan_dependencies(self):
        result = subprocess.run(['pip', 'check'], capture_output=True, text=True)
        if result.returncode != 0:
            return result.stdout
        return "No vulnerabilities found"
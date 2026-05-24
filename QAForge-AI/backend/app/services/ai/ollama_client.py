import requests
from typing import Optional

class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url

    def generate_response(self, prompt: str, model: str = "llama2") -> str:
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={"model": model, "prompt": prompt}
        )
        response.raise_for_status()
        return response.json()["response"]

    def list_models(self) -> list:
        response = requests.get(f"{self.base_url}/api/tags")
        response.raise_for_status()
        return response.json()["models"]
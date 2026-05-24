from typing import List, Dict
from .ollama_client import OllamaClient

class MultiAgentSystem:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.ollama_client = OllamaClient(base_url)
        self.agents = {}

    def add_agent(self, name: str, model: str, system_prompt: str):
        self.agents[name] = {
            "model": model,
            "system_prompt": system_prompt,
            "conversation_history": []
        }

    def generate_response(self, agent_name: str, prompt: str) -> str:
        if agent_name not in self.agents:
            raise ValueError(f"Agent {agent_name} not found")

        agent = self.agents[agent_name]
        full_prompt = f"{agent['system_prompt']}\n\nConversation history:\n"
        for message in agent["conversation_history"]:
            full_prompt += f"{message['role']}: {message['content']}\n"

        full_prompt += f"\nUser: {prompt}"

        response = self.ollama_client.generate_response(full_prompt, agent["model"])

        agent["conversation_history"].append({"role": "User", "content": prompt})
        agent["conversation_history"].append({"role": "Assistant", "content": response})

        return response

    def get_conversation_history(self, agent_name: str) -> List[Dict]:
        if agent_name not in self.agents:
            raise ValueError(f"Agent {agent_name} not found")
        return self.agents[agent_name]["conversation_history"]
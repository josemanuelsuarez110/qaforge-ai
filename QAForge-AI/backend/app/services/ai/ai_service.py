from app.core.ai_rules import AIRules

class AIService:
    def __init__(self):
        self.rules = AIRules()

    def validate_prompt(self, prompt):
        return self.rules.validate_prompt(prompt)

    def generate_response(self, prompt):
        if not self.validate_prompt(prompt):
            raise ValueError("Prompt contains prohibited content")
        # Proceed with AI generation
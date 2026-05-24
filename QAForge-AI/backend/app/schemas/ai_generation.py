from pydantic import BaseModel

class AIGenerationRequest(BaseModel):
    prompt: str

class AIGenerationResponse(BaseModel):
    response: str
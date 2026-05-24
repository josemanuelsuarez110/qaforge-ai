from fastapi import APIRouter, Depends, HTTPException
from app.core.security import get_current_user
from app.services.ai.ai_service import AIService
from app.schemas.ai_generation import AIGenerationRequest, AIGenerationResponse

router = APIRouter()
ai_service = AIService()

@router.post("/generate", response_model=AIGenerationResponse)
def generate_ai_response(request: AIGenerationRequest, current_user: User = Depends(get_current_user)):
    if not ai_service.validate_prompt(request.prompt):
        raise HTTPException(status_code=400, detail="Invalid prompt content")
    response = ai_service.generate_response(request.prompt)
    return {"response": response}
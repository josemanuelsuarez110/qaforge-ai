from fastapi import APIRouter, Depends, HTTPException, status
from ...core.security import get_current_user
from ...core.database import get_db
from ...models.ai_generation import AIGeneration
from ...services.ai.ollama_client import OllamaClient
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/generate")
async def generate_text(prompt: str, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    ollama_client = OllamaClient()
    response = ollama_client.generate(prompt)

    ai_generation = AIGeneration(
        prompt=prompt,
        response=response,
        user_id=current_user["sub"]
    )
    db.add(ai_generation)
    db.commit()
    db.refresh(ai_generation)

    return {"response": response}

@router.get("/generations")
async def get_generations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    generations = db.query(AIGeneration).offset(skip).limit(limit).all()
    return generations

@router.get("/generations/{generation_id}")
async def get_generation(generation_id: int, db: Session = Depends(get_db)):
    generation = db.query(AIGeneration).filter(AIGeneration.id == generation_id).first()
    if not generation:
        raise HTTPException(status_code=404, detail="Generation not found")
    return generation
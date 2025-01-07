from pydantic import BaseModel
from src.orm import SessionLocal



class PokemonCreate(BaseModel):
    number: int
    name: str
    type1: str
    type2: str = None
    total: int
    hp: int
    attack: int
    defense: int
    sp_atk: int
    sp_def: int
    speed: int
    generation: int
    legendary: bool


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
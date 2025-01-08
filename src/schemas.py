from pydantic import BaseModel
from sqlalchemy.orm import Session
from .orm import SessionLocal

class PokemonBase(BaseModel):
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

class PokemonCreate(PokemonBase):
    pass

class Pokemon(PokemonBase):
    id: int

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
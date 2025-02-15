from pydantic import BaseModel
from typing import Optional
class PokemonSchema(BaseModel):
    id: int
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

    class Config:
        orm_mode: True

class PokemonResponse(BaseModel):
    message: str
    # data: Optional[PokemonSchema]

    class Config:
        orm_mode:True

class User(BaseModel):
    username: str
    password: str

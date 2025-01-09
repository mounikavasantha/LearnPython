from pydantic import BaseModel,ConfigDict
from typing import Optional,List


class PokemonResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    number: Optional[int] = None
    name: str
    type1: str
    type2: Optional[str] = None
    total: int
    hp: int
    attack: int
    defense: int
    sp_atk: int
    sp_def: int
    speed: int
    generation: int
    legendary: bool

class InputModification(BaseModel):
    id:int=None
    number:int=None
    name: Optional[str] = None
    type1: Optional[str] = None
    type2: Optional[str] = None
    total: Optional[int] = None
    hp: Optional[int] = None
    attack: Optional[int] = None
    defense: Optional[int] = None
    sp_atk: Optional[int] = None
    sp_def: Optional[int] = None
    speed: Optional[int] = None
    generation: Optional[int] = None
    legendary: Optional[int] = None

class PokemonDataResponse(BaseModel):
    total: int
    page: int
    per_page: int
    data: List[PokemonResponse]



# class payload:

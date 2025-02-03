from pydantic import BaseModel

class Pokemon(BaseModel):
    id:int
    name:str
    type:str
    total:int
    hp:int
    attack:int
    defense:int
    sp_atk:int
    sp_def:int
    speed:int
    generation:int
    legendary:bool
    

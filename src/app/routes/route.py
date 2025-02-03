from fastapi import APIRouter
from src.app.crud.crud import CRUD
from src.app.models.model import Pokemon

router = APIRouter()
crud = CRUD()

@router.get("/pokemon")
async def read_pokemondata(id: int):
    data = crud.get_pokemondata(id)
    return data

@router.post("/pokemon")
async def create_pokemondata(payload: Pokemon):
    data = crud.create_pokemondata(payload)
    return data
@router.get("/all pokenmondata")
async def read_all_pokemondata():
    data=crud.get_all_pokemondata()
    return data
@router.put("/update pokemondata with id")
async def update_pokemon_data(id:int,payload:Pokemon):
    data=crud.update_pokemon_data(id,payload)
    return data

@router.delete("/delete pokemondata with id")
async def delete_pokemon_data(id:int):
    data=crud.delete_pokemon_data(id)
    return data

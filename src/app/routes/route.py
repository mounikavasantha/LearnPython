from fastapi import APIRouter,Depends
from src.app.crud.crud import CRUD
from src.app.models.model import PokemonSchema, PokemonResponse
from src.app.database.orm import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()
crud = CRUD()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.get("/pokemon")
async def read_pokemondata(id: int,db:Session=Depends(get_db)):
    data = crud.get_pokemondata(id,db)
    return data

@router.post("/pokemon",response_model=PokemonResponse)
async def create_pokemondata(payload: PokemonSchema, db: Session = Depends(get_db)):
    data = crud.create_pokemondata(payload,db)
    return data
@router.get("/all pokenmondata")
async def read_all_pokemondata(db: Session = Depends(get_db)):
    data = crud.get_all_pokemondata(db)
    return data
@router.put("/update pokemondata with id", response_model=PokemonResponse)
async def update_pokemon_data(id: int, payload: PokemonSchema,db: Session = Depends(get_db)):
    data=crud.update_pokemon_data(id,payload,db)
    return data

@router.delete("/delete pokemondata with id")
async def delete_pokemon_data(id:int,db:Session=Depends(get_db)):
    data=crud.delete_pokemon_data(id,db)
    return data

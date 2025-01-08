from fastapi import APIRouter, Depends, HTTPException
from typing import List,Any
from sqlalchemy.orm import Session
from crud import Crud
from schemas import PokemonResponse, InputModification  # Change to absolute import
from orm import SessionLocal,Pokemon # Change to absolute import


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


# @router.get("/pokemon_data", response_model=List[PokemonResponse])
# def read_all_pokemon_data(db: Session = Depends(get_db)):
#     return crud.get_all_data(db)


@router.get(
    "/pokemon/{id}",
    summary="Retrieve a pokemon_data for a specific ID",
    response_model=PokemonResponse,
    responses={
        200: {
            "description": "pokeman data retrieved successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "name": "Bulbasaur",
                        "type1": "Grass",
                        "type2": "Poison",
                        "total": 318,
                    }
                }
            },
        },
        404: {
            "description": "No data was found.",
            "content": {
                "application/json": {
                    "example": {"detail": "No data was found for id: 123."}
                }
            },
        },
    },
)
def read_pokemon_data(
    id: int,
    db: Session = Depends(get_db),
    # key: str = Depends(header_scheme),
) -> Any:
    pokemon_data = Crud.get_all_data(id, db)
    if not pokemon_data:
        raise HTTPException(status_code=404, detail=f"No data was found for id: {id}")
    return pokemon_data


@router.post(
    "/create_pokemondata/",
    summary="Create a new pokemon data",
    response_model=PokemonResponse,
    responses={
        200: {
            "description": "The pokemon data has been created succeffully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "name": "Bulbasaur",
                        "type1": "Grass",
                        "type2": "Poison",
                        "total": 318,
                    }
                }
            },
        },
        404: {
            "description": "No data was found.",
            "content": {
                "application/json": {
                    "example": {"detail": "No data was found for id: 123."}
                }
            },
        },
    },
)
def create_pokemon_data(
    pokemon_data: PokemonResponse,
    db: Session = Depends(get_db),
) -> Any:
    data = Crud.create_pokemon_data(pokemon_data, db)
    return data
@router.put(
    "/update",
    summary="Update a pokemon data",
    response_model=PokemonResponse,
    responses={
        200: {
            "description": "The pokemon data has been updated successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "name": "Bulbasaur",
                        "type1": "Grass",
                        "type2": "Poison",
                        "total": 318,
                    }
                }
            },
        },
        404: {
            "description": "No data was found.",
            "content": {
                "application/json": {
                    "example": {"detail": "No data was found for id: 123."}
                }
            },
        },
    },
)
def update(
    id: int,
    data: InputModification,
    db: Session = Depends(get_db),
) -> Any:
    data = Crud.update_pokemon_data(id, data, db)
    return data

@router.delete(
    "/delete",
    summary="Delete a pokemon data",
    responses={
        204: {
            "description": "The pokemon data has been deleted successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "name": "Bulbasaur",
                        "type1": "Grass",
                        "type2": "Poison",
                        "total": 318,
                    }
                }
            },
        },
        404: {
            "description": "No data was found.",
            "content": {
                "application/json": {
                    "example": {"detail": "No data was found for id: 123."}
                }
            },
        },
    },
)
def delete_pokemon_data(
    id: int,
    db: Session = Depends(get_db),
) -> Any:
    Crud.delete_pokemon_data(id, db)
    return {
        "status": "Success",
        "message": "id removed from database successfully",
    }


    
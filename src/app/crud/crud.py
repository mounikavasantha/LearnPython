from typing import List
from src.app.database.orm import Pokemon
from sqlalchemy.orm import Session
from src.app.models.model import PokemonResponse, PokemonSchema
from fastapi import HTTPException
import traceback


class CRUD:

    def get_pokemondata(self, id: int, db: Session):
        try:
            result = db.query(Pokemon).filter(Pokemon.id == id).first()
            if not result:
                raise HTTPException(
                    status_code=404, detail="Pokemon not found for the id"
                )
            print(f"Found Pokemon: {result}")
            return result
        except HTTPException as e:
            raise e
        except Exception as e:
            print(f"Error: {str(e)}")
            print(traceback.format_exc())
            raise HTTPException(status_code=500, detail="Internal Server Error")

    def create_pokemondata(self, payload: PokemonSchema, db: Session):
        try:
            # Check if the Pokemon with the given ID already exists
            existing_pokemon = (
                db.query(Pokemon).filter(Pokemon.id == payload.id).first()
            )
            if existing_pokemon:
                raise HTTPException(
                    status_code=404, detail="Pokemon with this ID already exists"
                )

            new_pokemon = Pokemon(**payload.dict(exclude_unset=True))
            db.add(new_pokemon)
            db.commit()
            db.refresh(new_pokemon)
            return PokemonResponse(
                message="Pokemon data created successfully",

            )
        except HTTPException as e:
            raise e
        except Exception as e:
            db.rollback()
            print(f"Error: {str(e)}")
            print(traceback.format_exc())
            return PokemonResponse(message="Error creating Pokemon data", data=None)
    def get_all_pokemondata(self, db: Session):
        try:
            result=db.query(Pokemon).all()
            return result
        except Exception as e:
            return e

    def update_pokemon_data(self, id, payload,db):
        try:
            existing_pokemon = (
                db.query(Pokemon).filter(Pokemon.id == payload.id).first()
            )
            new_pokemon = Pokemon(**payload.dict(exclude_unset=True))
            db.add(new_pokemon)
            db.commit()
            db.refresh(new_pokemon)
            return PokemonResponse(
                message="Pokemon data updated successfully",

            )

        except Exception as e:
            return e

    def delete_pokemon_data(self, id,db):
        try:
            pokemon = db.query(Pokemon).filter(Pokemon.id == id).first()
            if pokemon:
                db.query(Pokemon).filter(Pokemon.id == id).delete()
                db.commit()
                return {"message": "Pokemon data deleted successfully"}
            return {"message": "Pokemon data not found"}
        except Exception as e:
            return e

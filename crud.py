from sqlalchemy.orm import Session
from orm import Pokemon
from schemas import PokemonResponse
from fastapi import HTTPException,Depends


class Crud:

    def get_all_data(id,db:Session):
        try:
            result = db.query(Pokemon).filter(Pokemon.id==id).scalar()
            if result:
                return PokemonResponse.model_validate(result)
            return None
        except Exception as e:
            print(f"no data found for the {id}, {e}")
            raise
    def create_pokemon_data(data:PokemonResponse, db: Session):
        try:
            check_data=db.query(Pokemon).filter(Pokemon.id==data.id).scalar()
            if check_data:
                raise HTTPException(
                    status_code=400, detail=f"data already exists with {data.id}"
                )
            pokemon_dict={
                "id": data.id,
                "number":data.number,
                "name": data.name,
                "type1": data.type1,
                "type2": data.type2,
                "total": data.total,
                "hp": data.hp,
                "attack": data.attack,
                "defense": data.defense,
                "sp_atk": data.sp_atk,
                "sp_def": data.sp_def,
                "speed": data.speed,
                "generation": data.generation,
                "legendary": data.legendary,
            }
            pokemon_data = Pokemon(**pokemon_dict)
            db.add(pokemon_data)
            db.commit()
            db.refresh(pokemon_data)
            return pokemon_data
        except Exception as e:
            db.rollback()
            raise e

    def update_pokemon_data(id,data:dict,db):
        try:
            pokemon_data = db.query(Pokemon).filter(Pokemon.id == id).scalar()
            if not pokemon_data:
                raise HTTPException(
                    status_code=404, detail=f"Pokemon with id {id} not found"
                )
            data_dict = data.dict(exclude_unset=True)
            for key, value in data_dict.items():
                setattr(pokemon_data, key, value)
            db.commit()
            return pokemon_data
        except Exception as e:
            db.rollback()
            raise e

    def delete_pokemon_data(id,db):
        try:
            print(id,"AAAAA")
            check_pokemon_data=db.query(Pokemon).filter(Pokemon.id==id).scalar()
            print(check_pokemon_data,00000)
            if not check_pokemon_data:
                raise HTTPException(status_code=404,detail=f"data not found for the id u provided {id}")
            db.delete(check_pokemon_data)
            db.commit()
            return check_pokemon_data
        except Exception as e:
            db.rollback()
            raise e

    def get_data(name, db, page, per_page):
        try:
            query = db.query(Pokemon)
            if name:
                query = query.filter(Pokemon.name == name)

            total = query.count()
            paginated_result = query.offset((page - 1) * per_page).limit(per_page).all()

            return {
                "total": total,
                "page": page,
                "per_page": per_page,
                "data": [PokemonResponse.model_validate(pokemon) for pokemon in paginated_result]
            }
        except Exception as e:
            print(f"Error retrieving data: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")
crud = Crud()

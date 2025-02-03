from typing import List
from src.app.models.model import Pokemon


class CRUD:
    def __init__(self):
        self.pokemon_data: List[Pokemon] = []

    def get_pokemondata(self, id: int):
        try:
            print(f"Searching for Pokemon with id: {id}")
            print(f"Current Pokemon data: {self.pokemon_data}")
            result = next(
                (pokemon for pokemon in self.pokemon_data if pokemon.id == id), None
            )
            print(f"Found Pokemon: {result}")
            return result
        except Exception as e:
            return e

    def create_pokemondata(self, payload: Pokemon):
        try:
            if any(pokemon.id == payload.id for pokemon in self.pokemon_data):
                print(f"Pokemon data already exists: {payload.id}")
                print(f"Pokemon data after insertion: {self.pokemon_data}")
                return {"message": f"Pokemon data already exists with id {payload.id}"}
            self.pokemon_data.append(payload)
            print(f"Pokemon data after insertion: {self.pokemon_data}")
            return {"message": "Pokemon data created successfully"}
        except Exception as e:
            return e

    def get_all_pokemondata(self):
        try:
            print(f"Fetching all Pokemon data: {self.pokemon_data}")
            return self.pokemon_data
        except Exception as e:
            return e

    def update_pokemon_data(self,id,payload):
        try:
            for pokemon in self.pokemon_data:
                if pokemon.id == id:
                    pokemon.name = payload.name
                    pokemon.type = payload.type
                    pokemon.total = payload.total
                    pokemon.hp = payload.hp
                    pokemon.attack = payload.attack
                    pokemon.defense = payload.defense
                    pokemon.sp_atk = payload.sp_atk
                    pokemon.sp_def = payload.sp_def
                    pokemon.speed = payload.speed
                    pokemon.generation = payload.generation
                    pokemon.legendary = payload.legendary
                    return {"message": "Pokemon data updated successfully"}
            return {"message": "Pokemon data not found"}
        except Exception as e:
            return e
    def delete_pokemon_data(self,id):
        try:
            for pokemon in self.pokemon_data:
                if pokemon.id==id:
                    self.pokemon_data.remove(pokemon)
                    return {"message":"Pokemon data deleted successfully"}
            return {"message":"Pokemon data not found"}
        except Exception as e:
            return e


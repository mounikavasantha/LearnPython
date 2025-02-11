import json
from sqlalchemy.orm import Session
from app.database.orm import SessionLocal, Pokemon


def validate_json(file_path):
    try:
        with open(file_path, "r") as f:
            json_data = json.load(f)
        print("JSON data is properly formatted.")
        return json_data
    except json.JSONDecodeError as e:
        print(f"Invalid JSON data: {e}")
        return None


def insert_pokemon_data(json_data):
    db: Session = SessionLocal()
    try:
        for entry in json_data:
            pokemon = Pokemon(
                number=entry["#"],
                name=entry["Name"],
                type1=entry["Type 1"],
                type2=entry["Type 2"],
                total=entry["Total"],
                hp=entry["HP"],
                attack=entry["Attack"],
                defense=entry["Defense"],
                sp_atk=entry["Sp. Atk"],
                sp_def=entry["Sp. Def"],
                speed=entry["Speed"],
                generation=entry["Generation"],
                legendary=entry["Legendary"],
            )
            db.add(pokemon)
        db.commit()
    finally:
        db.close()


# Example usage
file_path = r"C:\Users\VasanthaMounika(Anna\OneDrive - OneWorkplace\Desktop\Python_training\src\pokemon.json"
json_data = validate_json(file_path)

if json_data:
    insert_pokemon_data(json_data)

import json
from sqlalchemy.orm import sessionmaker
from orm import engine, Pokemon

with open('src/pokemon.json') as f:
    pokemon_data = json.load(f)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Iterate over the JSON data and create Pokemon objects
for p in pokemon_data:
    pokemon = Pokemon(
        number=p["#"],
        name=p["Name"],
        type1=p["Type 1"],
        type2=p["Type 2"],
        total=p["Total"],
        hp=p["HP"],
        attack=p["Attack"],
        defense=p["Defense"],
        sp_atk=p["Sp. Atk"],
        sp_def=p["Sp. Def"],
        speed=p["Speed"],
        generation=p["Generation"],
        legendary=p["Legendary"]
    )
    session.add(pokemon)

session.commit()
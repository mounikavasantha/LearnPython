import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer

from src.routes.route import router

app = FastAPI(
    title="Pokemon API",
    description="These are a simple API's on Pokemon data.",

)

app.get("/get all the pokemon data")
def get_pokemon_data():
    pass

app.include_router(router, prefix="/api/v1")
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8033)

import uvicorn
from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Pokemon API",
    description="These are a simple API's on Pokemon data.",
)

app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8033)
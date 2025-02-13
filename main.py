from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn
from src.app.routes.route import router

app = FastAPI()
security=HTTPBasic()

app = FastAPI()

security = HTTPBasic()


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "password"
    if (
        credentials.username != correct_username
        or credentials.password != correct_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

app.include_router(router,dependencies=[Depends(authenticate)])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

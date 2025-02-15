from src.app.routes.route import get_db
from fastapi import Depends,HTTPException,status
from fastapi.security import HTTPBasicCredentials,HTTPBasic
from sqlalchemy.orm import Session
from src.app.database.orm import User

security=HTTPBasic()
def verify_auth(credentials:HTTPBasicCredentials=Depends(security),db:Session=Depends(get_db)):
    user = db.query(User).filter(User.username == credentials.username).first()
    if user is None or user.password != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

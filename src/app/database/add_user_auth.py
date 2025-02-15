from sqlalchemy.orm import Session
from orm import SessionLocal, User


def add_user(username: str, password: str):
    db: Session = SessionLocal()
    try:
        user = User(username=username, password=password)
        db.add(user)
        db.commit()
        db.refresh(user)
        print(f"User {username} added with ID {user.id}")
    except Exception as e:
        db.rollback()
        print(f"Error adding user: {e}")
    finally:
        db.close()


add_user("admin", "password")

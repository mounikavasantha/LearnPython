from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL ="postgresql+psycopg2://new_user1:new_password1@localhost:5432/new_database"
print(DATABASE_URL)
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Pokemon(Base):
    __tablename__ = "pokemon_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer)
    name = Column(String(255))
    type1 = Column(String(50))
    type2 = Column(String(50))
    total = Column(Integer)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    sp_atk = Column(Integer)
    sp_def = Column(Integer)
    speed = Column(Integer)
    generation = Column(Integer)
    legendary = Column(Boolean)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
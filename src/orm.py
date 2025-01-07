import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Pokemon(Base):
    __tablename__ = "pokemon_table"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    name = Column(String)
    type1 = Column(String)
    type2 = Column(String, nullable=True)
    total = Column(Integer)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    sp_atk = Column(Integer)
    sp_def = Column(Integer)
    speed = Column(Integer)
    generation = Column(Integer)
    legendary = Column(Boolean)


DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+psycopg2://Mounika:Password@localhost:5432/pokemon_data"
)
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

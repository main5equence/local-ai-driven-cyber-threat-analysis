import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

os.makedirs("data", exist_ok=True)

DATABASE_URL = "sqlite:///data/threats.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


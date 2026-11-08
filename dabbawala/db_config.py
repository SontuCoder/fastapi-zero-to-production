from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

load_dotenv()

DB_URL = os.getenv("DB_URL")

engine = create_engine(DB_URL, echo=True)

Session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

class Base(DeclarativeBase):
    pass

def get_db():
    session = Session()
    try:
        yield session
    finally: 
        session.close()

def create_tables():
    Base.metadata.create_all(bind=engine)

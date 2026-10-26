from sqlmodel import SQLModel, create_engine, Session

# It will create a folder for DB locally. in Project you will pass a SQL Provider URL
DB_URL = "sqlite:///rangmanch.db"

engine = create_engine(DB_URL, echo=True)

def create_table():
    """Create Table using SQLModel Class from model.py"""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Dependency yhat provides a datanbase seassion per request"""
    with Session(engine) as seeion:
        yield seeion

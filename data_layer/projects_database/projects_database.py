from sqlmodel import create_engine, Session

DATABASE_URL = "sqlite:///data_layer/projects_database/projects_database.db"

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

def connect_with_the_database() -> Session:

    return Session(engine)

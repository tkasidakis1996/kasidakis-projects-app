from sqlmodel import create_engine, Session

DATABASE_URL = "sqlite:///data_layer/projects_database/projects_database.db"

# Create the engine
engine = create_engine(DATABASE_URL, echo=False)

def connect_with_the_database(test_engine = None) -> Session:

    if(test_engine):
        return Session(test_engine)

    return Session(engine)

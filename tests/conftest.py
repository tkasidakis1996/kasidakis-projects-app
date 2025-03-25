# tests/conftest.py

import pytest
from sqlmodel import SQLModel, create_engine, Session
from data_layer.projects_database.tables import Project
from datetime import date

# Temporary in-memory SQLite database
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL, echo=False)

# Use actual date objects here!
SAMPLE_PROJECTS = [
    Project(
        id=1,
        name="AI Research Tool",
        description="AI Tool",
        technologies_used="Python, FastAPI",
        start_date=date(2024, 1, 1),
        end_date=date(2024, 12, 31)
    ),
    Project(
        id=2,
        name="Drone System",
        description="Drone Mission Control",
        technologies_used="Python, Dronekit",
        start_date=date(2022, 1, 1),
        end_date=date(2022, 12, 31)
    )
]

@pytest.fixture(scope="function")
def projects_database():
    """Creates a fresh in-memory SQLite database with sample data."""
    SQLModel.metadata.create_all(engine)
    session = Session(engine)
    session.add_all(SAMPLE_PROJECTS)
    session.commit()
    yield session
    session.close()



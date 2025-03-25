from unittest.mock import patch

from sqlmodel import SQLModel, create_engine, Session

from data_layer.projects_database.tables import Project

from datetime import date

from app import app



def setup_test_engine():
    engine = create_engine("sqlite:///:memory:", echo=False)
    
    SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        session.add(Project(
            id=1,
            name="Test Project",
            description="Test description",
            technologies_used="Python",
            start_date=date(2024, 1, 1),
            end_date=date(2024, 12, 31)
        ))
        session.commit()
    
    return engine


@patch("api.projects.connection_with_the_projects_database")
def test_get_projects_success(mock_connection_with_the_projects_database):
    
    engine = setup_test_engine()
    
    mock_connection_with_the_projects_database.return_value = Session(engine)

    client = app.test_client()
    
    response = client.get("/projects")

    assert response.status_code == 200


@patch("api.projects.connection_with_the_projects_database")
def test_get_project_by_id_not_found(mock_connection_with_the_projects_database):
    
    engine = setup_test_engine()
    
    mock_connection_with_the_projects_database.return_value = Session(engine)

    client = app.test_client()
    
    response = client.get("/projects/999")

    assert response.status_code == 404


@patch("api.projects.connection_with_the_projects_database")
def test_get_projects_connection_error(mock_connection_with_the_projects_database):
    
    mock_connection_with_the_projects_database.side_effect = Exception("Database down")

    client = app.test_client()
    
    response = client.get("/projects")

    assert response.status_code == 500
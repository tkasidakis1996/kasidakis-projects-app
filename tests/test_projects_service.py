import pytest

from business_logic.projects_service import ProjectsService

from utils.exceptions.ProjectNotFound import ProjectNotFound

# Happy Path Test - Successfully Retrieve Project
def test_get_project_happy_path(projects_database):

    # Arrange
    projects_service = ProjectsService()

    # Act
    project = projects_service.get_projects_by_id(1, projects_database)

    # Assert
    assert project["name"] == "AI Research Tool"

def test_get_project_not_found(projects_database):

    projects_service = ProjectsService()

    with pytest.raises(ProjectNotFound):
        projects_service.get_projects_by_id(999, projects_database)

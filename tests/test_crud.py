from data_layer.projects_database.crud import read_projects, read_project_by_id

def test_read_projects(projects_database):

    # Act
    projects = read_projects(projects_database)
    
    # Assert
    assert len(projects) == 2
    
    assert projects[0]["name"] == "AI Research Tool"
    
    assert projects[1]["name"] == "Drone System"

def test_read_project_by_id_when_project_exists(projects_database):

    # Act
    project = read_project_by_id(1, projects_database)

    # Assert
    assert project["name"] == "AI Research Tool"

def test_read_project_by_id_when_project_does_not_exist(projects_database):

    # Act
    project = read_project_by_id(999, projects_database)
    
    # Assert
    assert project == {}

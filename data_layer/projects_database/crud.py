from sqlmodel import select, Session

from data_layer.projects_database.tables import Project

def read_projects(projects_database : Session) -> list[dict]:
    
    statement = select(Project)
    
    projects_from_the_database = projects_database.exec(statement).all()

    projects : list = []

    for one_project_from_database in projects_from_the_database:

        project = one_project_from_database.model_dump()

        projects.append(project)

    return projects


def read_project_by_id(project_id: int, projects_database : Session):
    
    statement = select(Project).where(Project.id == project_id)
    
    project_from_the_database = projects_database.exec(statement).first()
    
    if not project_from_the_database:

        return {}
    
    return project_from_the_database.model_dump()
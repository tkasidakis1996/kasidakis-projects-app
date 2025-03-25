from sqlmodel import select

from data_layer.projects_database.tables import Project

def read_projects(session):
    
    statement = select(Project)
    
    projects = session.exec(statement).all()
    
    return projects

# Function to Read a Project by ID
def read_project_by_id(project_id: int, session):
    
    statement = select(Project).where(Project.id == project_id)
    
    project = session.exec(statement).first()
    
    if not project:
        
        return None
    
    return project
from data_layer.projects_database.crud import read_projects, read_project_by_id

from utils.exceptions.ProjectNotFound import ProjectNotFound

class ProjectsService():

    def get_projects(self, projects_databse) -> list[dict]:

        projects : list[dict] = read_projects(projects_databse)

        return projects

    def get_projects_by_id(self, project_id : int, projects_databse) -> dict:

        specific_project : dict = read_project_by_id(project_id, projects_databse)

        if(not specific_project):
            raise ProjectNotFound(f"Project with ID {project_id} doesn't exist at the database")

        return specific_project
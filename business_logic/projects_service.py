from data_layer.projects_database.crud import read_projects, read_project_by_id

class ProjectsService():

    def get_projects(self, projects_databse) -> list[dict]:

        projects : list[dict] = read_projects(projects_databse)

        return projects

    def get_projects_by_id(self, project_id : int, projects_databse) -> dict:

        specific_project = read_project_by_id(project_id, projects_databse)

        return specific_project
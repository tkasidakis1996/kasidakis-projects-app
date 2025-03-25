from data_layer.crud import read_projects, read_project_by_id

class ProjectsService():

    def __init__():
        pass

    def get_projects(projects_databse) -> list[dict]:

        projects : list[dict] = read_projects(projects_databse)

        return projects

    def get_projects_by_id(project_id : int, projects_databse) -> dict:

        specific_project = read_project_by_id(project_id, projects_databse)

        return specific_project
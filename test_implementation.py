from business_logic.projects_service import ProjectsService

from data_layer.projects_database.projects_database import connect_with_the_database as connection_with_the_projects_database

projects_database = connection_with_the_projects_database()

projects_service = ProjectsService()

projects = projects_service.get_projects(projects_database)

print(projects)

specific_project = projects_service.get_projects_by_id(1, projects_database)

print(specific_project)


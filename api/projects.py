from flask import jsonify

from flask_smorest import Blueprint

from business_logic.projects_service import ProjectsService

from data_layer.projects_database.projects_database import connect_with_the_database as connection_with_the_projects_database


projects_router = Blueprint('projects', __name__, description='Operations on Kasidakis projects')

@projects_router.route('/projects', methods=['GET'])
def get_projects():

    projects_database = connection_with_the_projects_database()
    
    projects_service : ProjectsService = ProjectsService()

    projects = projects_service.get_projects(projects_database)

    return jsonify(projects, status=200, mimetype='application/json')

@projects_router.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):

    projects_database = connection_with_the_projects_database()
    
    projects_service : ProjectsService = ProjectsService()

    specific_project = projects_service.get_projects(project_id, projects_database)

    return jsonify(specific_project, status=200, mimetype='application/json')


from flask import jsonify, request

from flask_smorest import Blueprint, abort

from business_logic.projects_service import ProjectsService

from data_layer


projects_router = Blueprint('projects', __name__, description='Operations on Kasidakis projects')

@projects_router.route('/projects', methods=['GET'])
@projects_router.response(200, ProjectSchema(many=True))
def get_projects():

    try:
        # obtain here the connection with the databse
        
        projects_service : ProjectsService = ProjectsService()

        projects = projects_service.get_projects(projects_database)

    except:
        pass
    finally:
        # close connection here
        # and return the response here


# Endpoint to get a single project by ID
@blp.route('/projects/<int:project_id>', methods=['GET'])
@blp.response(200, ProjectSchema)
@blp.response(404, description="Project not found")
def get_project(project_id):
    """Get a specific project by ID"""
    project = next((proj for proj in projects if proj['id'] == project_id), None)
    if project:
        return project
    abort(404, message="Project not found")
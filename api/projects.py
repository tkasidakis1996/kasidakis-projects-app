from flask import jsonify

from flask_smorest import Blueprint

from business_logic.projects_service import ProjectsService

from data_layer.projects_database.projects_database import connect_with_the_database as connection_with_the_projects_database

from api.schemas_for_swagger.project_schema import ProjectSchema, ProjectListSchema

from utils.exceptions.ProjectNotFound import ProjectNotFound

from loguru import logger

projects_router = Blueprint('projects', __name__, description='Operations on Kasidakis projects')

@projects_router.route('/projects', methods=['GET'])
@projects_router.response(200, ProjectListSchema)
@projects_router.response(500, description="Database connection error or internal server error")
def get_projects():
    
    logger.info("Request received for projects")

    try:
        projects_database = connection_with_the_projects_database()
    
    except Exception:
        
        logger.error("Unable to connect with the Projects Database")
        
        return jsonify({"error": "Unable to connect with the Projects Database"}), 500

    try:
        projects_service: ProjectsService = ProjectsService()
        
        projects = projects_service.get_projects(projects_database)
    
    except Exception:
        
        projects_database.close()
        
        logger.error("Unable to retrieve projects from the Projects Database")
        
        return jsonify({"error": "Unable to retrieve projects from the Projects Database"}), 500
    
    logger.info("Request processed successfully")
    
    projects_database.close()

    return jsonify(projects), 200


@projects_router.route('/projects/<int:project_id>', methods=['GET'])
@projects_router.response(200, ProjectSchema)
@projects_router.response(404, description="Project not found")
@projects_router.response(500, description="Database connection error or internal server error")
def get_project(project_id):
    
    logger.info(f"Request received - Project with ID {project_id}")

    try:
        projects_database = connection_with_the_projects_database()
    
    except Exception:
        
        logger.error("Unable to connect with the Projects Database")
        
        return jsonify({"error": "Unable to connect with the Projects Database"}), 500

    projects_service: ProjectsService = ProjectsService()

    try:
        specific_project = projects_service.get_projects_by_id(project_id, projects_database)
    
    except ProjectNotFound:
        
        projects_database.close()
        
        logger.warning(f"Project with ID {project_id} not found")
        
        return jsonify({"error": f"Project with ID {project_id} not found"}), 404
    
    except Exception:
        
        projects_database.close()
        
        logger.error("Unable to retrieve project from the Projects Database")
        
        return jsonify({"error": "Unable to retrieve project from the Projects Database"}), 500

    logger.info(f"Project with ID {project_id} - Information retrieved successfully")
    
    projects_database.close()

    return jsonify(specific_project), 200

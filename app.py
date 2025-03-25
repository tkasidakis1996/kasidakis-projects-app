from flask import Flask
from flask_smorest import Api
from api.projects import projects_router

app = Flask(__name__)

# Flask-Smorest Configuration (Swagger Setup)
app.config['API_TITLE'] = 'Projects Service API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.3'
app.config['OPENAPI_URL_PREFIX'] = '/docs'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

api = Api(app)

# Register Blueprint (Router)
api.register_blueprint(projects_router)

if __name__ == "__main__":
    app.run(debug=True)
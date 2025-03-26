from flask import Flask
from flask_smorest import Api
from api.projects import projects_router  # Import your router

app = Flask(__name__)

app.config['API_TITLE'] = 'Kasidakis Projects API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.3'
app.config['OPENAPI_URL_PREFIX'] = '/docs'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

# Initialize API and Register Blueprints
api = Api(app)
api.register_blueprint(projects_router)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


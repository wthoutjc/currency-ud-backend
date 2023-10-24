from decouple import config

from flask import Flask, render_template
from flask_swagger_ui import get_swaggerui_blueprint

# Routes
from src.routes.currency import currency_bp
from src.routes.exchange_rate import exchange_rate_bp

# Database
from src.models.models import db

SECRET_KEY = config('SECRET_KEY')

# DB - MySQL
HOST = config('DATABASE_HOST')
USERNAME = config('DATABASE_USERNAME')
PASSWORD = config('DATABASE_PASSWORD')
DATABASE = config('DATABASE')

def create_app():
    """
    This is the factory function that creates the Flask app.
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'

    app.config['SECRET_KEY'] = SECRET_KEY
    # TODO: AUTH JWT - SECRET_KEY

    db.init_app(app)
    
    # Blueprints
    app.register_blueprint(currency_bp)
    app.register_blueprint(exchange_rate_bp)

    # Swagger
    SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
    API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

    # Call factory function to create our blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Currency API"
        },
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # Root endpoint
    @app.route("/index")
    def index():
        """
        This is the root endpoint of the API.
        ---
        parameters:
        - None
        responses:
        200:
            description: The root endpoint of the API.
        """
        return render_template("index.html")

    return app
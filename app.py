from flask import Flask, render_template
from flask_swagger_ui import get_swaggerui_blueprint

# Database
from src.models.models import db

# Routes
from src.routes.currency import currency_bp
from src.routes.exchange_rate import exchange_rate_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///currency_db.db'
    db.init_app(app)

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
    @app.route("/")
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

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
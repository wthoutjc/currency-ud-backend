from flask import Flask, render_template

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
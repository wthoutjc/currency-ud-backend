import os
from decouple import config

# Database
from src.models.models import db

time_zone = config('TZ')
os.environ['TZ'] = time_zone

from src.create_app import create_app

# Must for prod
# Update the SQLite database file path to use /tmp
app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/instance/currency_db.db'

# Lambda handler
def lambda_handler(event, context):
    return app(event, context)

if __name__ == '__main__':
    with app.app_context():
        app.instance_path = '/tmp/instance'
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)
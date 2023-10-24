import os
from decouple import config

# Database
from src.models.models import db

time_zone = config('TZ')
os.environ['TZ'] = time_zone

from src.create_app import create_app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)
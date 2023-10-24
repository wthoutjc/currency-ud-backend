import awsgi
import os
from decouple import config

# Database
from src.models.models import db

time_zone = config('TZ')
os.environ['TZ'] = time_zone

from src.create_app import create_app
app = create_app()

# Lambda handler
def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)
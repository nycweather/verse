from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

from app.api.article.models import Article
from app.api.user.models import User
from app.api.home.models import Popular


# Load the environment variables from the '.env' file
load_dotenv('.env')

# Get the database connection string from the environment variable
DB_CONNECTION_STRING = os.getenv('DB_CONNECTION_STRING')


def init_db(app):
    # Set the database URI from the environment variable
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION_STRING

    # Other database configurations (if needed)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)

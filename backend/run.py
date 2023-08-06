import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager


from app.database.db import db, init_db

def create_app():
    app = Flask(__name__)

    # Load configuration settings from '.env' file
    load_dotenv('.env')

    # Set the secret key and database connection from the environment variables
    app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_CONNECTION_STRING')

    # Initialize the database using the 'db' object from 'app.database.db'
    init_db(app)

    # Initialize the JWT manager
    JWTManager(app)

    # # Bcrypt
    # bcrypt = Bcrypt(app)

    # Register API blueprints
    from app.api.article.views import article_bp
    from app.api.user.views import user_bp
    from app.api.authentication.views import auth_bp
    from app.api.home.views import home_bp

    app.register_blueprint(home_bp, url_prefix='/api')
    app.register_blueprint(article_bp, url_prefix='/api/article')
    app.register_blueprint(user_bp, url_prefix='/api/user')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    # Enable CORS for all API routes
    CORS(app)

    with app.app_context():
        # Create the database tables if they don't exist
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='127.0.0.1', port=8080)

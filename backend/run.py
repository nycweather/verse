from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv 

# Import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    
    # Load configuration settings from '.env' file
    load_dotenv('.env')

    # Set the secret key and database connection from the environment variables
    app.secret_key = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_CONNECTION_STRING')

    # Initialize the database using the 'db' object from 'app.database.db'
    # from app.database.db import db
    # db.init_app(app)

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

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='127.0.0.1', port=8080)

# This file defines the API endpoints for authentication (e.g., login, registration).
# It uses Flask's Blueprint to create the 'authentication' API endpoints.
import re

from flask import Blueprint, jsonify, request

from app.database.db import db
from app.utils.http_constants import HTTP_CODES
from app.api.user.models import User

# Create a Blueprint for 'authentication' API endpoints.
auth_bp = Blueprint('authentication', __name__)

# Define API endpoints here (e.g., login, registration, etc.).

@auth_bp.route('/register', methods=['POST'])
def register():
    # Implement logic to handle user registration.
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']
    print(email, username, password)
    # Check if credentials are valid
    if not email or not username or not password:
        return jsonify({'message': 'Invalid credentials!'}), HTTP_CODES.HTTP_400_BAD_REQUEST
    # Checking username
    if len(username) < 4:
        return jsonify({'message': 'Username is too short!'}), HTTP_CODES.HTTP_400_BAD_REQUEST
    if username.isalnum() == False:
        return jsonify({'message': 'Username must be alphanumeric!'}), HTTP_CODES.HTTP_400_BAD_REQUEST
    # Checking password
    if len(password) < 6:
        return jsonify({'message': 'Password is too short!'}), HTTP_CODES.HTTP_400_BAD_REQUEST
    # Checking email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email) and len(email) < 9:
        return jsonify({'message': 'Invalid email!'}), HTTP_CODES.HTTP_400_BAD_REQUEST
    # Checking if user already exists
    user_check = User.query.filter_by(username=username).first()
    if user_check:
        return jsonify({'message': 'User already exists!'}), HTTP_CODES.HTTP_400_BAD_REQUEST
    #Checking if email already exists
    email_check = User.query.filter_by(email=email).first()
    if email_check:
        return jsonify({'message': 'Email already exists!'}), HTTP_CODES.HTTP_400_BAD_REQUEST
    # Generating password hash
    hashed_password = (password)
    # Creating user
    user = User(username=username, email=email, password=hashed_password, admin_level=0)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully!',
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                        'admin_level': user.admin_level
                        }
                    }), HTTP_CODES.HTTP_201_CREATED


@auth_bp.route('/login', methods=['POST'])
def login():
    # Implement logic to handle user login.
    pass

# More API endpoints can be added here for other authentication operations.

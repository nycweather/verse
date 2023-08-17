# This file defines the API endpoints for authentication (e.g., login, registration).
# It uses Flask's Blueprint to create the 'authentication' API endpoints.
from datetime import timedelta

from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt

from app.database.db import db
from app.utils.http_constants import HTTP_CODES
from app.api.user.models import User
from app.utils.helpers import register_helper

# Create a Blueprint for 'authentication' API endpoints.
auth_bp = Blueprint('authentication', __name__)

# Define API endpoints here (e.g., login, registration, etc.).

@auth_bp.route('/register', methods=['POST'])
def register():
    # Implement logic to handle user registration.
    return register_helper(request)

    

@auth_bp.route('/login', methods=['POST'])
def login():
    # Implement logic to handle user login.
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    # Check if credentials are valid
    if not username or not password:
        return jsonify({'message': 'Username or Password is incorrect!'}), HTTP_CODES.HTTP_400_BAD_REQUEST
    # Checking if user exists
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'Username or Password is incorrect!'}), HTTP_CODES.HTTP_400_BAD_REQUEST
    # Checking if password is correct
    password_check = Bcrypt().check_password_hash(user.password, password)
    if not password_check:
        return jsonify({'message': 'Username or Password is incorrect!'}), HTTP_CODES.HTTP_400_BAD_REQUEST
    # Setting JWT token
    refresh = create_refresh_token(identity=user.id)
    access = create_access_token(identity=user.id)
    return jsonify({
        'message': 'Logged in successfully!',
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'refresh_token': refresh,
            'access_token': access
        }
    }), HTTP_CODES.HTTP_200_OK

# Refresh token endpoint
@auth_bp.route('/refresh', methods=['GET'])
@jwt_required(refresh=True)
def refresh():
    # Implement logic to handle access token refresh.
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user, expires_delta=timedelta(hours=1))
    return jsonify({'access_token': new_token}), HTTP_CODES.HTTP_200_OK

# Logout endpoint
@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    return jsonify({'message': f'You are logged in as: {get_jwt_identity()}'}), HTTP_CODES.HTTP_200_OK
# More API endpoints can be added here for other authentication operations.

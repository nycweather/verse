# This file defines the API endpoints for user-related operations.
# It uses Flask's Blueprint to create the 'user' API endpoints.

from flask import Blueprint, jsonify, request

from app.utils.http_constants import HTTP_CODES
from app.api.user.models import User
from app.database.db import db

# Create a Blueprint for 'user' API endpoints.
user_bp = Blueprint('user', __name__)

# Define API endpoints here (e.g., user registration, profile update, etc.).

@user_bp.route('/update', methods=['POST'])
def update_user():
    if request.method == 'POST':
        user = User.query.filter_by(id=id).first()
        if user:
            user.name = request.json['name']
            user.email = request.json['email']
            user.password = request.json['password']
            db.session.commit()
            return jsonify({'message': 'User updated successfully!'}), HTTP_CODES.HTTP_200_OK
        else:
            return jsonify({'message': 'User not found!'}), HTTP_CODES.HTTP_404_NOT_FOUND
    elif request.method == 'DELETE':
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'User deleted successfully!'}), HTTP_CODES.HTTP_200_OK
        else:
            return jsonify({'message': 'User not found!'}), HTTP_CODES.HTTP_404_NOT_FOUND

# More API endpoints can be added here for other user-related operations.

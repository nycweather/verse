import re

from flask import request, jsonify
from app.database.db import db
from app.api.user.models import User
from app.utils.http_constants import HTTP_CODES
from flask_bcrypt import Bcrypt

def password_helper(password):
    # Hash the password using bcrypt
    bcrypt = Bcrypt()
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    return hashed_password

def email_helper(email):
    # Validate the email format
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) and len(email) >= 9

def register_helper(request: request):
    # Implement logic to handle user registration.
    email = request.json.get('email')
    username = request.json.get('username')
    password = request.json.get('password')

    # Check if credentials are valid
    if not email or not username or not password:
        return jsonify({'message': 'Invalid credentials!'}), HTTP_CODES.HTTP_400_BAD_REQUEST

    # Checking username
    if len(username) < 4 or not username.isalnum():
        return jsonify({'message': 'Invalid username!'}), HTTP_CODES.HTTP_400_BAD_REQUEST

    # Checking password
    if len(password) < 6 or not password.isalnum():
        return jsonify({'message': 'Invalid password!'}), HTTP_CODES.HTTP_400_BAD_REQUEST

    # Checking email
    if not email_helper(email):
        return jsonify({'message': 'Invalid email!'}), HTTP_CODES.HTTP_400_BAD_REQUEST

    # Checking if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists!'}), HTTP_CODES.HTTP_400_BAD_REQUEST

    # Checking if email already exists
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists!'}), HTTP_CODES.HTTP_400_BAD_REQUEST

    # Hashing the password
    hashed_password = password_helper(password)

    # Creating user
    user = User(username=username, email=email, password=hashed_password, admin_level=0)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'message': 'User created successfully!',
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'admin_level': user.admin_level
        }
    }), HTTP_CODES.HTTP_201_CREATED

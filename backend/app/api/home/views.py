# This file defines the views and endpoints for the homepage.

from flask import Blueprint, render_template

# Create a Blueprint for 'home' views
home_bp = Blueprint('home', __name__)

# Define homepage endpoint
@home_bp.route('/', methods=['GET'])
def index():
    # Render the 'index.html' template for the homepage
    return {'message': 'Home Page!'}

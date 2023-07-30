# This file defines the database models for users (e.g., 'User' model).
import pytz
from datetime import datetime

from app.database.db import db


class User(db.Model):
    # Define the 'User' model here (e.g., id, username, password, etc.).
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(pytz.timezone('EST')))
    updated_at = db.Column(db.DateTime, onupdate=datetime.now(pytz.timezone('EST')))
    articles = db.relationship('Article', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'
    
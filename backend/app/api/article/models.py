# This file defines the database models for the blog.
# It uses a database ORM like SQLAlchemy to create the 'Post' and 'Category' models.

import pytz
from datetime import datetime

from app.database.db import db

class Category(db.Model):
    # Define the 'Category' model here (e.g., id, name, etc.).
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    verified = db.Column(db.Boolean, default=False)

class Article(db.Model):
    # Define the 'Post' model here (e.g., id, title, content, etc.).
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(pytz.timezone('EST')))
    updated_at = db.Column(db.DateTime, onupdate=datetime.now(pytz.timezone('EST')))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    visits = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Article {self.title}\n<Owner {self.owner_id}>\n<Created at {self.created_at}>'

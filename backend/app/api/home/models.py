# This file defines the database models for most popular articles.
import pytz
from datetime import datetime

from app.database.db import db


class Popular(db.Model):
    # Define the 'Popular' model here (e.g., id, title, content, etc.).
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    added_to_table = db.Column(db.DateTime, default=datetime.now(pytz.timezone('EST')))
    visits = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Popular {self.title}\n<Owner {self.owner_id}>\n<Created at {self.created_at}>'
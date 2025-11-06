"""
This file defines the database models (tables) for the Flask app.
Each class represents a table in the SQLite database.
"""

from flask_sqlalchemy import SQLAlchemy  # ORM library for database handling
from flask_login import UserMixin        # Adds helpful user methods for login management
from datetime import datetime            # For timestamping database entries

# Create a global SQLAlchemy instance (we’ll link it to Flask in app.py)
db = SQLAlchemy()

# USER MODEL
class User(db.Model, UserMixin):
    # Primary key (unique identifier for each user)
    id = db.Column(db.Integer, primary_key=True)
    
    # Username field (must be unique and not empty)
    username = db.Column(db.String(100), nullable=False, unique=True)

    # Email field (also unique and required)
    email = db.Column(db.String(120), nullable=False, unique=True)

    # Password field (this will store a hashed password, not plaintext)
    password = db.Column(db.String(200), nullable=False)

    # Boolean flag to check if the user is an administrator
    is_admin = db.Column(db.Boolean, default=False)

# EVALUATION REQUEST MODEL
class EvaluationRequest(db.Model):
    # Primary key for each evaluation record
    id = db.Column(db.Integer, primary_key=True)

    # The name of the antique or item being evaluated
    item_name = db.Column(db.String(150), nullable=False)

    # Description text provided by the user
    description = db.Column(db.Text, nullable=False)

    # Preferred contact method (e.g., 'email' or 'phone')
    contact_method = db.Column(db.String(20))

    # Optional uploaded image file name
    image_filename = db.Column(db.String(100))

    # Automatically adds the current time when the record is created
    date_requested = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign key linking to the User who made the request
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

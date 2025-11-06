"""
Configuration file for the Flask web application.
This file centralises settings like secret keys and database connections.
Keeping configuration separate makes the project cleaner and more secure.
"""

import os  # Import the OS module to handle file paths and environment variables

# Get the absolute path to the current project directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define an 'instance' folder path to store database and sensitive files
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")

# Ensure the 'instance' folder exists (create if missing)
os.makedirs(INSTANCE_DIR, exist_ok=True)

class Config:
    # SECRET_KEY is used for session management and CSRF protection
    # In production, this should come from an environment variable, not hard-coded
    SECRET_KEY = os.environ.get("SECRET_KEY", "934e793aad901ff732c340df9d32c2d38a0cc690e90668c1f76bbfc600440f8e")

    # Build a path for the SQLite database located in the instance folder
    DB_PATH = os.path.join(INSTANCE_DIR, "lovejoy.db")

    # SQLAlchemy connection string for the SQLite database
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + DB_PATH

    # Disable event system to save memory (not needed in most apps)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

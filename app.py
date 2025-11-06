"""
Main Flask application file.
This is the entry point for running the web app.
It initialises Flask, connects extensions (SQLAlchemy, Bcrypt, LoginManager),
and defines simple routes (pages) to test the setup.
"""

# Import necessary Flask modules
from flask import Flask, render_template  # render_template displays HTML pages

# Import security and authentication libraries
from flask_bcrypt import Bcrypt           # Used for hashing passwords
from flask_login import LoginManager      # Handles user session management

# Import our configuration and models
from config import Config
from models import db, User, EvaluationRequest

# APP INITIALISATION
app = Flask(__name__)                     # Create the Flask application instance
app.config.from_object(Config)            # Load settings from Config class (config.py)

# INITIALISE EXTENSIONS
db.init_app(app)                          # Connect the database to the Flask app
bcrypt = Bcrypt(app)                      # Initialise Bcrypt for password hashing
login_manager = LoginManager(app)         # Set up login session manager
login_manager.login_view = "login"        # If a page requires login, redirect here

# USER LOADER FUNCTION
# Flask-Login uses this function to reload a user from their ID stored in the session.
@login_manager.user_loader
def load_user(user_id):
    # Convert the user_id (string) back into an integer and return the User object
    return User.query.get(int(user_id))

# ROUTES
@app.route("/")                           # The root URL of the website
def home():
    # This renders an HTML template called 'home.html'
    return render_template("home.html")

# MAIN ENTRY POINT
if __name__ == "__main__":
    # The following block only runs if we execute this file directly
    with app.app_context():               # Creates an application context (required for db ops)
        db.create_all()                   # Create database tables if they don’t exist
    app.run(debug=True)                   # Start the development server (debug = auto-reload)

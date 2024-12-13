from flask import Flask
from config import Config  # Ensure you have a config file for settings like SECRET_KEY

def create_app(config_class=Config):
    """
    Application factory function to create and configure the Flask app.
    """
    # Initialize the Flask app with custom template and static folder paths
    app = Flask(__name__,
                template_folder='../templates',  # Adjust if templates are not in the default location
                static_folder='../static')      # Adjust if static files are not in the default location

    # Load configuration from the config class
    app.config.from_object(config_class)

    # Import and register blueprints
    from .routes import main_bp  # Import the blueprint from routes.py
    app.register_blueprint(main_bp)

    return app


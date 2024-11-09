from flask import Flask
from config import Config


# This is a basic sceleton for the app. Just to run the server and see if it starts correctly.

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here

    # Basic root for test
    @app.route('/')
    def test():
        return "Test aplicacion biblioteca"

    return app
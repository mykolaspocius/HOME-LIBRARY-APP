from flask import Flask
from config import Config


# This is a basic sceleton for the app. Just to run the server and see if it starts correctly.

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.books import bp as books_bp
    app.register_blueprint(books_bp,url_prefix='/books')

    return app
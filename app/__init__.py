from flask import Flask
from config import Config
from app.extentions import sql_db,migrate,login_manager
from app.db_models.user import Usuario


# This is a basic sceleton for the app. Just to run the server and see if it starts correctly.

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    sql_db.init_app(app)
    migrate.init_app(app,sql_db)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.books import bp as books_bp
    app.register_blueprint(books_bp,url_prefix='/books')

    # Register some cli commands
    from app.register_commands import register
    register(app)

    return app
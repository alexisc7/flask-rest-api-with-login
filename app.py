import os
from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from routes.user_routes import user_bp
from routes.auth_routes import auth_bp
from db import init_db, close_connection
from config import DevelopmentConfig, ProductionConfig

load_dotenv()

def create_app():
    app = Flask(__name__)
    # Carga configuración
    env = os.environ.get("FLASK_ENV", "development")
    if env == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)
        init_db()  # Inicializa la BD solo en desarrollo

    # Inicializa extensiones
    JWTManager(app)

    # Registro de teardown y blueprints
    app.teardown_appcontext(close_connection)
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app

# Exponer instancia para WSGI
app = create_app()

if __name__ == "__main__":
    app.run()
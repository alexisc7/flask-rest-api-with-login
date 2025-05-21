import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    # Clave para firmar sesiones y cookies
    SECRET_KEY = os.environ.get("SECRET_KEY", "mi_fallback_secret_key")
    # Ruta absoluta o relativa a la base de datos SQLite
    DATABASE_URL = os.environ.get("DATABASE_URL", os.path.join(basedir, "usersdb.db"))
    # JWT
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "mi_fallback_jwt_secret")
    JWT_ACCESS_TOKEN_EXPIRES = int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRES", 3600))  # segundos


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = "development"


class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = "production"
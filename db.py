# Conexión y cierre de base de datos
import os
import sqlite3
from flask import g
from config import BaseConfig

SCHEMA_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "database.sql")

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(BaseConfig.DATABASE_URL)
        g.db.row_factory = sqlite3.Row
        g.cursor = g.db.cursor()
    return g.db, g.cursor


def close_connection(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """
    Si la base de datos no existe, la crea ejecutando el script SQL.
    Sólo debe llamarse en desarrollo.
    """
    db_path = BaseConfig.DATABASE_URL
    if not os.path.exists(db_path):
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            schema_sql = f.read()
        conn = sqlite3.connect(db_path)
        conn.executescript(schema_sql)
        conn.commit()
        conn.close()
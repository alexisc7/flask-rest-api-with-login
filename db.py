# Conexión y cierre de base de datos
    
import sqlite3
from flask import g

DATABASE = "usersdb.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
        g.cursor = g.db.cursor()
    return g.db, g.cursor

def close_connection(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()
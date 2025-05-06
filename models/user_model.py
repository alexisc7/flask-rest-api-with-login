# Operaciones con la base de datos (CRUD)

from db import get_db
from utils.helpers import serialize_row
from werkzeug.security import generate_password_hash

def get_all_users():
    _, cursor = get_db()
    cursor.execute("SELECT * FROM users")
    return [serialize_row(row) for row in cursor.fetchall()]


def get_user_by_id(user_id):
    _, cursor = get_db()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    return serialize_row(row) if row else None


def create_user(data):
    db, cursor = get_db()
    hashed_password = generate_password_hash(data["password"])
    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?) RETURNING *",
        (data["username"], data["email"], hashed_password)
    )
    new_user = cursor.fetchone()
    db.commit()
    return serialize_row(new_user)


def update_user(user_id, data):
    db, cursor = get_db()
    hashed_password = generate_password_hash(data["password"])
    cursor.execute(
        "UPDATE users SET username = ?, email = ?, password = ? WHERE id = ? RETURNING *",
        (data["username"], data["email"], hashed_password, user_id)
    )
    updated = cursor.fetchone()
    db.commit()
    return serialize_row(updated) if updated else None


def delete_user(user_id):
    db, cursor = get_db()
    cursor.execute("DELETE FROM users WHERE id = ? RETURNING *", (user_id,))
    deleted = cursor.fetchone()
    db.commit()
    return serialize_row(deleted) if deleted else None
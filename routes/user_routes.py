from flask import Blueprint, request, jsonify
from models.user_model import (
    get_all_users,
    get_user_by_id,
    create_user as model_create_user,
    update_user as model_update_user,
    delete_user as model_delete_user,
)

user_bp = Blueprint("user_bp", __name__, url_prefix="/api/users")

@user_bp.get("/")
def get_users():
    users = get_all_users()
    return jsonify(users), 200


@user_bp.get("/<int:id>")
def get_user(id):
    user = get_user_by_id(id)
    if user is None:
        return jsonify({"message": "Usuario no encontrado"}), 404
    return jsonify(user), 200

@user_bp.post("/")
def create_user():
    data = request.get_json()
    new_user = model_create_user(data)
    return jsonify(new_user), 201

@user_bp.put("/<int:id>")
def update_user(id):
    data = request.get_json()
    updated = model_update_user(id, data)
    if updated is None:
        return jsonify({"message": "Usuario no encontrado"}), 404
    return jsonify({"message": "Usuario actualizado con éxito", "usuario_actualizado": updated}), 200

@user_bp.delete("/<int:id>")
def delete_user(id):
    deleted = model_delete_user(id)
    if deleted is None:
        return jsonify({"message": "Usuario no encontrado"}), 404
    return jsonify({"message": "Usuario eliminado con éxito", "usuario_eliminado": deleted}), 200
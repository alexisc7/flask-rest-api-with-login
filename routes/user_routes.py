from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from models.user_model import (
    get_all_users,
    get_user_by_id,
    create_user as model_create_user,
    update_user as model_update_user,
    delete_user as model_delete_user,
)
from schemas.user_schema import UserCreate, UserUpdate

user_bp = Blueprint("user_bp", __name__, url_prefix="/api/users")

def validation_error_response(errors):
    return jsonify({"message": "Error de validación", "errors": errors}), 422


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
    payload = request.get_json(silent=True)
    if not payload:
        return jsonify({"message": "JSON inválido"}), 400

    try:
        data = UserCreate(**payload)
    except ValidationError as e:
        return validation_error_response(e.errors())

    new_user = model_create_user(data.dict())
    new_user.pop("password", None)
    return jsonify(new_user), 201


@user_bp.put("/<int:id>")
def update_user(id):
    payload = request.get_json(silent=True)
    if not payload:
        return jsonify({"message": "JSON inválido"}), 400

    try:
        data = UserUpdate(**payload)
    except ValidationError as e:
        return validation_error_response(e.errors())

    # Asegurarse de que al menos un campo venga
    if not data.dict(exclude_unset=True):
        return jsonify({"message": "Proporcioná al menos un campo a actualizar"}), 400

    updated = model_update_user(id, data.dict(exclude_unset=True))
    if updated is None:
        return jsonify({"message": "Usuario no encontrado"}), 404

    updated.pop("password", None)
    return jsonify({"message": "Usuario actualizado con éxito", "usuario_actualizado": updated}), 200


@user_bp.delete("/<int:id>")
def delete_user(id):
    deleted = model_delete_user(id)
    if deleted is None:
        return jsonify({"message": "Usuario no encontrado"}), 404
    deleted.pop("password", None)
    return jsonify({"message": "Usuario eliminado con éxito", "usuario_eliminado": deleted}), 200
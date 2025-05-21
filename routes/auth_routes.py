from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from models.user_model import get_user_by_email

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True)
    if not data or "email" not in data or "password" not in data:
        return jsonify({"message": "Email y password son requeridos"}), 400

    user = get_user_by_email(data["email"])
    if not user or not check_password_hash(user["password"], data["password"]):
        return jsonify({"message": "Credenciales inválidas"}), 401

    # Generar token
    access_token = create_access_token(identity={"id": user["id"], "email": user["email"]})
    return jsonify({"access_token": access_token}), 200
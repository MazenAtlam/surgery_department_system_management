from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.user import User
from app.services.auth_service import login_user, register_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    result = register_user(data)
    return jsonify(result), 201 if result["success"] else 400


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    result = login_user(data)
    return jsonify(result), 200 if result["success"] else 401


@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return (
        jsonify(
            {
                "message": "This is a protected route",
                "user": {"id": user.id, "username": user.username, "email": user.email},
            }
        ),
        200,
    )

from flask import Blueprint, jsonify

from app.services.user_service import get_user_data_by_id

user_bp = Blueprint("user", __name__)


@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user_data = get_user_data_by_id(user_id)
    if user_data:
        return jsonify(user_data), 200
    return jsonify({"error": "User not found"}), 404

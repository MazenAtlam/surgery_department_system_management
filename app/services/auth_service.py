from datetime import datetime

from flask_jwt_extended import create_access_token, get_jwt, jwt_required
from werkzeug.security import check_password_hash

import app.models as m
from app import db


def register_user(user_data):
    # Check if user exists
    if m.User.query.filter_by(email=user_data["email"]).first():
        return {"success": False, "message": "Email already registered"}

    role_id = m.Role.query.filter_by(name="patient").first().id

    # Add picture
    pic_id = m.UploadedFile.query.filter_by(file_name="default.png").first().id

    # Convert string to date object
    dob_str = user_data["date_of_birth"]  # This comes from your input data
    date_of_birth = datetime.strptime(dob_str, "%d-%m-%Y").date()

    gender: str = user_data["gender"][0].upper()  # 'M' or 'F'

    # Create new user
    new_user = m.User(
        email=user_data["email"],
        password=user_data["password"],
        username=user_data["username"],
        ssn=user_data["ssn"],
        gender=gender,
        date_of_birth=date_of_birth,
        role_id=role_id,
        pic_id=pic_id,
    )

    db.session.add(new_user)
    db.session.commit()

    # Create token for the new user
    access_token = create_access_token(identity=new_user.id)

    return {
        "success": True,
        "message": "User registered successfully",
        "access_token": access_token,
    }


def login_user(login_data):
    user = m.User.query.filter_by(email=login_data["email"]).first()

    if not user or not check_password_hash(user.password_hash, login_data["password"]):
        return {"success": False, "message": "Invalid email or password"}

    # Create token
    access_token = create_access_token(identity=user.id)

    return {
        "success": True,
        "message": "Login successful",
        "access_token": access_token,
        "user": {"id": user.id, "username": user.username, "email": user.email},
    }


# Add to your auth_service.py
def logout_user():
    jti = get_jwt()["jti"]  # Get the JWT's unique identifier
    # In production, you would store this in a token blacklist database
    return {"success": True, "message": "Successfully logged out"}

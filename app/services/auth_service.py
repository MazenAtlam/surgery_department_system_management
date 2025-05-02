from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.models.user import User


def register_user(user_data):
    # Check if user exists
    if User.query.filter_by(email=user_data["email"]).first():
        return {"success": False, "message": "Email already registered"}

    from app.models import Role

    role_id = Role.query.filter_by(name="Patient").first().id

    from datetime import datetime

    # Convert string to date object
    dob_str = user_data["dob"]  # This comes from your input data
    dob = datetime.strptime(dob_str, "%d-%m-%Y").date()

    # Create new user
    new_user = User(
        email=user_data["email"],
        password=user_data["password"],
        name=user_data["name"],
        ssn=user_data["ssn"],
        gender=user_data["gender"],
        dob=dob,
        role_id=role_id,
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
    user = User.query.filter_by(email=login_data["email"]).first()

    if not user or not check_password_hash(user.password_hash, login_data["password"]):
        return {"success": False, "message": "Invalid email or password"}

    # Create token
    access_token = create_access_token(identity=user.id)

    return {
        "success": True,
        "message": "Login successful",
        "access_token": access_token,
        "user": {"id": user.id, "name": user.name, "email": user.email},
    }

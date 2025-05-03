import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = (
        os.environ.get("SECRET_KEY") or "m6Mqvd1RWQE6v3WdYnHUHfBNXHxOxLoSWhj-PW8Z0e"
    )

    USERNAME = os.environ.get("USERNAME") or "postgres"
    PASSWORD = os.environ.get("PASSWORD") or "npg_Io23FZrkzcMt"
    HOST = (
        os.environ.get("HOST")
        or "ep-misty-poetry-a21sokc7-pooler.eu-central-1.aws.neon.tech"
    )
    PORT = os.environ.get("PORT") or "5432"
    DBNAME = os.environ.get("DATABASE_NAME") or "Surgerydb"

    SQLALCHEMY_DATABASE_URI = (
        "postgresql://"
        + USERNAME
        + ":"
        + PASSWORD
        + "@"
        + HOST
        + "/"
        + DBNAME
        + "?sslmode=require"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = (
        os.environ.get("JWT_SECRET_KEY")
        or "ereteyubcgdhfjmazensherifahmedmostafaanas##$$%^djyfgjidigp0-ititjgj"
    )
    jwt_access_token_expires = float(
        os.environ.get("JWT_ACCESS_TOKEN_EXPIRES") or "3600"
    )
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=jwt_access_token_expires)

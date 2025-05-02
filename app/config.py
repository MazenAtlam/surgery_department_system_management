import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")

    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")
    host = os.environ.get("HOST")
    dbname = os.environ.get("DATABASE_NAME")

    SQLALCHEMY_DATABASE_URI = (
        "postgresql://"
        + username
        + ":"
        + password
        + "@"
        + host
        + "/"
        + dbname
        + "?sslmode=require"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = os.environ.get("JWT_ACCESS_TOKEN_EXPIRES")

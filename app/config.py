import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = (
        os.environ.get("SECRET_KEY") or "m6Mqvd1RWQE6v3WdYnHUHfBNXHxOxLoSWhj-PW8Z0eQ"
    )
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "data.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = (
        os.environ.get("JWT_SECRET_KEY")
        or "ereteyubcgdhfjmazensherifahmedmostafa##$$%^djyfgjidigp0-ititjgj"
    )
    JWT_ACCESS_TOKEN_EXPIRES = 3600

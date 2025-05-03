import psycopg2
from psycopg2 import OperationalError
from app.config import Config


def get_db_connection():
    """
    Establishes and returns a connection to a PostgreSQL database on Neon.

    Returns:
        A psycopg2 connection object if successful, None otherwise.
    """
    # Replace these with your actual Neon database credentials
    connection_params = {
        'host': Config.HOST,
        'database': Config.DBNAME,
        'user': Config.USERNAME,
        'password': Config.PASSWORD,
        'port': Config.PORT,
        'sslmode': 'require'  # Neon requires SSL connections
    }

    try:
        connection = psycopg2.connect(**connection_params)
        print("Successfully connected to the Neon PostgreSQL database")
        return connection
    except OperationalError as e:
        print(f"Error connecting to PostgreSQL database: {e}")
        return None
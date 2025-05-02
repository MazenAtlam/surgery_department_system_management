import sqlite3
from typing import Dict, Optional

from flask import current_app

from app.config import Config


def get_user_data_by_id(user_id: int) -> Optional[Dict]:
    """
    Fetch detailed user data by ID using raw SQL.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict: User data with medical history and photo URL if found, else None.
    """
    conn = None
    try:

        conn = sqlite3.connect(Config.SQLALCHEMY_DATABASE_URI)
        conn.row_factory = sqlite3.Row  # Return rows as dictionaries

        query = """
                SELECT u.user_id, \
                       u.name, \
                       DATE_PART('year', AGE(CURRENT_DATE, u.dob)) AS age, \
                       u.phone_num, \
                       u.gender, \
                       u.email, \
                       pf.file_url                                 AS photo_url, \
                       mh.history_id, \
                       mh.family_history, \
                       mh.disease_name
                FROM "user" AS u
                         JOIN patient AS p ON p.user_id = u.user_id
                         LEFT JOIN (SELECT DISTINCT \
                                    ON (patient_id) \
                                        patient_id, \
                                        file_url \
                                    FROM files \
                                    WHERE file_type = 'photo' \
                                    ORDER BY patient_id, upload_time DESC) AS pf ON pf.patient_id = p.patient_id
                         LEFT JOIN medical_history AS mh ON mh.patient_id = p.patient_id
                WHERE u.user_id = ? \
                """

        cursor = conn.cursor()
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()

        return dict(result) if result else None

    except sqlite3.Error as e:
        current_app.logger.error(f"Database error in get_user_data_by_id: {e}")
        return None
    finally:
        if conn:
            conn.close()


# from flask import current_app
# import sqlite3
#
#
# def get_user_data_by_id(id):
#     """
#     Retrieve a user by email using raw SQL commands
#
#     Args:
#         email (str): The email address to search for
#
#     Returns:
#         dict: User data if found, None otherwise
#     """
#     conn = None
#     try:
#         # Get the database path from Flask config
#         db_path = current_app.config.get('DATABASE_URI', 'data.sqlite')
#
#         # Connect to the SQLite database
#         conn = sqlite3.connect(db_path)
#         conn.row_factory = sqlite3.Row  # To get results as dictionaries
#
#         # Create a cursor object
#         cursor = conn.cursor()
#
#         # Execute the SQL query with parameterized input to prevent SQL injection
#         cursor.execute("SELECT * FROM users WHERE email = ?", (id,))
#
#         # Fetch the result
#         user = cursor.fetchone()
#
#         # Return as dict if found
#         return dict(user) if user else None
#
#     except sqlite3.Error as e:
#         current_app.logger.error(f"Database error: {e}")
#         return None
#     finally:
#         if conn:
#             conn.close()

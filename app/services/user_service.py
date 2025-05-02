import sqlite3
from typing import Dict, List, Optional

from flask import current_app

from app.config import Config


def get_user_data_by_id(user_id: str) -> Optional[Dict]:
    """
    Fetch comprehensive user data by ID including phone numbers and profile picture.

    Args:
        user_id (str): The ID of the user to retrieve (e.g., 'user1')

    Returns:
        dict: User data with phone numbers (as list) and picture URL if found, else None.
    """
    conn = None
    try:
        conn = sqlite3.connect(Config.SQLALCHEMY_DATABASE_URI)
        conn.row_factory = sqlite3.Row

        query = """
                SELECT u.name, \
                       u.email, \
                       CAST((julianday('now') - julianday(u.dob)) / 365 AS INTEGER)                                       AS age, \
                       u.ssn, \
                       u.gender, \
                       GROUP_CONCAT(pn.number)                                                                            AS phone_numbers, \
                       COALESCE(uf.file_url, \
                                (SELECT file_url FROM uploaded_files WHERE file_name = 'default.png' LIMIT 1)
            ) AS picture_url
                FROM users u \
                         LEFT JOIN phone_numbers pn ON u.id = pn.user_id \
                         LEFT JOIN uploaded_files uf ON u.pic_id = uf.id
                WHERE u.id = ?
                GROUP BY u.id, u.name, u.email, u.dob, u.ssn, u.gender, uf.file_url \
                """

        cursor = conn.cursor()
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()

        if result:
            # Convert SQLite result to dict and process phone numbers
            user_data = dict(result)
            if user_data["phone_numbers"]:
                user_data["phone_numbers"]: List[str] = user_data[
                    "phone_numbers"
                ].split(",")
            else:
                user_data["phone_numbers"]: List[str] = []
            return user_data
        return None

    except sqlite3.Error as e:
        current_app.logger.error(f"Database error in get_user_data_by_id: {e}")
        return None
    finally:
        if conn:
            conn.close()

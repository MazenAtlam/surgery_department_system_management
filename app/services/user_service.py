from typing import Dict, List, Optional

import psycopg2
from flask import current_app

from app.utils.db_connect import get_db_connection


def get_user_data_by_id(user_id: str) -> Optional[Dict]:
    """
    Fetch comprehensive user data by ID including phone numbers and profile picture.

    Args:
        user_id (str): The ID of the user to retrieve (UUID format)

    Returns:
        dict: User data with phone numbers (as list) and picture URL if found, else None.
    """
    conn = get_db_connection()
    if not conn:
        return None

    try:
        query = """
                SELECT 
                    u.name,
                    u.email,
                    EXTRACT(YEAR FROM age(current_date, u.dob))::integer AS age,
                    u.ssn,
                    u.gender,
                    p.blood_type,
                    STRING_AGG(pn.number, ', ') AS phone_numbers,
                    COALESCE(
                        uf.file_url,
                        (SELECT file_url FROM uploaded_files WHERE file_name = 'default.png' LIMIT 1)
                    ) AS picture_url
                FROM users u
                LEFT JOIN phone_numbers pn ON u.id = pn.user_id
                LEFT JOIN uploaded_files uf ON u.pic_id = uf.id
                LEFT JOIN patients p ON u.id = p.user_id
                WHERE u.id = %s
                GROUP BY 
                    u.id, u.name, u.email, u.dob, 
                    u.ssn, u.gender, p.blood_type, uf.file_url
                """

        cursor = conn.cursor()
        cursor.execute(query, (user_id,))
        columns = [desc[0] for desc in cursor.description]  # Get column names
        result = cursor.fetchone()

        if result:
            # Convert to dict using column names
            user_data = dict(zip(columns, result))

            # Process phone numbers
            user_data["phone_numbers"] = (
                user_data["phone_numbers"].split(", ")
                if user_data["phone_numbers"]
                else []
            )
            return user_data
        return None

    except psycopg2.Error as e:
        current_app.logger.error(f"Database error in get_user_data_by_id: {e}")
        return None
    finally:
        conn.close()

import sqlite3


DATABASE_NAME = "edutwin.db"


def get_connection():

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    return connection


def create_tables():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            education TEXT,
            skills TEXT,
            courses TEXT,
            projects TEXT,
            interests TEXT,
            career_goal TEXT
        )
        """
    )

    connection.commit()

    connection.close()


def save_profile(profile):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO profiles (
            name,
            education,
            skills,
            courses,
            projects,
            interests,
            career_goal
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            profile["name"],
            profile["education"],
            profile["skills"],
            profile["courses"],
            profile["projects"],
            profile["interests"],
            profile["career_goal"]
        )
    )

    connection.commit()

    connection.close()


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

import sqlite3

DATABASE_NAME = "students.db"

# Think of it as: open database → prepare SQL → run SQL → save → close.

def get_connection():
    """
    Open a connection to SQLite.

    sqlite3 is included with Python, so no separate database
    server such as MySQL or PostgreSQL is required.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    """Create the students table if it does not already exist."""
    connection = get_connection()
    
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL,
            cgpa REAL NOT NULL,
            course TEXT NOT NULL,
            skills TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()

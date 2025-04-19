import psycopg2
import os

def get_db_connection():
    try:
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise ValueError("DATABASE_URL not set")
        conn = psycopg2.connect(database_url)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def close_db_connection(conn):
    if conn:
        conn.close()
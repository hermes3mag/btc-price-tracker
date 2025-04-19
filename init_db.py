from db_utils import get_db_connection, close_db_connection
import psycopg2

def create_table():
    # Connect to the database
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to the database.")
        return
    try:
        cur = conn.cursor()

        # Define the SQL to create a table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS btc_prices (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP NOT NULL,
            price_usd NUMERIC(12, 2) NOT NULL
        );
        """

        # Execute the query
        cur.execute(create_table_query)
        conn.commit()
        print("Table created successfully!")
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        cur.close()
        close_db_connection(conn)

if __name__ == "__main__":
    create_table()
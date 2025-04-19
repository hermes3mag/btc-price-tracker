import psycopg2

def create_table():
    # Connect to the database
    conn = psycopg2.connect(
        host="db",
        database="bitcoin_db",
        user="bitcoin_user",
        password="bitcoin_password"
    )
    cur = conn.cursor()

    # Define the SQL to create a table
    create_table_query = """
    CREATE TABLE btc_prices (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP NOT NULL,
            price_usd NUMERIC(12, 2) NOT NULL
        );
    """

    # Execute the query
    cur.execute(create_table_query)
    conn.commit()

    # Close the connection
    cur.close()
    conn.close()
    print("Table created successfully!")

if __name__ == "__main__":
    create_table()
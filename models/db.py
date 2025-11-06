import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Connect to the database
def cursor():
    try:
        connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )
        print("Connection successful!")

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # # Example query
        # cursor.execute("SELECT NOW();")
        # result = cursor.fetchone()
        # print("Current Time:", result)

        # Close the cursor and connection
        # cursor.close()
        # connection.close()
        # print("Connection closed.")

    except Exception as e:
        cursor = None
        print(f"Failed to connect: {e}")
    return cursor

if __name__ == "__main__":
    c = cursor()
    c.execute("""SELECT json_agg(row_to_json(p))
FROM (
    SELECT * FROM medicines
) AS p;
""")
    posts = c.fetchall()
    print(posts[0][0])
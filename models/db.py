import psycopg2
from dotenv import load_dotenv
import os
from psycopg2.extras import RealDictCursor

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
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        # # Example query
        # cursor.execute("SELECT NOW();")
        # result = cursor.fetchone()
        # print("Current Time:", result)

        # Close the cursor and connection
        # cursor.close()
        # connection.close()
        # print("Connection closed.")
        return cursor, connection

    except Exception as e:
        print(f"Failed to connect: {e}")
        return None, None

if __name__ == "__main__":
    cursor, conn = cursor()
#     c.execute("""SELECT json_agg(row_to_json(p))
# FROM (
#     SELECT * FROM medicines
# ) AS p;
# """)
#     posts = c.fetchall()
#     print(posts[0]['json_agg'])
#     email = "example@email.com"
#     cursor.execute("""
#                 SELECT * FROM cart
#                 WHERE "user" = (SELECT id FROM users WHERE email = %s)
#             """, (email,))
#     products = cursor.fetchall()
#     for med in products:
#         med_name = med['medicine']
#         cursor.execute("""SELECT * FROM medicines WHERE name = %s""", (med_name,))
#         med_data = cursor.fetchone()
#         med["price"] = med_data["price"]
#         med["sale"] = med_data["sale"]
#         med["image"] = med_data["image"]
#         med["stock"] = med_data["stock"]
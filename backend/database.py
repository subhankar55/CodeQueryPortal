import mysql.connector
from mysql.connector import Error

# TODO: Replace with your actual database credentials
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Maiti@1230',
    'database': 'CodeQueryPortal'
}

def get_db_connection():
    """Establishes a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def setup_database():
    """Creates the database and the users table if they don't exist."""
    try:
        # Connect without specifying a database to create it first
        conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        conn.database = DB_CONFIG['database']
        
        users_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            name VARCHAR(255),
            picture VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor.execute(users_table_query)
        
        conn.commit()
        cursor.close()
        conn.close()
        print("Database and users table are set up.")
    except Error as e:
        print(f"Error during database setup: {e}")


def save_user(user_data):
    """Saves or updates user data in the database."""
    conn = get_db_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor(dictionary=True)

        # Check if user exists
        cursor.execute("SELECT * FROM users WHERE email = %s", (user_data['email'],))
        user = cursor.fetchone()

        if user:
            # Update user if exists
            update_query = """
            UPDATE users SET name = %s, picture = %s 
            WHERE email = %s
            """
            cursor.execute(update_query, (user_data['name'], user_data['picture'], user_data['email']))
        else:
            # Insert new user
            insert_query = """
            INSERT INTO users (email, name, picture) 
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (user_data['email'], user_data['name'], user_data['picture']))

        conn.commit()
        cursor.close()
        conn.close()
    except Error as e:
        print(f"Error saving user: {e}")


import sqlite3
import os

DATABASE_PATH = 'single_database.db'

def init_database():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Drop the existing tables
    cursor.execute('DROP TABLE IF EXISTS user_data')
    cursor.execute('DROP TABLE IF EXISTS order_data')

    # Create the 'user_data' table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # Create the 'order_data' table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_data (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            order_info TEXT NOT NULL,
            color TEXT NOT NULL,
            size TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def store_user_data(name, email):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO user_data (name, email)
        VALUES (?, ?)
    ''', (name, email))

    conn.commit()
    conn.close()

def store_order_data(name, email, order, color, size):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Log extracted form data for debugging
    print(f"Storing data: name={name}, email={email}, order={order}, color={color}, size={size}")

    # Construct and log the SQL statement
    sql = f"""
        INSERT INTO order_data (name, email, order_info, color, size)
        VALUES (?, ?, ?, ?, ?)
    """
    print(sql)
    
    # Execute the SQL statement with the provided values
    cursor.execute(sql, (name, email, order, color, size))

    conn.commit()
    conn.close()

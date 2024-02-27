import sqlite3
import os

DATABASE_PATH = 'single_database.db'

def init_database():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Check if the tables already exist
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user_data'")
    user_data_table_exists = cursor.fetchone()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='order_data'")
    order_data_table_exists = cursor.fetchone()

    # Create the 'user_data' table if it doesn't exist
    if not user_data_table_exists:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_data (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    # Create the 'order_data' table if it doesn't exist
    if not order_data_table_exists:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS order_data (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                order_info TEXT NOT NULL,
                color TEXT NOT NULL,
                size TEXT NOT NULL,
                address TEXT NOT NULL,
                state TEXT NOT NULL,
                city TEXT NOT NULL,
                zip TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
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

def store_order_data(name, email, order_info, color, size, address, state, city, zip):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Construct and log the SQL statement
    sql = f"""
    INSERT INTO order_data (name, email, order_info, color, size, address, state, city, zip) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    
    
    # Execute the SQL statement with the provided values
    cursor.execute(sql, (name, email, order_info, color, size, address, state, city, zip))

    conn.commit()
    conn.close()

def fetch_user_data():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM user_data')
    user_data = cursor.fetchall()

    conn.close()
    return user_data

def fetch_order_data():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM order_data')
    order_data = cursor.fetchall()

    conn.close()
    return order_data
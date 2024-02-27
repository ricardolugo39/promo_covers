from flask import render_template, current_app, Blueprint, request, redirect, g, session, url_for
from logic.database import fetch_user_data, fetch_order_data, init_database
from logic.send_email import send_shipping_email
import sqlite3
import os

admin_bp = Blueprint('admin', __name__)

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'Hasten123456$'

@admin_bp.route('/admin', methods=['GET', 'POST'])
def display_admin():

    # Check if the user is already authenticated
    if not session.get('logged_in'):
        # If not authenticated, check if the login form is submitted
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            # Check the entered credentials against hardcoded values (demo purposes)
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                # Set the user as authenticated
                session['logged_in'] = True
                return redirect(url_for('admin.display_admin'))  # Redirect to admin page upon successful login
            else:
                return render_template('login.html', login_error='Invalid credentials')
         # If not authenticated and no login form submitted, render the login page
        return render_template('login.html')



    user_data = fetch_user_data()
    order_data = fetch_order_data()

    DATABASE_PATH = 'single_database.db'

    customer_info = None  # Initialize customer_info outside the if block

    if request.method == 'POST':
        order = request.form.get('orderInfo')
        tracking = request.form.get('trackingNumber')
        
        customer_info = fetch_customer_info(order)
        g.db.close()
        send_shipping_email(customer_info, order, tracking)

    return render_template('admin.html', template_folder=current_app.template_folder, user_data=user_data, order_data=order_data, customer_info=customer_info)


def fetch_customer_info(order_info):
    # Use Flask's g object for handling database connections
    DATABASE_PATH = 'single_database.db'

    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE_PATH)
    conn = g.db
    cursor = conn.cursor()

    cursor.execute('''
        SELECT size, color, name, address, city, state, zip, email
        FROM order_data
        WHERE order_info = ?
    ''', (order_info,))

    customer_info = cursor.fetchone()

    return customer_info
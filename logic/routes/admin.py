from flask import render_template, current_app, Blueprint, request, redirect, g
from logic.database import fetch_user_data, fetch_order_data, init_database
from logic.send_email import send_shipping_email
import sqlite3
import os

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin', methods=['GET', 'POST'])
def display_admin():
    user_data = fetch_user_data()
    order_data = fetch_order_data()

    DATABASE_PATH = 'single_database.db'

    customer_info = None  # Initialize customer_info outside the if block

    if request.method == 'POST':
        order = request.form.get('orderInfo')
        tracking = request.form.get('trackingNumber')
        # email = request.form.get('email')

        # Example of using fetch_customer_info
        customer_info = fetch_customer_info(order)
        # Close the connection at the end of the request
        g.db.close()

        # send email
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
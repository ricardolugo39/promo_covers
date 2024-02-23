from flask import render_template, current_app, Blueprint, request, redirect
from logic.database import fetch_user_data, fetch_order_data
from logic.send_email import send_shipping_email

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin', methods=['GET', 'POST'])
def display_admin():
    user_data = fetch_user_data()
    order_data = fetch_order_data()

    if request.method == 'POST':
        # Handle form submission
        order = request.form.get('orderInfo')
        tracking = request.form.get('trackingNumber')
        email = request.form.get('email')

        # send email
        send_shipping_email(email, order, tracking)

    return render_template ('admin.html', template_folder=current_app.template_folder, user_data = user_data, order_data = order_data)
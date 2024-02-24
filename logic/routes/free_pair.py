from flask import Blueprint, render_template, request, current_app, redirect, url_for
from logic.database import store_order_data
from logic.send_email import send_confirmation_email

free_pair_bp = Blueprint('free_pair', __name__)

@free_pair_bp.route('/free_pair', methods=['GET', 'POST'])
def display_free_pair():
    current_app.logger.info('Request Content: %s', request.get_data())

    # name_param = request.args.get('name', '')
    # email_param = request.args.get('email', '')

    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        order_info = request.form.get('order_info')
        color = request.form.get('color')
        size = request.form.get('size')
        address = request.form.get('address')
        state = request.form.get('state')
        city = request.form.get('city')
        zip = request.form.get('zip')

        # Store the form data in the database
        store_order_data(name, email, order_info, color, size, address, state, city, zip)

        # send confirmation email
        send_confirmation_email(name, email, order_info, color, size, address, state, city, zip)

        # Redirect to the complete order page after processing the form
        return redirect(url_for('complete_order.display_complete_order'))


    # Render the template for GET requests
    return render_template('free_pair.html', template_folder=current_app.template_folder)

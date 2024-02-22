from flask import Blueprint, render_template, request, current_app, redirect, url_for
from logic.database import store_order_data
from logic.send_email import send_confirmation_email

free_pair_bp = Blueprint('free_pair', __name__)

@free_pair_bp.route('/free_pair', methods=['GET', 'POST'])
def display_free_pair():
    current_app.logger.info('Request Content: %s', request.get_data())

    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('template-contactform-name')
        email = request.form.get('template-contactform-email')
        order = request.form.get('template-contactform-order')
        color = request.form.get('template-contactform-color-select')
        size = request.form.get('template-contactform-size-select')

        # Store the form data in the database
        store_order_data(name, email, order, color, size)

        # send confirmation email
        send_confirmation_email(name, email, order, color, size)

        # Redirect to the complete order page after processing the form
        return redirect(url_for('complete_order.display_complete_order'))


    # Render the template for GET requests
    return render_template('free_pair.html')

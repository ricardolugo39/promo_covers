from flask import render_template, redirect, url_for, request, current_app
from logic import bp
from logic.database import store_user_data
from logic.send_email import send_interest_email

@bp.route('/', methods=['GET', 'POST'])
def landing_page():
    # Implementation for landing page and form submission
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('template-contactform-name')
        email = request.form.get('template-contactform-email')

        # Server-side validation
        if not name or not email:
            error_message = "Please fill out all required fields."
            return render_template('index.html', error_message=error_message)

        # Store the form data in the database
        store_user_data(name, email)

        # send interest email
        send_interest_email(name, email)

        # Redirect to the Amazon link after form submission
        amazon_link = 'https://www.amazon.com/dp/B0CHMVWB1P'
        return redirect(amazon_link)


    # Render the HTML index template
    return render_template('index.html', template_folder=current_app.template_folder)

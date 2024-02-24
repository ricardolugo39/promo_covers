from flask import render_template, redirect, url_for, request, current_app, render_template_string, Blueprint
from logic import bp
from logic.database import store_user_data
from logic.send_email import send_interest_email

@bp.route('/', methods=['GET', 'POST'])
def landing_page():
    # Implementation for landing page and form submission
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')

        # Server-side validation
        if not name or not email:
            error_message = "Please fill out all required fields."
            return render_template('index.html', error_message=error_message)

        # Store the form data in the database
        store_user_data(name, email)

        # send interest email
        send_interest_email(name, email)

        # Render a temporary page with a message
        message = "Thank you for your interest in our Cleat Covers. You will be redirected to our Amazon Store shortly."
        return render_template('temp_page.html', message=message)

        
        
        # Redirect to the Amazon link after form submission
        #amazon_link = 'https://www.amazon.com/dp/B0CHMVWB1P'
        #return redirect(amazon_link)


    # Render the HTML index template
    return render_template('index.html', template_folder=current_app.template_folder)


temp_bp = Blueprint('temp_page', __name__)

@temp_bp.route('/temporary_page')
def temporary_page():
    return render_template('temp_page.html')




@bp.route('/redirect_to_amazon')
def redirect_to_amazon():
    # Add a 5-second delay using JavaScript for client-side redirection
    js_redirect = """
    <script>
        setTimeout(function() {
            window.location.href = "{{ amazon_link }}";
        }, 200);  // 1-second delay
    </script>
    """
    return render_template_string(js_redirect, amazon_link='https://www.amazon.com/dp/B0CHMVWB1P')

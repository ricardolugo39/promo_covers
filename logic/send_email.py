import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from urllib.parse import urlencode
import os

SMTP_SERVER = 'mail.hasten.shop'
SMTP_PORT = 587
SMTP_USERNAME = 'hello@hasten.shop'
SMTP_PASSWORD = 'Hasten123456$'
SENDER_EMAIL = 'hello@hasten.shop'
RECIPIENT_EMAIL = 'hastensports@outlook.com'

def send_interest_email(name, email):
    subject = 'Has10 Cleat Internal interest email'
    body = f"Name: {name}\nEmail: {email}"

    # Get the path to the 'email_confirmation.html' file in the 'templates' folder
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'email_interest.html')

    with open(template_path, 'r') as file:
        html_content = file.read()

    # Replace placeholders in the HTML content with actual values
    html_content = html_content.replace('{name}', name)
    html_content = html_content.replace('{email}', email)

    # Generate the link with query parameters
    # params = urlencode({'name': name, 'email': email})
    # new_form_link = f'http://127.0.0.1:5000/email_interest?{params}'

    # Include the link in the email content
    # html_content = html_content.replace('{new_form_link}', new_form_link)

    # Generate the link with query parameters
    order_confirmation_link = f'http://127.0.0.1:5000/free_pair?name={name}&email={email}'

    # Include the link in the email content
    html_content = html_content.replace('{order_confirmation_link}', order_confirmation_link)


    # Create the user's email message
    user_subject = 'Customer HAS10 interest email'
    user_message = MIMEMultipart()
    user_message['From'] = SENDER_EMAIL
    user_message['To'] = email
    user_message['Subject'] = user_subject
    user_message.attach(MIMEText(html_content, 'html'))

    # Create the internal's email message
    recipient_subject = 'Has10 Cleat Internal interest email'
    recipient_message = MIMEMultipart()
    recipient_message['From'] = SENDER_EMAIL
    recipient_message['To'] = RECIPIENT_EMAIL
    recipient_message['Subject'] = recipient_subject
    recipient_message.attach(MIMEText(body, 'plain'))


    # Send both emails
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, email, user_message.as_string())
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, recipient_message.as_string())

# Call the function with sample data for testing
#send_interest_email('John Doe', 'ricardolugo39@me.com')
        
def send_confirmation_email(name, email, order, color, size):
    subject = 'Has10 Cleat Order Confirmation'
    body = f"new customer order from {name},\n\n\n\nOrder Details:\nOrder: {order}\nColor: {color}\nSize: {size}"

    # Get the path to the 'email_confirmation.html' file in the 'templates' folder
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'email_confirmation.html')

    with open(template_path, 'r') as file:
        html_content = file.read()

    # Replace placeholders in the HTML content with actual values
    html_content = html_content.replace('{name}', name)
    html_content = html_content.replace('{email}', email)
    html_content = html_content.replace('{order}', order)
    html_content = html_content.replace('{color}', color)
    html_content = html_content.replace('{size}', size)

    # Create customer email message
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = email
    message['Subject'] = subject
    message.attach(MIMEText(html_content, 'html'))
    
    # internal email
    recipient_subject = 'Has10 Cleat Internal interest email'
    recipient_message = MIMEMultipart()
    recipient_message['From'] = SENDER_EMAIL
    recipient_message['To'] = RECIPIENT_EMAIL
    recipient_message['Subject'] = recipient_subject
    recipient_message.attach(MIMEText(body, 'plain'))

    # Send the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, email, message.as_string())
        server.sendmail(SENDER_EMAIL,RECIPIENT_EMAIL,recipient_message.as_string())

# Example usage:
# send_confirmation_email('John Doe', 'ricardolugo39@me.com', 'Cleat', 'Red', '10')
        
def send_shipping_email(email, order, tracking):
    subject = 'Shipping Confirmation'
    body = f"nShipping info for,\n\n\n\nOrder Details:\nOrder: {order}\Tracking: {tracking}"

    # Get the path to the 'email_confirmation.html' file in the 'templates' folder
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'email_shipping.html')

    with open(template_path, 'r') as file:
        html_content = file.read()

    # Replace placeholders in the HTML content with actual values
    # html_content = html_content.replace('{name}', name)
    html_content = html_content.replace('{email}', email)
    html_content = html_content.replace('{order}', order)
    html_content = html_content.replace('{tracking}', tracking)

    # Create customer email message
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = email
    message['Subject'] = subject
    message.attach(MIMEText(html_content, 'html'))
    
    # internal email
    recipient_subject = 'Shipping Internal'
    recipient_message = MIMEMultipart()
    recipient_message['From'] = SENDER_EMAIL
    recipient_message['To'] = RECIPIENT_EMAIL
    recipient_message['Subject'] = recipient_subject
    recipient_message.attach(MIMEText(body, 'plain'))

    # Send the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, email, message.as_string())
        server.sendmail(SENDER_EMAIL,RECIPIENT_EMAIL,recipient_message.as_string())

# Example usage:
# send_interest_email('rick','ricardolugo39@me.com')
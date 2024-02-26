from flask import Blueprint, render_template, request, redirect, url_for, current_app
from logic import bp

email_interest = Blueprint('email_interest', __name__)

@bp.route('/email_interest', methods=['GET', 'POST'])
def display_order_confirmation():
    return render_template('email_shipping.html', template_folder=current_app.template_folder)
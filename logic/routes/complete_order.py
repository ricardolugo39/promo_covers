from flask import render_template, current_app, Blueprint, request, redirect

complete_order_bp = Blueprint('complete_order', __name__)

@complete_order_bp.route('/complete_order', methods=['GET', 'POST'])
def display_complete_order():
    return render_template ('complete_order.html', template_folder=current_app.template_folder)
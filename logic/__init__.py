# logic/__init__.py

from flask import Blueprint
from logic.database import init_database

# Initialize the database
init_database()

bp = Blueprint('main_app', __name__)

from logic.routes.index import landing_page
from logic.routes.email_interest import display_order_confirmation
from logic.routes.free_pair import display_free_pair
from logic.routes.complete_order import display_complete_order

# Add URL rules to the blueprint
bp.add_url_rule('/', 'landing_page', landing_page)
bp.add_url_rule('/order_confirmation', 'display_order_confirmation', display_order_confirmation)
bp.add_url_rule('/free_pair', 'display_free_pair', display_free_pair)
# bp.add_url_rule('/complete_order', 'display_complete_order', display_complete_order)
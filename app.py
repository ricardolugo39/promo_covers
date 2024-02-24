# app.py

from flask import Flask
from logic import bp
from logic.routes.free_pair import free_pair_bp
from logic.routes.complete_order import complete_order_bp
from logic.routes.admin import admin_bp
from logic.routes.index import temp_bp


app = Flask(__name__, template_folder='logic/templates', static_folder='logic/static')

# Register the blueprint
app.register_blueprint(bp)
app.register_blueprint(free_pair_bp)
app.register_blueprint(complete_order_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(temp_bp)

if __name__ == "__main__":
    app.run(debug=True)

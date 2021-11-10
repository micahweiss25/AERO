from flask import Blueprint, current_app


spages = Blueprint('spages', __name__,
                        template_folder='templates')


@spages.route("/")
def index():
    return current_app.send_static_file('index.html')

@spages.route("/dashboard")
def dash():
    return current_app.send_static_file('dashboard.html')
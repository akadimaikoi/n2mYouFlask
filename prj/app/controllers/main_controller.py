from flask import Blueprint, render_template
from app.services.main_service import get_data


main_bp = Blueprint('index', __name__)

@main_bp.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

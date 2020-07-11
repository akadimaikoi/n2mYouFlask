from flask import Blueprint
from app.models.response_model import RESPONSE

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/hi')
@hello_bp.route('/hello')
def hello():
    return RESPONSE

from flask import Blueprint
from api.models.response_model import response

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/hello')
def hello():
    return response['default']

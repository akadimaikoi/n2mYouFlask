from flask import Blueprint, jsonify
from app.services.answer_service import get_answer

answer_bp = Blueprint('api', __name__)

@answer_bp.route('/api')
def api_answer():
	answer = get_answer()
	return jsonify(answer), 200

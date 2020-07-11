from app.models.answer_model import AnswerModel

def get_answer():
	answer = AnswerModel(name='Flask Basic App!', description='A simple Flask application.')
	return ({'answer': answer.__dict__})

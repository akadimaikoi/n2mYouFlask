# prj/api/__init__.py
from flask import Flask
from app.controllers import main_bp, hello_bp, answer_bp

def create_app():
    project = Flask(__name__)
    project.register_blueprint(main_bp)
    project.register_blueprint(hello_bp)
    project.register_blueprint(answer_bp)
    return project

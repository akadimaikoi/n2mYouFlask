import os
import logging
from flask import Flask
from app.controllers import main_bp, hello_bp, answer_bp


def create_app():
	project = Flask(__name__)
	
	# Environment
	project.config["ENV"] = os.getenv("FLASK_ENV") == "production"
	project.config["DEBUG"] = os.getenv("FLASK_DEBUG") == "False"
	project.config["PORT"] = int(os.getenv("PORT", 8000))
	project.config["EXP"] = os.getenv("EXP")
	
	# Logging
	log_level = os.getenv("LOG_LEVEL", "ERROR")
	logging.basicConfig(level=log_level)
	
	logging.info(f"Valor de EXP: {os.getenv('EXP')}")
	
	project.register_blueprint(main_bp)
	project.register_blueprint(hello_bp)
	project.register_blueprint(answer_bp)
	
	return project
	

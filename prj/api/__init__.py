from flask import Flask
from api.controllers.hello_controller import hello_bp

app = Flask(__name__)
app.register_blueprint(hello_bp)

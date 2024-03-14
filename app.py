from api import api
from flask import Flask

app = Flask(__name__)

app.register_blueprint(api)
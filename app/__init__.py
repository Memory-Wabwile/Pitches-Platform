from flask import Flask

#initializing application
app = Flask(__name__)
from . import views
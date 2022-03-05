from flask import render_template
from . import main

@main.route('/')
def index():
    '''
    function that returns the index page and its data
    '''
    return render_template('index.html')
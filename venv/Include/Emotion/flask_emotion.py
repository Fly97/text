from flask import *
emotion = Blueprint('emotion', __name__)

@emotion.route('/add')
def add():
    return 'emotion_add'

@emotion.route('/show')
def show():
    return 'emotion_show'

from flask import *
grammer = Blueprint('grammer', __name__)

@grammer.route('/add')
def add():
    return 'grammer_add'

@grammer.route('/show')
def show():
    return 'grammer_show'
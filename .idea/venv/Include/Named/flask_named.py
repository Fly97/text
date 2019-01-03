from flask import *
named = Blueprint('named', __name__)

@named.route('/add')
def add():
    return 'named_add'

@named.route('/show')
def show():
    return 'named_show'
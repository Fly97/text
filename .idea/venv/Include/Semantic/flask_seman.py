from flask import *
seman = Blueprint('seman', __name__)

@seman.route('/add')
def add():
    return 'seman_add'

@seman.route('/show')
def show():
    return 'seman_show'
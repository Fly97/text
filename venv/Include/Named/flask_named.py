from flask import *
import codecs,json,sys,os
from Named import name
from Named import get_name
from flask_cors import CORS

named = Blueprint('named', __name__)
cors = CORS(named, resources={r"/named/sentdata": {"origins": "*"}})
cors = CORS(named, resources={r"/named/getdata": {"origins": "*"}})

@named.route('/sentdata',methods=['GET','POST'])                      ##从前端得到数据
def sentdata():
    data = request.get_data()
    json_re = json.loads(data)
    print(json_re["text"])
    name.whole(json_re["text"])
    return '完成'

@named.route('/getdata',methods=['GET','POST'])                       ##将数据从后端传到前端
def getdata():
    data = json.dumps(get_name.sett(), ensure_ascii=False)
    return data

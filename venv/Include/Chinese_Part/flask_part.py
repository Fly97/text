from flask import *
import codecs,json,sys,os
from Chinese_Part import tagging
from Chinese_Part import get_part
from flask_cors import CORS

part = Blueprint('part', __name__)
cors = CORS(part, resources={r"/part/sentdata": {"origins": "*"}})
cors = CORS(part, resources={r"/part/getdata": {"origins": "*"}})

@part.route('/sentdata',methods=['GET','POST'])                 ##从前端得到数据
def sentdata():
    data = request.get_data()
    json_re = json.loads(data)
    print(json_re["text"])
    tagging.whole(json_re["text"])      #进行词性标注
    return '完成'

@part.route('/getdata',methods=['GET','POST'])                       ##将数据从后端传到前端
def getdata():
    data = json.dumps(get_part.getdata(), ensure_ascii=False)
    return data


from flask import *
import codecs,json,sys,os
from Grammer import gramm
from Grammer import get
from flask_cors import CORS

grammer = Blueprint('grammer', __name__)
cors = CORS(grammer, resources={r"/grammer/sentdata": {"origins": "*"}})
cors = CORS(grammer, resources={r"/grammer/getdata": {"origins": "*"}})

@grammer.route('/sentdata',methods=['GET','POST'])                      ##从前端得到数据
def sentdata():
    data = request.get_data()
    json_re = json.loads(data)
    print(json_re["text"])
    gramm.whole(json_re["text"])      #进行词性标注
    return '完成'

@grammer.route('/getdata',methods=['GET','POST'])                       ##将数据从后端传到前端
def getdata():
    data = json.dumps(get.getdata(), ensure_ascii=False)
    return data


from flask import *
from Semantic import traindata
from Semantic import get
import codecs,json,sys,os
from flask_cors import CORS

seman = Blueprint('seman', __name__)
cors = CORS(seman, resources={r"/seman/sentdata": {"origins": "*"}})
cors = CORS(seman, resources={r"/seman/getdata": {"origins": "*"}})

@seman.route('/sentdata',methods=['GET','POST'])
def sentdata():
    data = request.get_data()
    json_re = json.loads(data)
    print(json_re["text"])
    traindata.whole(json_re["text"])  # 进行词性标注
    return '完成'

@seman.route('/getdata',methods=['GET','POST'])
def getdata():
    data = json.dumps(get.getdata(), ensure_ascii=False)
    return data
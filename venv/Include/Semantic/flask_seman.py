from flask import *
from Semantic import traindata
from Semantic import get
import codecs,json,sys,os
seman = Blueprint('seman', __name__)

@seman.route('/sentdata')
def sentdata():
    data = request.get_data()
    json_re = json.loads(data)
    print(json_re["text"])
    traindata.whole(json_re["text"])  # 进行词性标注
    return '完成'

@seman.route('/getdata')
def getdata():
    data = json.dumps(get.getdata(), ensure_ascii=False)
    return data
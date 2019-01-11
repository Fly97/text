from flask import *
import codecs,json,sys,os
from Emotion import get_emotion
from Emotion import emoting
from flask_cors import CORS

emotion = Blueprint('emotion', __name__)
cors = CORS(emotion, resources={r"/emotion/sentdata": {"origins": "*"}})
cors = CORS(emotion, resources={r"/emotion/getdata": {"origins": "*"}})

@emotion.route('/sentdata',methods=['GET','POST'])                 ##从前端得到数据
def sentdata():
    data = request.get_data()
    json_re = json.loads(data)
    print(json_re["text"])
    emoting.predict_one(json_re["text"])      #进行词性标注
    return '完成'

@emotion.route('/getdata',methods=['GET','POST'])                       ##将数据从后端传到前端
def getdata():
    data = json.dumps(get_emotion.getdata(), ensure_ascii=False)
    return data
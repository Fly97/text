from flask import *
import codecs,json,sys,os
import tagging
from setdata import setdata
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/zhx": {"origins": "*"}})
cors = CORS(app, resources={r"/save": {"origins": "*"}})
app.config['JSON_AS_ASCII'] = False

@app.route('/sentdata',methods=['GET','POST'])                      ##从前端得到数据
def sentdata():
    data = request.get_data()
    json_re = json.loads(data)
    print(json_re["text"])
    tagging.whole(json_re["text"])      #进行词性标注
    return '完成'

@app.route('/getdata',methods=['GET','POST'])                       ##将数据从后端传到前端
def getdata():
    data = json.dumps(setdata(), ensure_ascii=False)
    return data

if __name__ == '__main__':
    app.run( port=8888, debug=True)

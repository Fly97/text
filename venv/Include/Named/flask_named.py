from flask import *
from Named import name
from Named import setdata
named = Blueprint('named', __name__)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@named.route('/sentdata',methods=['GET','POST'])                      ##从前端得到数据
def sentdata():
    data = request.get_data()
    json_re = json.loads(data)
    print(json_re["text"])
    name.whole(json_re["text"])
    return '完成'

@named.route('/getdata',methods=['GET','POST'])                       ##将数据从后端传到前端
def getdata():
    data = json.dumps(setdata.set(), ensure_ascii=False)
    return data

from flask import *
import codecs,json,sys,os
import tagging
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/zhx": {"origins": "*"}})
cors = CORS(app, resources={r"/save": {"origins": "*"}})
app.config['JSON_AS_ASCII'] = False

@app.route('/chinese')
def chinese():
    return render_template('main.html')

@app.route('/chinese_crf',methods=['GET'])
def chinese_crf():
    text=request.args.get("wd")
    tagging.whole(text)
    data = json.dumps(setdata(), ensure_ascii=False)
    return data


def setdata():         #将以及处理完（词性标注）的数据从文件中读出
    input = codecs.open("..\\resource\chinese_part\\outpart.txt", 'r', 'utf-8')
    words=""
    parts=""
    text=""
    for line in input.readlines():
        text=line
        strs=line.strip().split()
        for str in strs:
            st=str.strip().split('/')
            words = words + st[0] + ','
            parts = parts + st[1] + ','
    data=[{
        'words': words,
        'parts': parts,
        'text': text,
    }]
    input.close()
    return data

if __name__ == '__main__':
    app.run( port=2222, debug=True)

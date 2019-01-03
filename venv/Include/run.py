from flask import *
import codecs,json,sys,os
from Chinese_Part import get
from Chinese_Part import tagging
from Chinese_Part import flask_part
from Emotion import flask_emotion
from Named import flask_named
from Grammer import flask_grammer
from Semantic import flask_seman

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# 这里分别给app注册了两个蓝图admin,user
# 参数url_prefix='/xxx'的意思是设置request.url中的url前缀，
# 即当request.url是以/admin或者/user的情况下才会通过注册的蓝图的视图方法处理请求并返回
app.register_blueprint(flask_part.part, url_prefix='/part')
app.register_blueprint(flask_emotion.emotion, url_prefix='/emotion')
app.register_blueprint(flask_grammer.grammer, url_prefix='/grammer')
app.register_blueprint(flask_named.named, url_prefix='/named')
app.register_blueprint(flask_seman.seman, url_prefix='/seman')


@app.route('/')
def index():
    return render_template('main.html')

@app.route('/chinese_crf',methods=['GET'])
def chinese_crf():
    text=request.args.get("wd")
    tagging.whole(text)
    data = json.dumps(get.getdata(), ensure_ascii=False)
    return data

@app.errorhandler(500)
def error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    print(app.url_map)
    app.run(port=4444, debug=True)
import codecs,json,sys,os
def getdata():         #将以及处理完（词性标注）的数据从文件中读出
    input = codecs.open("../resource/emotion/out.txt", 'r', 'utf-8')
    str=input.read()
    emotion=""
    if str=='1':
        emotion="positive"
    else:
        emotion="negative"
    input.close()
    data=[{
        'sign': str,
        'emotion': emotion,
    }]
    return data

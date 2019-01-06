import codecs,json,sys,os
def getdata():         #将以及处理完（词性标注）的数据从文件中读出
    input = codecs.open("../resource/chinese_part/outpart.txt", 'r', 'utf-8')
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
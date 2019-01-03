import codecs,json,sys,os
def set():         #将以及处理完（命名实体识别）的数据从文件中读出
    input = codecs.open("..\\resource\\name_recognition\\nameoutput.txt", 'r', 'utf-8')
    PER=""
    LOC=""
    ORG=""
    for line in input.readlines():
        LOC = []
        PER = []
        ORG = []
        str = line.strip().split()
        for s in str:
            z = s.strip().split(":")
            tag = z[0]
            word = z[1]
            if tag == "LOC":
                LOC.append(word)
            if tag == "PER":
                PER.append(word)
            if tag == "ORG":
                ORG.append(word)
    data=[{
        'PER': PER,
        'LOC': LOC,
        'ORG': ORG,
    }]
    input.close()
    return data
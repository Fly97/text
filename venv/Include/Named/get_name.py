import codecs,json,sys,os
def sett():         #将以及处理完（命名实体识别）的数据从文件中读出
    input = codecs.open("../resource/name_recognition/nameoutput.txt", 'r', 'utf-8')
    PER=""
    LOC=""
    ORG=""
    PER1 = ""
    LOC1 = ""
    ORG1 = ""
    for line in input.readlines():
        LOC = []
        PER = []
        ORG = []
        str = line.strip().split()
        for s in str:
            z = s.strip().split(":")
            tag = z[0]
            word = z[1]
            if tag == "PER":
                PER.append(word)
            if tag == "LOC":
                LOC.append(word)
            if tag == "ORG":
                ORG.append(word)
    PER = list(set(PER))
    LOC = list(set(LOC))
    ORG = list(set(ORG))
    for i in range(0,PER.__len__()):
        PER1=PER1+PER[i]+','
    for i in range(0,LOC.__len__()):
        LOC1=LOC1+LOC[i]+','
    for i in range(0,ORG.__len__()):
        ORG1=ORG1+ORG[i]+','
    data = [{
        'PER': PER1,
        'LOC': LOC1,
        'ORG': ORG1,
    }]
    input.close()
    return data


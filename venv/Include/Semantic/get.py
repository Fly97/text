import codecs,json,sys,os
def getdata():         #将以及处理完（词性标注）的数据从文件中读出
    input = codecs.open("../resource/chinese_srl/dataout.txt", 'r', 'utf-8')
    words=""
    parts=""
    roles=""
    for line in input.readlines():
        strs=line.strip().split()
        if(len(strs)<3):
            continue
        words = words + strs[0] + ','
        parts = parts + strs[1] + ','
        roles=roles + strs[2] + ','


    data=[{
        'words': words,
        'parts': parts,
        'roles': roles,
    }]
    input.close()
    return data

if __name__ == '__main__':
    print(getdata())
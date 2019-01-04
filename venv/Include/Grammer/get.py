import codecs,json,sys,os
def getdata():         #将以及处理完（词性标注）的数据从文件中读出
    input = codecs.open("../resource/gramm/graout.txt", 'r', 'utf-8')
    words=""
    parts=""
    relation=""
    for line in input.readlines():
        strs=line.strip().split()
        if (len(strs) < 5):
            continue
        words = words + strs[0] + ','
        parts = parts + strs[1] + ','
        relation = relation + strs[4]+ ','
    data=[{
        'words': words,
        'parts': parts,
        'relation': relation,
    }]
    input.close()
    return data
if __name__ == '__main__':
    print(getdata())


import codecs,json,sys,os
def getdata():         #将以及处理完（词性标注）的数据从文件中读出
    input = codecs.open("../resource/chinese_srl/dataout.txt", 'r', 'utf-8')
    words=[]
    roles=[]
    w=""
    r=""
    for line in input.readlines():
        strs=line.strip().split()
        if(len(strs)<3):
            continue

        # words = words + strs[0] + ','
        # parts = parts + strs[1] + ','
        # roles=roles + strs[2] + ','
        words.append(strs[0])
        roles.append(strs[2])
    # print(words)
    # print(roles)

    # data=[{
    #     'words': words,
    #     'roles': roles,
    # }]
    tag=roles[0]
    for i in range(0,roles.__len__()):
        if roles[i]==tag:
            w=w+words[i]+"/"
        else:
            #
            if tag=="ARGM-TMP":
                tag1="时间"
            elif tag=="-":
                tag1="-"
            elif tag=="ARGM-LOC":
                tag1="地点"
            elif tag=="ARG0":
                tag1="主体"
            elif tag=="ARG1":
                tag1="主体1"
            elif tag=="ARG2":
                tag1="主体2"
            elif tag=="ARG3":
                tag1="主体3"
            elif tag=="ARGM-MNR":
                tag1="方式"
            elif tag=="ARGM-BNE":
                tag1="受益人"
            elif tag=="ARGM-CND":
                tag1="条件"
            elif tag=="ARGM-DIR":
                tag1="方向"
            elif tag=="ARGM-DGR":
                tag1="程度"
            elif tag=="ARGM-EXT":
                tag1="扩展"
            elif tag=="ARGM-ADV":
                tag1="标记"
            elif tag=="V":
                tag1="动词"

            elif tag=="FRQ":
                tag1="频率"
            elif tag=="ARGM-PRP":
                tag1="目的"
            elif tag=="ARGM-TPC":
                tag1="主题"
            elif tag=="ARGM-CRD":
                tag1="并列参数 "
            elif tag=="ARGM-PRD":
                tag1="谓语动词"
            elif tag=="ARGM-PSR":
                tag1="持有者"
            elif tag=="ARGM-PSE":
                tag1="被持有"
            else:
                tag1=tag
            #

            w=w+","+words[i]
            r=r+tag1+","
            tag=roles[i]

    data=[{
        'words': w,
        'roles': r,
    }]

    input.close()
    return data

if __name__ == '__main__':
    print(getdata())
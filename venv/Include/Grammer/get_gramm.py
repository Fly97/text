import codecs,json,sys,os
def getdata():         #将以及处理完（词性标注）的数据从文件中读出
    input = codecs.open("../resource/gramm/out2.txt", 'r', 'utf-8')
    id=""
    fid=""
    word=""
    post = ""
    dep_type = ""
    da=[]
    for line in input.readlines():
        strs=line.strip().split()
        # if (len(strs) < 7):
        #     continue
        if (len(strs) >6):
            fidd = int(strs[6])
            if int(strs[6])>0:
                fidd=fidd-1
            id = id + strs[0] + ','
            fid = fid + str(fidd) + ','
            word = word + strs[1]+ ','
            post = post + strs[3] + ','
            dep_type = dep_type + strs[7] + ','
        else:
            data={
                'id': id,
                'fid': fid,
                'word': word,
                'post': post,
                'dep_type': dep_type,
            }
            da.append(data)
            id = ""
            fid = ""
            word = ""
            post = ""
            dep_type = ""
#    data = [{
#        'id': id,
#       'fid': fid,
#        'word': word,
#        'post': post,
#        'dep_type': dep_type,
#    }]
#    da.append(data)
    input.close()
    return da
if __name__ == '__main__':
    print(getdata())



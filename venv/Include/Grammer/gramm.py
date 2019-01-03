import codecs
import sys
import os
from Chinese_Part import tagging



def settest():
    f = open('..\\..\\resource\gramm\\graout.txt', 'w')
    f.truncate()
    f.close()
    path = os.path.abspath(os.path.dirname(os.getcwd()))
    path = path.replace("\Include", "")
    path1 = path + "\\resource\chinese_part\outpart.txt"
    path2=  path + "\\resource\gramm\\test.data"
    input_data = open(path1, 'r', encoding='utf-8')#读
    output_data = codecs.open(path2, 'w', 'utf-8')#写
    for line in input_data.readlines():
        word_list = line.strip().split()
        for word in word_list:
            w = word.strip().split('/')
            output_data.write(w[0]+'\t'+w[1]+'\t'+w[1]+'\t'+'O\n')
    input_data.close()
    output_data.close()

def totest():
    path = os.path.abspath(os.path.dirname(os.getcwd()))
    path = path.replace("\Include", "")
    path = path+ "\\resource\gramm"
    order = "crf_test -m model test.data >>graout.txt"
    command = "cd /d " + path + "&&" + order
    os.system(command)

def whole():
    tagging.whole("六点半我要去坐火车！")
    settest()
    totest()

if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(os.getcwd()))
    path = path.replace("\Include", "")
    path = path + "\\resource\gramm\graout.txt"
    whole()
    input = codecs.open(path, 'r', 'utf-8')
    for line in input.readlines():
        print(line)

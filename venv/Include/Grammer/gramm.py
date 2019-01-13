import codecs
import sys
import os
from Chinese_Part import tagging

def settest():
    f = open('../resource/gramm/out1.txt', 'w')
    f.truncate()
    f.close()
    f = open('../resource/gramm/out2.txt', 'w')
    f.truncate()
    f.close()
    path = os.path.abspath(os.path.dirname(os.getcwd()))
    path = path.replace("/Include", "")
    path1 = path + "/resource/chinese_part/outpart.txt"
    path2=  path + "/resource/gramm/test.data"
    input_data = open(path1, 'r', encoding='utf-8')#读
    output_data = codecs.open(path2, 'w', 'utf-8')#写

    for line in input_data.readlines():
        i=0
        word_list = line.strip().split()
        for word in word_list:
            i=i+1
            w = word.strip().split('/')
            output_data.write(str(i)+'\t'+w[0]+'\t'+w[0]+'\t'+w[1]+'\t'+w[1]+'\t'+'O\n')
            if w[0]=="。":
                output_data.write('\n')
                i=0
    input_data.close()
    output_data.close()

def totest():
    path = os.path.abspath(os.path.dirname(os.getcwd()))
    path = path.replace("/Include", "")
    path = path+ "/resource/gramm"
    order = "crf_test -m model1 test.data >>out1.txt"
    command = "cd " + path + "&&" + order
    os.system(command)
    order = "crf_test -m model2 out1.txt >>out2.txt"
    command = "cd " + path + "&&" + order
    os.system(command)


def whole(text):
    tagging.whole(text)
    settest()
    totest()

if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(os.getcwd()))
    path = path.replace("/Include", "")
    path = path + "/resource/gramm/graout.txt"
    whole("今天天气真好")
    input = codecs.open(path, 'r', 'utf-8')
    for line in input.readlines():
        print(line)

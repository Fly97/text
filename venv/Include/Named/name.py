import codecs
import sys
import os

def character_split(input_file, output_file):#数据预处理
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    for line in input_data.readlines():
        for word in line.strip():
            word = word.strip()
            if word:
                output_data.write(word + "\tB\n")
    input_data.close()
    output_data.close()

def setname(text):                              #实体识别
    f = open('../resource/name_recognition/nameinput.txt', 'w')
    f.truncate()
    f.close()
    filename = '../resource/input_text.txt'
    string = text
    with codecs.open(filename, 'w', 'utf-8') as file_object:
        file_object.write(string)
    input_file = "../resource/input_text.txt"
    output_file = "../resource/name_recognition/test_name.data"
    character_split(input_file, output_file)
    #print("已生成测试集\n开始进行文本测试")
    path = os.path.abspath(os.path.dirname(os.getcwd()))
    path = path.replace("/Include", "")
    path = path + "/resource/name_recognition"
    order = "crf_test -m model_name test_name.data >>nameinput.txt"  # 生成train格式储存到nameinput
    command = "cd " + path + "&&" + order
    os.system(command)


def character_word():              #命名实体识别后的数据处理
    input_data = open("../resource/name_recognition/nameinput.txt", 'r', encoding='utf-8')
    output_data = codecs.open("../resource/name_recognition/nameoutput.txt", 'w', 'utf-8')


    for line in input_data.readlines():
        if line == '\n':
            output_data.write('\n')
        else:
            char_tag_pair = line.strip().split('\t')
            char = char_tag_pair[0]
            tag = char_tag_pair[2]
            if tag == 'B-PER':#人名
                output_data.write(' PER:' + char)
            elif tag == 'I-PER':
                output_data.write(char)
            if tag == 'B-LOC':#地名
                output_data.write(' LOC:' + char)
            elif tag == 'I-LOC':
                output_data.write(char)
            if tag == 'B-ORG':  # 机构名
                output_data.write(' ORG:' + char)
            elif tag == 'I-ORG':
                output_data.write(char)

    input_data.close()
    output_data.close()


def whole(text):
    setname(text)
    character_word()

if __name__ == '__main__':
    whole("卢思童和曾辉祥在河南的郑州的中原工学院的计算机学院打球！")

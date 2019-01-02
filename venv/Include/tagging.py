import codecs
import sys
import os

def character_split(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    for line in input_data.readlines():
        for word in line.strip():
            word = word.strip()
            if word:
                output_data.write(word + "\tS\n")
    input_data.close()
    output_data.close()

def setword(text):
    f = open('..\\resource\chinese_word\\wording.txt', 'w')
    f.truncate()
    f.close()
    filename = '..\\resource\\input_text.txt'
    string = text
    with codecs.open(filename, 'w', 'utf-8') as file_object:
        file_object.write(string)
    input_file = "..\\resource\\input_text.txt"
    output_file = "..\\resource\chinese_word\\test_word.data"
    character_split(input_file, output_file)
    #print("已生成测试集\n开始进行文本测试")
    path = os.path.abspath(os.path.dirname(os.getcwd())) + "\\resource\chinese_word"
    order = "crf_test -m model_word test_word.data >>wording.txt"
    command = "cd /d " + path + "&&" + order
    os.system(command)

def setpart():
    input = codecs.open("..\\resource\chinese_word\\outword.txt", 'r', 'utf-8')
    output = codecs.open("..\\resource\chinese_part\\test_part.data", 'w', 'utf-8')
    f = open('..\\resource\chinese_part\\parting.txt', 'w')
    f.truncate()
    f.close()
    for line in input.readlines():
        word_list = line.strip().split('  ')
        for word in word_list:
            output.write(word + '\tX' + '\n')
    input.close()
    output.close()
    path = os.path.abspath(os.path.dirname(os.getcwd())) + "\\resource\chinese_part"
    order = "crf_test -m model_part test_part.data >>parting.txt"
    command = "cd /d " + path + "&&" + order
    os.system(command)

def character_word():
    input_data = open("..\\resource\chinese_word\\wording.txt", 'r', encoding='utf-8')
    output_data = codecs.open("..\\resource\chinese_word\\outword.txt", 'w', 'utf-8')
    for line in input_data.readlines():
        if line == '\n':
            output_data.write('\n')
        else:
            char_tag_pair = line.strip().split('\t')
            char = char_tag_pair[0]
            tag = char_tag_pair[2]
            if tag == 'B':
                output_data.write(' ' + char)
            elif tag == 'M':
                output_data.write(char)
            elif tag == 'E':
                output_data.write(char + ' ')
            else: # tag == 'S'
                output_data.write(' ' + char + ' ')
    input_data.close()
    output_data.close()

def character_part():
    input = open("..\\resource\chinese_part\\parting.txt", 'r', encoding='utf-8')
    output = codecs.open("..\\resource\chinese_part\\outpart.txt", 'w', 'utf-8')
    for line in input.readlines():
        line = line.replace('\n', '')
        line=line.replace('\t', '')
        line = line.replace('X', '/')
        line=line+' '
        output.write(line)
    input.close()
    output.close()
    print("分词：")
    inputwort = codecs.open("..\\resource\chinese_word\\outword.txt", 'r', 'utf-8')
    for line in inputwort.readlines():
        print(line)
    print("词性标注：")
    input = codecs.open("..\\resource\chinese_part\\outpart.txt", 'r', 'utf-8')
    for line in input.readlines():
        print(line)


def whole(text):

    setword(text)
    character_word()
    setpart()
    character_part()

if __name__ == '__main__':
    whole("今天真好")
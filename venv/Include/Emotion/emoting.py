import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
import pandas as pd
import jieba
from keras.models import load_model
import ast
import  codecs
from keras import backend as K
K.clear_session()
# pos = pd.read_excel('pos.xls', header=None)
# pos['label'] = 1
# neg = pd.read_excel('neg.xls', header=None)
# neg['label'] = 0
# all_ = pos.append(neg, ignore_index=True)
# all_['words'] = all_[0].apply(lambda s: list(jieba.cut(s))) #调用结巴分词
#


# maxlen = 100 #截断词数
# min_count = 5 #出现次数少于该值的词扔掉。这是最简单的降维方法


# #
# content = []
# for i in all_['words']:
# 	content.extend(i)
# print("content数据格式",type(content))
# print(content)
# file = open('content.txt','w')
# file.write(str(content))
# file.close()
#


# file_object=open('cont.txt')
# list_str = file_object.read()
#
# content = ast.literal_eval(list_str)
#
# abc = pd.Series(content).value_counts()
# abc = abc[abc >= min_count]
# abc[:] = list(range(1, len(abc)+1))
# abc[''] = 0 #添加空字符串用来补全
# word_set = set(abc.index)
#
#
# print("成功")
# def doc2num(s, maxlen):
#     s = [i for i in s if i in word_set]
#     s = s[:maxlen] + ['']*max(0, maxlen-len(s))
#     return list(abc[s])

# all_['doc2num'] = all_['words'].apply(lambda s: doc2num(s, maxlen))
#
# #手动打乱数据
# idx = list(range(len(all_)))
# np.random.shuffle(idx)
# all_ = all_.loc[idx]
#
# #按keras的输入要求来生成数据
# x = np.array(list(all_['doc2num']))
# y = np.array(list(all_['label']))
# y = y.reshape((-1,1)) #调整标签形状

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Embedding
from keras.layers import LSTM

# 建立模型
# model = Sequential()
# model.add(Embedding(len(abc), 256, input_length=maxlen))
# model.add(LSTM(128))
# model.add(Dropout(0.5))
# model.add(Dense(1))
# model.add(Activation('sigmoid'))
# model.compile(loss='binary_crossentropy',
#               optimizer='adam',
#               metrics=['accuracy'])
#
# batch_size = 128
# train_num = 15000
#
# model.fit(x[:train_num], y[:train_num], batch_size = batch_size, nb_epoch=30)
#
# model.evaluate(x[train_num:], y[train_num:], batch_size = batch_size)
#
# print("开始训练")
# model.save("model",overwrite=True, include_optimizer=True)
# print("训练成功")

# list = []          ## 空列表
# str="曾辉祥 你 真好 ， 我 喜欢 你 。"
# for li in str.strip().split():
#     list.append(li)   ## 使用 append() 添加元素
# print(list)

# def doc2num(s, maxlen):
#     s = [i for i in s if i in word_set]
#     s = s[:maxlen] + [''] * max(0, maxlen - len(s))
#     return list(abc[s])

def doc2num(s, maxlen):
    min_count = 5  # 出现次数少于该值的词扔掉。这是最简单的降维方法
    file_object = open('../../resource/emotion/cont.txt', encoding='UTF-8')
    list_str = file_object.read()
    file_object.close()
    content = ast.literal_eval(list_str)
    abc = pd.Series(content).value_counts()
    abc = abc[abc >= min_count]
    abc[:] = list(range(1, len(abc) + 1))
    abc[''] = 0  # 添加空字符串用来补全
    word_set = set(abc.index)
    s = [i for i in s if i in word_set]
    s = s[:maxlen] + [''] * max(0, maxlen - len(s))
    return list(abc[s])

def predict_one(s): #单个句子的预测函数
    maxlen = 100  # 截断词数
    model = load_model('../resource/emotion/model')
    s = np.array(doc2num(list(jieba.cut(s)), maxlen))
    s = s.reshape((1, s.shape[0]))
    output = codecs.open('../resource/emotion/out.txt', 'w', 'utf-8')
    output.write(str(model.predict_classes(s)[0][0]))
    output.close()
    # return model.predict_classes(s)[0][0]

# print("情感分析",predict_one("马碧的牛根生坑爹，这包装一不小心就买错蒙牛了。我是扔呢还是扔呢？"))


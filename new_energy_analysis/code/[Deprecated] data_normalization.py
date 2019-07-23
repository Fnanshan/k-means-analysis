# -*- coding: utf-8 -*-
# 数据规范化
import pandas as pd
import numpy as np

datafile = '../data/1.xls'     # 参数初始化
data = pd.read_excel(datafile, header=None)   # 读取数据
# print(data[u'longitude'])
data = data[1:][2]
# print(data)
print('最小-最大规范化\n', (data - data.min())/(data.max() - 1.0*data.min()))  # 最小-最大规范化
print('零-均值规范化\n', (data - data.mean())/data.std())     # 零-均值规范化
print('小数定标规范化\n', data/10**np.ceil(np.log10(data.abs().max())))    # 小数定标规范化
# print(data - data.min())

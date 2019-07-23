# -*- coding: utf-8 -*-
# Taxi数据统计量分析
from __future__ import print_function
import pandas as pd

taxiData = '../data/1.xls'  # Taxi数据
data = pd.read_excel(taxiData, index_col=u'taxiId')     # 读取数据，指定“taxiId”列为索引列
# 北京市界的地理坐标为   北纬39”26’至41”03’，东经115”25’至 117”30’。
# longitude 经度      latitude 维度；
# taxi经纬度格式     116.47191,39.90577
# xls中的logitude列是数字，latitude列是字符串
data = data[(data[u'longitude'] > 115.25000) & (data[u'longitude'] < 117.30000) & (data[u'latitude'] > 39.26000) & (data[u'latitude'] < 41.03000)]  # 过滤异常数据
statistics = data.describe()  # 保存基本统计量

statistics.loc['range'] = statistics.loc['max']-statistics.loc['min']  # 极差
statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean']  # 变异系数
statistics.loc['dis'] = statistics.loc['75%']-statistics.loc['25%']  # 四分位数间距

print(statistics)

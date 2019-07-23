# -*- coding: utf-8 -*-
import pandas as pd
import json
from urllib.request import urlopen, quote
import csv
import traceback
import os


# # 构造获取经纬度的函数
# def getlnglat(address):
#     url = 'http://api.map.baidu.com/geocoder/v2/?address='
#     output = 'json'
#     # ak = '你的ak'#需填入自己申请应用后生成的ak
#     ak = 'qmoh1p3EWrIhe52RwQcCPGzxFOAYbDGE'
#     add = quote(address)  # 本文城市变量为中文，为防止乱码，先用quote进行编码
#     # http://api.map.baidu.com/geocoder/v2/?address=你的地址&output=json&ak=您的ak&callback=showLocation //GET请求
#     url2 = url + add + '&output=' + output + "&ak=" + ak
#     req = urlopen(url2)
#     res = req.read().decode()   # 将其他编码的字符串解码成unicode
#     temp = json.loads(res)      # 对json数据进行解析
#     return temp


file = open('../tmp/1.json', 'w')  # 建立json数据文件
with open('../data/1.csv', 'r') as csvfile:  # 打开csv
    reader = csv.reader(csvfile)
    for line in reader:  # 读取csv里的数据
        # 忽略第一行
        if reader.line_num == 1:  # 由于第一行为变量名称，故忽略掉
            continue
            # line是个list，取得所有需要的值
        taxiId = line[0].strip()  # 将第一列city读取出来并清除不需要字符
        lng = line[1].strip()  # 将第二列price读取出来并清除不需要字符
        lat = line[2].strip()
        print('taxiId :\n', taxiId)
        print('lng :\n', lng)
        print('lat :\n', lat)
        # lng = getlnglat(b)['result']['location']['lng']  # 采用构造的函数来获取经度
        # lat = getlnglat(b)['result']['location']['lat']  # 获取纬度
        str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"taxiId":' + str(taxiId) +'},'
        # str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(c) +'},'
        # print(str_temp) #也可以通过打印出来，把数据copy到百度热力地图api的相应位置上
        file.write(str_temp)  # 写入文档
file.close()  # 保存

# file = open('经纬度.json', 'w')  # 建立json数据文件
# data_1 = pd.read_csv("house_price.csv")  # 读取小区房价信息
# for i in data_1.values:
#     try:
#         b = i[0].strip()
#         print('b :\n', b)
#         c = str(i[1]).strip()
#         print('c :\n', c)
#         lng = getlnglat(b)['result']['location']['lng']  # 获取经度
#         lat = getlnglat(b)['result']['location']['lat']  # 获取纬度
#         str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(c) + '},'
#         file.write(str_temp)
#     except:
#         f = open("异常日志.txt", 'a')
#         traceback.print_exc(file=f)
#         f.flush()
#         f.close()
# file.close()
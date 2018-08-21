#coding:gbk
import pandas as pd
import numpy as np
import json
from urllib2 import urlopen, quote
import csv
import traceback
import os

# 构造获取经纬度的函数
def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/?address='
    output = 'json'
    ak = '[*Your Key]'
    add = quote(address)  # 本文城市变量为中文，为防止乱码，先用quote进行编码
    url2 = url + add + '&output=' + output + "&ak=" + ak
    req = urlopen(url2)
    res = req.read().decode()
    temp = json.loads(res)
    return temp

out = open('[*Output File Name]','wb')
#out = open("test.csv", 'wb')
#writer = csv.writer(out, dialect='excel')
input = pd.read_csv("[*Input File Name]",low_memory=False)
for i in input.values:
    try:
        row = []
        id = i[0]
        b = i[3].strip()
        #lng = getlnglat(b)['result']['location']['lng']  # 获取经度
        #lat = getlnglat(b)['result']['location']['lat']  # 获取纬度
        pre = getlnglat(b)['result']['precise']  # 是否精确查找
        con = getlnglat(b)['result']['confidence']  # 可信度
        lev = getlnglat(b)['result']['level']  # 能精确理解的地址类型

        str_temp = str(id) + ',' + str(b) + ',' + str(pre) + ',' + str(con) + ',' + str(lev) + '\n'
        #str_temp = '{"id":' + str(id) + ',"address":' + str(b) + ',"precise":' + str(pre) + ',"confidence":' + str(con) +',"level":'+str(lev) +'},'
        out.write(str_temp)
        #row.append([id, b, pre, con, lev])
        #writer.writerow(row)
    except:
        f = open("异常日志.txt", 'a')
        traceback.print_exc(file=f)
        f.flush()
        f.close()
out.close()
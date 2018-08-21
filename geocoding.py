#coding:gbk
import pandas as pd
import numpy as np
import json
from urllib2 import urlopen, quote
import csv
import traceback
import os

# �����ȡ��γ�ȵĺ���
def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/?address='
    output = 'json'
    ak = '[*Your Key]'
    add = quote(address)  # ���ĳ��б���Ϊ���ģ�Ϊ��ֹ���룬����quote���б���
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
        #lng = getlnglat(b)['result']['location']['lng']  # ��ȡ����
        #lat = getlnglat(b)['result']['location']['lat']  # ��ȡγ��
        pre = getlnglat(b)['result']['precise']  # �Ƿ�ȷ����
        con = getlnglat(b)['result']['confidence']  # ���Ŷ�
        lev = getlnglat(b)['result']['level']  # �ܾ�ȷ���ĵ�ַ����

        str_temp = str(id) + ',' + str(b) + ',' + str(pre) + ',' + str(con) + ',' + str(lev) + '\n'
        #str_temp = '{"id":' + str(id) + ',"address":' + str(b) + ',"precise":' + str(pre) + ',"confidence":' + str(con) +',"level":'+str(lev) +'},'
        out.write(str_temp)
        #row.append([id, b, pre, con, lev])
        #writer.writerow(row)
    except:
        f = open("�쳣��־.txt", 'a')
        traceback.print_exc(file=f)
        f.flush()
        f.close()
out.close()
# Author：jingyile
# Data:2020/3/18 下午3:45
# Des:统计各个网页类型所占的比例

import pandas as pd
import numpy as np
from pandas import DataFrame
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:Answer1025.@localhost/DataMining?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize = 10000)
'''
用create_engine建立连接，连接地址的意思依次为“数据库格式（mysql）+程序名（pymysql）+账号密码@地址端口/数据库名（test）”，最后指定编码为utf8；
all_gzdata是表名，engine是连接数据的引擎，chunksize指定每次读取1万条记录。这时候sql是一个容器，未真正读取数据。
'''
# 找出所有类别
counts = [ i['fullURLId'].value_counts() for i in sql] #逐块统计
counts = pd.concat(counts).groupby(level=0).sum() #合并统计结果，把相同的统计项合并（即按index分组并求和）
counts = counts.reset_index() #重新设置index，将原来的index作为counts的一列。
counts.columns = ['index', 'num'] #重新设置列名，主要是第二列，默认为0
# print(counts)
counts['type'] = counts['index'].str.extract('(\d{3})') #提取前三个数字作为类别id
counts_ = counts[['type', 'num']].groupby('type').sum() #按类别合并
counts_.sort_values('num', ascending = False,inplace=True) #降序排列 替换
counts_['percentage'] = (counts_['num']/counts_['num'].sum())*100
# counts_.to_excel('./step1-1.xlsx')  #大类别及比例
# print(counts_)


# ------------------------------------------每个大类别下面小类别占比-----------------------------------------
a = counts.set_index(['type'])
b = counts.groupby('type').sum() # 同count_s
c = pd.merge(a,b,left_index=True,right_index=True)
c['persentage'] = (c['num_x']/c['num_y'])*100
del c['num_y']
c.rename(columns={'num_x':'num'},inplace=True)
print(c)
c.to_excel('./step1-2.xlsx')  #小类别及比例

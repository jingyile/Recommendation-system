# Author：jingyile
# Data:2020/3/18 下午4:09
# Des:点击次数分析

import pandas as pd
import numpy as np
from pandas import DataFrame
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://root:Answer1025.@localhost/DataMining?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize = 10000)

# 统计点击次数
c = [i['realIP'].value_counts() for i in sql] # 分块统计各个IP的出现次数
count3 = pd.concat(c).groupby(level = 0).sum() # 合并统计结果，level=0表示按index分组
count_df = pd.DataFrame(count3) # Series转为DataFrame
count3=count_df
count3[1]=1 # 添加1列全为1
realIP_sum = count3['realIP'].sum()
count3 = count3.groupby('realIP').sum()  ##统计各个“不同点击次数”分别出现的次数# 也可以使用counts1_['realIP'].value_counts()功能
count3.columns = [u'用户数']
count3.index.name = u'点击次数'
count3[u'用户百分比'] = count3[u'用户数']/count3[u'用户数'].sum()*100
count3[u'点击记录百分比'] = count3[u'用户数']*count3.index/realIP_sum*100
count3.sort_index(inplace = True)
c=count3.iloc[:7,]
c=c.T
# ----------------------------------统计1~7次数及7次以上的点击数-----------------------
c.insert(0,u'总计',[count3[u'用户数'].sum(),100,100])
c[u'>7'] = c.iloc[:,0]- c.iloc[:,1:].sum(1)
d = c.T
format = lambda x: '%.2f' % x  # 也可以使用d.round(4)
d = d.applymap(format)
d.to_excel('./step4-1.xlsx')
print(d)



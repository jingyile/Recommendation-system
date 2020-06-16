# Author：jingyile
# Data:2020/3/18 下午4:03
# Des:网页107类型中的内部统计

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:Answer1025.@localhost/DataMining?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize = 10000)

#统计107类别的情况
def count107(i): #自定义统计函数
  j = i[['fullURL']][i['fullURLId'].str.contains('107')].copy() #找出类别包含107的网址
  j['type'] = None #添加空列
  j['type'][j['fullURL'].str.contains('info/.+?/')] = u'知识首页' #info以/结尾
  j['type'][j['fullURL'].str.contains('info/.+?/.+?')] = u'知识列表页'
  j['type'][j['fullURL'].str.contains('/\d+?_*\d+?\.html')] = u'知识内容页'
  return j['type'].value_counts()

counts2 = [count107(i) for i in sql] #逐块统计
counts2 = pd.concat(counts2).groupby(level=0).sum() #合并统计结果
res107 = pd.DataFrame(counts2)
# res107.reset_index(inplace=True)
res107.index.name= u'107类型'
res107.rename(columns={'type':'num'},inplace=True)
res107[u'百分比'] = (res107['num']/res107['num'].sum())*100
res107.reset_index(inplace = True)
# res107.to_excel('./step2-1.xlsx')
print(res107)



# Author：jingyile
# Data:2020/3/18 下午4:03
# Des:网页199类型中的内部统计

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:Answer1025.@localhost/DataMining?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize = 10000)

# #统计199类别的情况


def count199(i):
  j = i[['pageTitle']][i['fullURLId'].str.contains('199') & i['fullURL'].str.contains('\?')]
  j['title'] = 1
  j['title'][j['pageTitle'].str.contains('法律快车-律师助手')] = '法律快车-律师助手'
  j['title'][j['pageTitle'].str.contains('免费发布法律咨询')] = '免费发布法律咨询'
  j['title'][j['pageTitle'].str.contains('咨询发布成功')] = '咨询发布成功'
  j['title'][j['pageTitle'].str.contains('法律快搜')] = '快搜'
  j['title'][j['title'] == 1] = '其他类型'
  return j



counts = [count199(i) for i in sql]
counts_ = pd.concat(counts)
res199 = counts_['title'].value_counts()
res199 = pd.DataFrame(res199)
res199.reset_index(inplace=True)
res199['percentage'] = (res199['title'] / res199['title'].sum()) * 100
res199.columns = ['title', 'num', 'percentage']
res199.sort_values(by='num', ascending=False, inplace=True)
# res199.to_excel('./step3-1.xlsx')
print(res199)

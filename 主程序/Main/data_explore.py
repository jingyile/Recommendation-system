# Author：jingyile
# Data:2020/3/21 下午1:50
# Des:数据探索可视化

import pandas as pd
data = pd.read_csv('all_data.csv', encoding='utf-8', low_memory=False)
print(data['fullURLId'].count())
# =====数据探索:不同类型的网页访问次数====
print('101(咨询相关):',data['fullURLId'].apply(str).str.contains('101').sum())
print('199(其他类型):',data['fullURLId'].apply(str).str.contains('199').sum())
print('107(知识相关):',data['fullURLId'].apply(str).str.contains('107').sum())
print('301(法律法规):',data['fullURLId'].apply(str).str.contains('301').sum())
print('102(律师相关):',data['fullURLId'].apply(str).str.contains('102').sum())
print('106(律师事务所):',data['fullURLId'].apply(str).str.contains('106').sum())
print('103(律师访谈相关):',data['fullURLId'].apply(str).str.contains('103').sum())
#
# # ===101类型网址数据探索
# index101 = data['fullURLId'].apply(str).str.contains('101')
# print('101003子类型：',sum(data.loc[index101, 'fullURLId'] == 101003))
#
#
# ===107类型网页探索
index107 = data['fullURLId'].apply(str).str.contains('107')

# ===199类型网址数据探索
index199 = data['fullURLId'].apply(str).str.contains('199')
print('199带?的总数：',data.loc[index199, 'fullURL'].str.contains('\?').sum())
data = data[~data['fullURL'].str.contains('\?')] # 把带?的去掉 不然会干扰后面的统计...
print('199法律法规的总数：',data.loc[index199, 'fullURL'].str.contains('faguizt').sum())
print('199咨询相关的总数：',data.loc[index199, 'fullURL'].str.contains('ask').sum())
# print('快车-律师助手：',data.loc[index199, 'pageTitle'].str.contains('法律快车-律师助手').sum())
# print('咨询发布成功：',data.loc[index199, 'pageTitle'].str.contains('咨询发布成功').sum())
# print('法律快搜：',data.loc[index199, 'pageTitle'].str.contains('法律快搜').sum())

# ===用户点击次数数据探索
# a = data['realIP'].apply(str).value_counts()
# print('点击数　用户比例')
# print(a.value_counts(normalize=True))


# ===网页点击次数
data = data.loc[data['fullURL'].str.contains('\.html')]   # 只统计有效网址...
data = data.loc[data['fullURL'].str.contains('hunyin')]   # 只看婚姻相关的...
print(data['fullURL'].value_counts())  # 统计热门网址

# # ===同网页翻页点击数
# index = data['fullURL'].str.contains('\d_\d')
# print(data['fullURL'][index][0])



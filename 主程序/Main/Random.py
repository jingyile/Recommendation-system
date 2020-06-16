# Author：jingyile
# Data:2020/4/18 下午4:16
# Des:随机挑选用户没有产生过行为的网址生产推荐列表

from trainTestSplit import trainTestSplit
import pandas as pd
from data_process import data_process
from random import sample

data_tr, data_te = trainTestSplit(n=3)

# ===取出训练集用户的IP与浏览网址======
ipTrain = list(set(data_tr['realIP']))
urlTrain = list(set(data_tr['fullURL']))

# 构建测试集用户网址浏览字典
ipTest = list(set(data_te['realIP']))
dic_te = {ip: list(data_te.loc[data_te['realIP'] == ip, 'fullURL']) for ip in ipTest}

index = data_process()
index2 = set(index['fullURL'])  # 候选推荐网址集合  <class 'set'>
rem = pd.DataFrame(index=range(len(data_te)), columns=['IP', 'url', 'rec1', 'rec2','rec3','rec4','rec5' 'recall', 'precision'])
rem['IP'] = list(data_te['realIP'])
rem['url'] = list(data_te['fullURL'])
for i in rem.index:
    rnum = 0  # 给用户的推荐中用户真正感兴趣的个数
    anum = len(dic_te[rem.loc[i, 'IP']])  # 当前用户实际访问个数    即该用户实际感兴趣的网页个数
    if rem.loc[i, 'url'] in index2:  # 判断当前浏览网址是否在候选网址集合中
        index2.remove(rem.loc[i, 'url'])  # 在候选网页中删除当前网址，避免重复推荐
    index3 = sample(index2, 5)  # 每个用户都随机...
    rem.loc[i, 'rec1'] = index3[0]  # 推荐的网址1
    rem.loc[i, 'rec2'] = index3[1]  # 推荐的网址2
    rem.loc[i, 'rec3'] = index3[2]  # 推荐的网址3
    rem.loc[i, 'rec4'] = index3[3]  # 推荐的网址4
    rem.loc[i, 'rec5'] = index3[4]  # 推荐的网址5
    # rem.loc[i, 'T/F'] =  rem.loc[i, 'rec'] in dic_te[rem.loc[i, 'IP']]
    if rem.loc[i, 'rec1'] in dic_te[rem.loc[i, 'IP']]:
        rnum = rnum + 1
    # if rem.loc[i, 'rec2'] in dic_te[rem.loc[i, 'IP']]:  # 判定推荐是否准确
    #     rnum = rnum + 1
    # if rem.loc[i, 'rec3'] in dic_te[rem.loc[i, 'IP']]:
    #     rnum = rnum + 1
    # if rem.loc[i, 'rec4'] in dic_te[rem.loc[i, 'IP']]:
    #     rnum = rnum + 1
    # if rem.loc[i, 'rec5'] in dic_te[rem.loc[i, 'IP']]:
    #     rnum = rnum + 1
    recall = float(rnum / anum)
    rem.loc[i, 'recall'] = recall
    prec = rnum / 5
    rem.loc[i, 'precision'] = prec
# rem.to_excel('./rem_r.xlsx')
recall = sum(rem['recall'])/len(rem)
precision = sum(rem['precision'])/len(rem)
f_score = recall*precision*2/(recall+precision)
print(recall)
print(precision)
print(f_score)
p_rec = sum(rem['recall']> 0)/(len(rem))   # 或 推荐成功率，推荐的k个网址中成功被用户点击了一个或多个即可视为推荐成功！
print(p_rec)

# 按随机的推荐发现推荐的准确率极低， 因为用户喜好不能很好确定

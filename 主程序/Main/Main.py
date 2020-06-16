# Author：jingyile
# Data:2020/4/18 下午7:18
# Des: 结合推荐


from trainTestSplit import trainTestSplit
import pandas as pd
from jaccard import jaccard
from data_process import data_process
# pd.set_option('display.max_rows',100) # 行限制
# pd.set_option('display.width',1000) # 增加每行的宽度
# pd.set_option('display.max_colwidth', 100)  # 列长度

data_tr, data_te = trainTestSplit(n=3)

# ===取出训练集用户的IP与浏览网址======
ipTrain = list(set(data_tr['realIP']))
urlTrain = list(set(data_tr['fullURL']))

# ===用户物品矩阵构建========
te = pd.DataFrame(0, index=ipTrain, columns=urlTrain)
for i in data_tr.index:
    te.loc[data_tr.loc[i, 'realIP'], data_tr.loc[i, 'fullURL']] = 1
te.sum().sum()   #　同data_tr个数
# te.to_excel('./te.xlsx')


# ===构建物品相似度矩阵======
cor = jaccard(te)  # 杰卡德相似系数
cor = pd.DataFrame(cor, index=urlTrain, columns=urlTrain)
# cor.to_excel('./cor.xlsx')

# 构建测试集用户网址浏览字典
ipTest = list(set(data_te['realIP']))
dic_te = {ip: list(data_te.loc[data_te['realIP'] == ip, 'fullURL']) for ip in ipTest}

rem = pd.DataFrame(index=range(len(data_te)), columns=['IP', 'url', 'rec1','rec2','rec3','rec4','rec5','recall','precision','R','anum'])
rem['IP'] = list(data_te['realIP'])
rem['url'] = list(data_te['fullURL'])
index = data_process()['fullURL'].value_counts()
for i in rem.index:
    rnum = 0  # 给用户的推荐中用户真正感兴趣的个数
    anum = len(dic_te[rem.loc[i, 'IP']])  # 当前用户实际访问个数    即该用户实际感兴趣的网页个数
    rem.loc[i, 'anum'] = anum
    if rem.loc[i, 'url'] in urlTrain:
        rem.loc[i,'R'] = 1
        index1 = cor.loc[rem.loc[i, 'url']].argmax()
        rem.loc[i, 'rec1'] = cor.index[index1]         # 推荐的网址1
        index2 = cor.loc[rem.loc[i, 'url']].argmax()-1
        rem.loc[i, 'rec2'] = cor.index[index2]         # 推荐的网址2
        index3 = cor.loc[rem.loc[i, 'url']].argmax()-2
        rem.loc[i, 'rec3'] = cor.index[index3]         # 推荐的网址3
        index4 = cor.loc[rem.loc[i, 'url']].argmax()-3
        rem.loc[i, 'rec4'] = cor.index[index4]         # 推荐的网址4
        index5 = cor.loc[rem.loc[i, 'url']].argmax()-4
        rem.loc[i, 'rec5'] = cor.index[index5]         # 推荐的网址5
    else:
        index0 = index  # 当前用户不能干扰其与用户
        if rem.loc[i, 'url'] in index0:  # 判断当前浏览网址是否在候选网址集合中
            index3 = index0.drop(rem.loc[i, 'url'])  # 在候选网页中删除当前网址，避免重复推荐
        rem.loc[i, 'rec1'] = index0.index[0]       # 推荐的网址1
        rem.loc[i, 'rec2'] = index0.index[1]      # 推荐的网址2
        rem.loc[i, 'rec3'] = index0.index[2]       # 推荐的网址3
        rem.loc[i, 'rec4'] = index0.index[3]      # 推荐的网址4
        rem.loc[i, 'rec5'] = index0.index[4]       # 推荐的网址5
    if rem.loc[i, 'rec1'] in dic_te[rem.loc[i, 'IP']]:
        rnum = rnum + 1
    if rem.loc[i, 'rec2'] in dic_te[rem.loc[i, 'IP']]:
        rnum = rnum + 1
    if rem.loc[i, 'rec3'] in dic_te[rem.loc[i, 'IP']]:
        rnum = rnum + 1
    if rem.loc[i, 'rec4'] in dic_te[rem.loc[i, 'IP']]:
        rnum = rnum + 1
    if rem.loc[i, 'rec5'] in dic_te[rem.loc[i, 'IP']]:
        rnum = rnum + 1
    recall = float(rnum / anum)
    rem.loc[i, 'recall'] = recall
    prec = rnum / 5
    rem.loc[i, 'precision'] = prec
# rem.to_excel('./rem_M5.xlsx')
recall = sum(rem['recall'])/len(rem)
precision = sum(rem['precision'])/len(rem)
f_score = recall*precision*2/(recall+precision)
print(recall)
print(precision)
print(f_score)
p_rec = sum(rem['recall']> 0)/(len(rem))   # 或 推荐成功率，推荐的k个网址中成功被用户点击了一个或多个即可视为推荐成功！
print(p_rec)


'''
0.017936118558989158
0.31766965428937505
0.033955080888919825
0.6024327784891165
'''
'''
0.01774000213814515
0.31630695443645346
0.033595792073979065
0.6270983213429256
'''

'''
0.01915322232302623
0.3324128862590424
0.03621952035841376
0.6449704142011834
'''

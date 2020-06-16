# Author：jingyile
# Data:2020/4/10 下午2:10
# Des:基于物品的协同过滤推荐
# 缺点：不能为所浏览网页不在训练集中的用户进行推荐
# 因为协同过滤过于依赖用户的历史数据，面对新的用户或者新的物品，在开始的时候没有数据集或数据较少时，无法做出推荐。即冷启动问题


from trainTestSplit import trainTestSplit
import pandas as pd
from jaccard import jaccard

# pd.set_option('display.max_rows',100) # 行限制
# pd.set_option('display.width',1000) # 增加每行的宽度
# pd.set_option('display.max_colwidth', 100)  # 列长度

data_tr, data_te = trainTestSplit(n=3)

# ===取出训练集用户的IP与浏览网址======
ipTrain = list(set(data_tr['realIP']))
urlTrain = list(set(data_tr['fullURL']))

# 构建测试集用户网址浏览字典
ipTest = list(set(data_te['realIP']))
dic_te = {ip: list(data_te.loc[data_te['realIP'] == ip, 'fullURL']) for ip in ipTest}

# ===用户物品矩阵构建========
te = pd.DataFrame(0, index=ipTrain, columns=urlTrain)
for i in data_tr.index:
    te.loc[data_tr.loc[i, 'realIP'], data_tr.loc[i, 'fullURL']] = 1
# te.sum().sum()   #　同data_tr个数
# te.to_excel('./te.xlsx')


# ===构建物品相似度矩阵======
j_cor = jaccard(te)  # 杰卡德相似系数
cor = pd.DataFrame(j_cor, index=urlTrain, columns=urlTrain)
# cor.to_excel('./cor.xlsx')



rem = pd.DataFrame(index=range(len(data_te)), columns=['IP', 'url', 'rec1','rec2','rec3','rec4','rec5','recall','precision'])
rem['IP'] = list(data_te['realIP'])
rem['url'] = list(data_te['fullURL'])
sum_r = 0
sum_p = 0
for i in rem.index:
    if rem.loc[i, 'url'] in urlTrain:
        rnum = 0                                # 初始化
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
        anum = len(dic_te[rem.loc[i,'IP']])      # 当前用户实际访问个数    即该用户实际感兴趣的网页个数
        if rem.loc[i, 'rec1'] in dic_te[rem.loc[i, 'IP']]:
            rnum = rnum + 1
        # if rem.loc[i, 'rec2'] in dic_te[rem.loc[i, 'IP']]:
        #     rnum = rnum + 1
        # if rem.loc[i, 'rec3'] in dic_te[rem.loc[i, 'IP']]:
        #     rnum = rnum + 1
        # if rem.loc[i, 'rec4'] in dic_te[rem.loc[i, 'IP']]:
        #     rnum = rnum + 1
        # if rem.loc[i, 'rec5'] in dic_te[rem.loc[i, 'IP']]:
        #     rnum = rnum + 1
        rec = float(rnum / anum)
        rem.loc[i, 'recall'] = rec
        prec = rnum / 5
        rem.loc[i, 'precision'] = prec
        if str(rem.loc[i,'recall'])=='nan':
            continue
        else:
            sum_r = sum_r + rem.loc[i,'recall']
            sum_p = sum_p + rem.loc[i,'precision']
# rem.to_excel('./rem5.xlsx')
recall = sum_r/(len(rem) - rem['recall'].isnull().sum())
precision = sum_p/(len(rem) - rem['recall'].isnull().sum())
f_score = recall*precision*2/(recall+precision)
print(recall)
print(precision)
print(f_score)
p_rec = sum(rem['recall'] > 0)/(len(rem) - rem['recall'].isnull().sum())   # 或 推荐成功率，推荐的k个网址中成功被用户点击了一个或多个即可视为推荐成功！
print(p_rec)

















# 开始推荐,rem第一列为测试集用户IP,第二列为已浏览过网址,第三列为相应推荐网址,第四列为推荐是否有效
# rem = pd.DataFrame(index=range(len(data_te)), columns=['IP', 'url', 'rec', 'T/F'])
# rem['IP'] = list(data_te['realIP'])
# rem['url'] = list(data_te['fullURL'])
# for i in rem.index:
#     if rem.loc[i, 'url'] in urlTrain:
#         index0 = cor.loc[rem.loc[i, 'url']].argmax()
#         rem.loc[i, 'rec'] = cor.index[index0]         # 推荐的网址
#         rem.loc[i, 'T/F'] = rem.loc[i, 'rec'] in dic_te[rem.loc[i, 'IP']]   # 判定推荐是否准确
# p_rec = sum(rem['T/F'] == True)/(len(rem) - rem['T/F'].isnull().sum())
# # rem.to_excel('./rem.xlsx')
# print(p_rec)

# 25为第一个推荐成功的
# 对应excel为6969　第913　　可算是解决这个问题了！！！　开心！
# http://www.lawtime.cn/info/hunyin/lihunchengxu/20120210163620.html

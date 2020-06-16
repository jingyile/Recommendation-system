# Author：jingyile
# Data:2020/4/3 下午2:10
# Des:数据集的划分

from data_process import data_process
from random import sample
data = data_process()   # 导入经过清洗后的婚姻数据集


def trainTestSplit(data=data, n=1):
    data['realIP'] = data['realIP'].apply(str)   # 将IP地址转为字符类型

    ipCount = data['realIP'].value_counts()      # 统计每个用户的网页浏览数
    reaIP = ipCount[ipCount > n].index           # 找出浏览网页数在n次以上的用户IP
    ipTrain = sample(list(reaIP), int(len(reaIP)*0.8))       # 训练集用户
    ipTest = [i for i in list(reaIP) if i not in ipTrain]    # 测试集用户

    index_tr = [i in ipTrain for i in data['realIP']]   # 训练用户浏览记录索引
    index_te = [i in ipTest for i in data['realIP']]    # 测试用户浏览记录索引

    dataTrain = data[index_tr]     # 训练集数据
    dataTest = data[index_te]      # 测试集数据
    return dataTrain, dataTest


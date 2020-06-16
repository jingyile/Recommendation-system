# Author：jingyile
# Data:2020/4/1 下午2:03
# Des: jaccard相似系数矩阵
# 论文查重也用的这个。。？


import numpy as np


def jaccard(data=None):
    te = -(data-1)              # 将用户物品矩阵的值反转
    dot1 = np.dot(data.T, data)  # 任意两网址同时被浏览次数
    dot2 = np.dot(te.T, data)    # 任意两个网址中只有一个被浏览的次数（上三角表示前一个被浏览，下三角表示后一个被浏览）
    dot3 = dot2.T+dot2          # 任意两个网址中随意一个被浏览的次数
    cor = dot1/(dot1+dot3)      # 杰卡德相似系数公式
    for i in range(len(cor)):   # 将对角线值处理为零
        cor[i, i] = 0
    return cor

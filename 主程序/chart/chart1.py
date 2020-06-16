# Author：jingyile
# Data:2020/4/12 上午11:04
# Des: https://www.jianshu.com/p/78ba36dddad8

import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
from matplotlib.font_manager import FontProperties

plt.rcParams['axes.unicode_minus']=False     # 正常显示负号
font = FontProperties(fname='simkai.ttf', size=12)

# x = np.array(["101", "199", "107", "301", "102", "106", "103"])  # x值取默认值
# y = np.array([49.1, 25.1, 21.8, 2.2, 2.1, 0.5, 0.2])
# x = np.array(["101001", "101002", "101003", "101004", "101005", "1001006", "101007","101008","101009"])  # x值取默认值
# y = np.array([1.4, 2.0, 96.3, 0.01, 0.01, 0.01, 0.01,0.01,0.25])
# x = np.array(["知识内容页", "知识列表页", "知识首页"])  # x值取默认值
# y = np.array([89.8,5.3,4.9])
# x = np.array(["带？的网址", "法律法规相关", "咨询相关", "地区首页及其他"])  # x值取默认值
# y = np.array([32.1, 23.3, 17.8, 26.8])
x = np.array(["律师助手", "发布咨询", "咨询发布成功", "快搜","其他类型",])  # x值取默认值
y = np.array([77.1,9.5,8.1,3.0,2.3])
#
sortIndex = np.argsort(-y) # 倒序，返回排序后各数据的原始下标
#
x_sort = x[sortIndex] # 重新进行排序，与y保持初始顺序一致
y_sort = y[sortIndex] # 重新进行排序，倒序


# 定义函数来显示柱状上的数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.-0.25, 1.01*height, '%s' % float(height)+'%')


plt.xticks(np.arange(len(x_sort)), x_sort,fontproperties=font)
a = plt.bar(np.arange(len(x_sort)),y_sort,color=['r','g','b', 'c', 'm', 'y'])
autolabel(a)

plt.title('199网页中带"?"的分析结果',fontproperties=font)
plt.xlabel('网页类型', fontproperties=font)
plt.ylabel('百分比', fontproperties=font)
plt.show()




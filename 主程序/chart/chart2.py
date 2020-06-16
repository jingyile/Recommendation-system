import matplotlib.pyplot as plt
import numpy as np

# 这两行代码解决 plt 中文显示的问题
from matplotlib.font_manager import FontProperties

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
font = FontProperties(fname='simkai.ttf', size=12)
x = np.array(['1次', '2次', '3次', '4次', '5次', '6次', '7次', '大于7次'])  # x值取默认值
y1 = np.array([57.4, 19.2, 7.6, 4.4, 2.6, 1.8, 1.1, 5.9])
y2 = np.array([15.8,10.6,6.3,4.9,3.6,3.0,2.2,53.8])
#
sortIndex = np.argsort(-y1) # 倒序，返回排序后各数据的原始下标
x_sort = x
y_sort = y1

bar_width = 0.4  # 条形宽度
index1 = np.arange(len(x))  # 横坐标1
index2 = index1 + bar_width  # 横坐标2

# 定义函数来显示柱状上的数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.-0.25, 1.01*height, '%s' % float(height)+'%')


plt.xticks(np.arange(len(x_sort)), x_sort,fontproperties=font)
a = plt.bar(index1, height=y1, width=bar_width, color='r', label='User')
b = plt.bar(index2, height=y2, width=bar_width, color='b', label='Click')
autolabel(a)
autolabel(b)
plt.legend()  # 显示图例
plt.ylabel('百分比',fontproperties=font)  # 纵坐标轴标题
plt.xlabel('点击次数',fontproperties=font)  # 横坐标轴标题
plt.title('网页点击次数分析结果',fontproperties=font)  # 图形标题
plt.show()

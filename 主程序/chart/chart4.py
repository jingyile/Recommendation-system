# https://www.cnblogs.com/zyg123/p/10504633.html

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
font = FontProperties(fname='simkai.ttf', size=12)
# ItemCF
x = ['1', '2', '3', '4', '5']
y1 = [0.1164367816091953, 0.1491442542787286, 0.17567567567567569, 0.14030456852791879, 0.288161715]
# Random
y2 = [0.0044628149969272,0.00232896652110625, 0.01397712833545108, 0.085046618, 0.0055385779122541605]
# Popular
y3 = [0.31124260355029585, 0.41124260355029585, 0.420532081377152, 0.4811585365853658, 0.554368187]
# ItemCF + Popular
y4 = [0.32923076923076923, 0.539893617021279, 0.6270983213429256, 0.6024327784891165, 0.735504634]
plt.plot(x, y1, '--k', lw=1, zorder=1)
plt.plot(x, y2, '--k', lw=1, zorder=1)
plt.plot(x, y3, '--k', lw=1, zorder=1)
plt.plot(x, y4, '--k', lw=1, zorder=1)
plt.scatter(x, y1, marker='s', s=60,  zorder=2, label='ItemCF')
plt.scatter(x, y2, marker='x', s=60,  zorder=2, label='Random')
plt.scatter(x, y3, marker='^', s=60,  zorder=2, label='Popular')
plt.scatter(x, y4, marker='o', s=60,  zorder=2, label='ItemCF+Popular')
plt.legend(loc="upper left")
plt.xlabel('推荐个数K的取值',fontproperties=font)
plt.ylabel('推荐的成功率',fontproperties=font)
plt.show()
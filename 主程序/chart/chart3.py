# https://www.cnblogs.com/zyg123/p/10504633.html

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname='simkai.ttf', size=12)
# ItemCF
x1 = [0.012122019, 0.018369707102824, 0.0137569753056588, 0.016248132859807994, 0.020209654710842927]
y1 = [0.0264367816091953, 0.0397463002114164, 0.0644007155635062, 0.02030456852791879, 0.03059360730593604]
# Random
x2 = [0.000701523659277664, 0.00102645706459265, 0.000477738119316264, 0.001016081998649352, 0.0006437082524414378]
y2 = [0.0614628149969272, 0.00154083204930662, 0.00232896652110625, 0.0019017432646592709, 0.062360248447205384]
# Popular
x3 = [0.0820368965739335, 0.0686945814892749, 0.0801945302405581, 0.0786165059911886, 0.08954981556381748]
y3 = [0.157407407407407, 0.144459279038718, 0.140532081377152, 0.1574111675127002, 0.1803626220362616]
# ItemCF + Popular
x4 = [0.0179361185589891, 0.0203622084779577, 0.0148526899119513, 0.02057323200567526, 0.02558309874575015]
y4 = [0.317669654289375, 0.339893617021279, 0.324344112263576, 0.3303754266211612, 0.37413010590015136]
plt.plot(x1, y1, '--k', lw=1, zorder=1)
plt.plot(x2, y2, '--k', lw=1, zorder=1)
plt.plot(x3, y3, '--k', lw=1, zorder=1)
plt.plot(x4, y4, '--k', lw=1, zorder=1)
plt.legend(loc="upper left")
plt.scatter(x1, y1, marker='s', s=60,  zorder=2, label='ItemCF')
plt.scatter(x2, y2, marker='x', s=60,  zorder=2, label='Random')
plt.scatter(x3, y3, marker='^', s=60,  zorder=2, label='Popular')
plt.scatter(x4, y4, marker='o', s=60,  zorder=2, label='ItemCF+Popular')
plt.legend(loc="upper right")
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.show()
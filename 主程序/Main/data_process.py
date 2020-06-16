# Author：jingyile
# Data:2020/3/22 下午3:50
# Des:数据预处理操作:
# 非html结尾的网页，删除,带?的情况，还原！翻页网址，还原！

import pandas as pd


pd.set_option('display.max_rows',100) # 行限制
pd.set_option('display.width',1000) # 增加每行的宽度
pd.set_option('display.max_colwidth', 100)  # 列长度
# data = pd.read_csv(file, encoding=encoding, low_memory=False)


def data_process(file='all_data.csv', encoding='utf-8'):

    data = pd.read_csv('all_data.csv', encoding='utf-8', low_memory=False)
    num0 = data['fullURL'].count()
    print('原始数据：',num0)
    # 婚姻类型数据　之前27025条不同访问网址（已去重）

    # 1.律师的行为记录（通过法律快车-律师助手判断）；
    data = data[data['pageTitle'].str.contains('法律快车-律师助手') == False]
    num1 = data['fullURL'].count()
    print('当前数据：',num1,'   已清除律师助手数据', num0-num1)

    # 2.去除咨询发布成功页面(通过标题判断)
    data = data[data['pageTitle'].str.contains('咨询发布成功') == False]  # 逻辑索引！！！
    num2 = data['fullURL'].count()
    print('当前数据：', num2, '   已清除咨询发布成功数据', num1 - num2)

    # 3.中间类型网页（网址带有midques_关键字）；
    data = data[~data['fullURL'].str.contains('midques')]
    num3 = data['fullURL'].count()
    print('当前数据：', num3, '   已清除中间类型网页数据', num2 - num3)

    # 4.带？类型网页，还原其本身的网页；
    index1 = data['fullURL'].str.contains('\?')
    # print(index1.sum())
    # print(data.loc[index1, 'fullURL'].head())
    data.loc[index1, 'fullURL'] = data.loc[index1, 'fullURL'].str.replace('\?.*', '')
    # print(data.loc[index1, 'fullURL'].head())
    num4 = data['fullURL'].count()
    print('当前数据：', num3, '   已清除无法还原本身数据', num3 - num4)

    # 5.其它类别的数据（主网址不包含lawtime关键字）
    data = data[data['fullURL'].str.contains('lawtime')]
    num5 = data['fullURL'].count()
    print('当前数据：', num5, '   已清除不包含lawtime关键字数据', num4 - num5)

    # 6.网址中不包含.html行为的用户记录；即
    data = data.loc[data['fullURL'].str.contains('\.html')]
    num6 = data['fullURL'].count()
    print('当前数据：', num6, '   已清除非html类型数据', num5 - num6)

    # 7.对翻页网址进行还原
    index2 = data['fullURL'].str.contains('\d_\d+\.html')
    # print(data.loc[index2, 'fullURL'][0])
    data.loc[index2, 'fullURL'] = data.loc[index2, 'fullURL'].str.replace('_\d+\.html', '.html')
    # print(data.loc[index2, 'fullURL'][0])
    # print(data['realIP'].count())
    num7 = data['fullURL'].count()
    print('当前数据：', num7, '   已清除无法还原本身数据', num6 - num7)
    # return data

    # 取出婚姻类型数据
    index3 = data['fullURL'].str.contains('hunyin')
    data_hunyin = data.loc[index3, ['realIP', 'fullURL']]
    num_hunyin0 = len(data_hunyin)
    print('当前婚姻类型数据：', num_hunyin0, '   已清除非婚姻类型数据', num7 - num_hunyin0)
    data_hunyin.drop_duplicates(inplace=True)  # 去除重复数据
    num_hunyin1 = len(data_hunyin)
    print('当前婚姻类型数据：', num_hunyin1, '   已清除重复浏览记录数据', num_hunyin0 - num_hunyin1)
    return data_hunyin
    # return ['fullURL'].value_counts()   #统计热门..
    # 婚姻类型数据　处理后16651条不同访问网址（已去重）

    # # 取出咨询类型数据
    # index4 = data['fullURL'].str.contains('ask')
    # data_ask = data.loc[index4, ['realIP', 'fullURL']]
    # data_ask.drop_duplicates(inplace=True)
    # return data_ask


# data_process()


# Author：jingyile
# Data:2020/3/22 下午3:50
# Des:https://www.jianshu.com/p/a70554726f26

#  1.设置read_csv的dtype参数，指定字段的数据类型
# pd.read_csv(sio, dtype={"user_id": int, "username": object})
#  2.设置read_csv的low_memory参数为False
#  pd.read_csv(sio, low_memory=False})


# pd.set_option('display.max_rows',100) # 行限制
# pd.set_option('display.width',1000) # 增加每行的宽度
# pd.set_option('display.max_colwidth', 100)  # 列长度


#  召回率（Recall）指一个用户喜欢的产品被推荐的概率
#  精确率（Precision）指用户对一个被推荐物品感兴趣的可能性


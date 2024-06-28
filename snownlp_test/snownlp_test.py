# 导入pandas库，用于数据处理
import pandas as pd
# 导入SnowNLP库，用于情感分析
from snownlp import SnowNLP

# 读取酒店评论数据
hotel_comment = pd.read_excel("bg_test/data/hotel_comment.xlsx")

# 检查评论数据中是否包含未指定情感倾向的情况
hotel_comment['情感倾向'] = None

# 遍历评论数据，对每条评论进行情感分析
for index, row in hotel_comment.iterrows():
    comment = row['评论信息']
    # 初始化SnowNLP对象，处理中文文本
    s = SnowNLP(comment)
    # 获取评论的情感倾向概率
    sentiment = s.sentiments
    # 更新数据帧中对应行的情感倾向值
    hotel_comment.at[index, '情感倾向'] = sentiment

# 根据情感倾向概率，将情感分类为正向、中性或负向
hotel_comment['情感倾向'] = hotel_comment['情感倾向'].apply(lambda x : "正向" if x >= 0.6 else ("中性" if x >=0.4 else "负向"))

# 将处理后的数据保存为CSV文件
hotel_comment.to_csv("bg_test/hotel_csv/hotel_comment.csv",index=False)
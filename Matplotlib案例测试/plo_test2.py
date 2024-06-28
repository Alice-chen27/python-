import pandas as pd
import matplotlib.pyplot as plt

# 从CSV文件加载酒店数据
df = pd.read_csv('python数据处理与可视化/data/hotel.csv')

# 按酒店星级分组，计算评分的平均值
average_ratings = df.groupby('星级')['评分'].mean()

# 设置图表字体和负号显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建一个新的图形，设置大小
plt.figure(figsize=(10, 6))

# 绘制平均评分数据，使用蓝色实线和圆点标记
average_ratings.plot(marker='o', color='b', linestyle='-')

# 设置图表标题、x轴和y轴标签
plt.title('各星级酒店平均评分走势')
plt.xlabel('星级')
plt.ylabel('平均评分')

# 设置x轴标签旋转角度，使其更易阅读
plt.xticks(rotation=0)

# 开启网格线，帮助可视化分析
plt.grid(True)

# 调整布局，使其更紧凑
plt.tight_layout()

# 显示绘制的图形
plt.show()
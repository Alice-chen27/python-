# 导入pandas库，用于数据处理
import pandas as pd
# 导入pyplot子库 from matplotlib，用于数据可视化
from matplotlib import pyplot as plt
# 导入FontProperties类，用于设置字体
from matplotlib.font_manager import FontProperties

# 读取酒店数据csv文件，并删除‘商圈’列为空的行
df = pd.read_csv("python数据处理与可视化/data/hotel.csv").dropna(subset=['商圈'])

# 统计各商圈酒店数量
hotel_counts = df['商圈'].value_counts()

# 设置matplotlib字体为黑体，解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 设置两种字体，分别用于标题和标签
# font1 = FontProperties(fname=r"simhei.ttf")
# font2 = FontProperties(fname=r"msyh.ttc")

# 创建画布，设置大小为12x6
plt.figure(figsize=(12,6))
# 绘制条形图，颜色为skyblue
hotel_counts.plot(kind='bar', color='skyblue')
# 设置图表标题
plt.title('各商圈酒店总数')
# 设置x轴标签
plt.xlabel('商圈')
# 设置y轴标签
plt.ylabel('酒店总数')
# 将x轴标签旋转90度，便于阅读
plt.xticks(rotation=90)
# 调整布局，避免标签重叠
plt.tight_layout()
# 显示图表
plt.show()
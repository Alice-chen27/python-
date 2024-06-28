# 导入数据处理和可视化所需的库
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 从CSV文件加载数据
df = pd.read_csv('python数据处理与可视化/data/clean_month.csv')

# 筛选数据集中鞍山市的数据
df_anshan = df[df['city'] == '鞍山']

# 将月份列转换为datetime类型，以便进行月份的计算
df['month'] = pd.to_datetime(df['month'],format='%Y-%m').dt.month
# print(df)

# 对筛选后的鞍山市数据同样进行月份列的转换
df_anshan['month'] = pd.to_datetime(df_anshan['month'],format='%Y-%m').dt.month
# print(df_anshan)

# 按月份分组，计算平均最高温和平均最低温度
df_month_avg = df_anshan.groupby('month').agg({'avg_high_tem':'mean','avg_low_tem':'mean'}).reset_index()
# print(df_month_avg)

# 设置Seaborn的主题样式为darkgrid
sns.set_theme(style='darkgrid')
# 设置字体为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 设置绘图风格和字体大小适配论文发表
sns.set_context('paper',font_scale = 2)

# 创建一个新的图形窗口，设置大小
plt.figure(figsize=(15,10))

# 绘制平均最高气温的线图
sns.lineplot(data=df_month_avg,x='month',y='avg_high_tem', color='#CC3300', linewidth = 2, marker = 'o', label='平均最高气温')
# 绘制平均最低气温的线图
sns.lineplot(data=df_month_avg,x='month',y='avg_low_tem', color='#339999', linewidth = 2, marker = 'o', label='平均最低气温')
# 填充最高气温区域
plt.fill_between(df_month_avg['month'],df_month_avg['avg_high_tem'],color='#CC3300',alpha=0.4)
# 填充最低气温区域
plt.fill_between(df_month_avg['month'],df_month_avg['avg_low_tem'],color='#339999',alpha=0.7)

# 设置图形的标题、x轴和y轴标签
plt.title('2011-2021年月份气温均值')
plt.xlabel('月份')
plt.ylabel('气温(℃)')
# 设置x轴的刻度标签为月份的中文表示
plt.xticks(range(1,13),[f'{i:02d}月' for i in range(1,13)])
# 设置y轴的范围
plt.ylim(-5,50)
# 设置图例的位置
plt.legend(loc='upper right')
# 显示图形
plt.show()
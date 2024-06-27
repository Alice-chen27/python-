# 导入Line类，用于创建折线图
# Import the Line class for creating line charts.
from pyecharts.charts import Line

# 导入options模块，用于配置图表选项
# Import the options module for configuring chart options.
from pyecharts import options as opts

# 导入pandas库，用于数据处理
# Import the pandas library for data processing.
import pandas as pd

# 从Excel文件中读取所有数据，sheet_name=None表示读取所有工作表
# Read all data from the Excel file, with sheet_name=None to read all sheets.
all_data = pd.read_excel("bg_test/data/AllData.xlsx", sheet_name=None)

# 将所有工作表的数据合并成一个DataFrame，ignore_index=True用于重置索引
# Concatenate all worksheets' data into a single DataFrame, resetting the index with ignore_index=True.
df = pd.concat(all_data.values(), ignore_index=True)

# 将'time'列转换为datetime类型，并提取小时部分到新列'hour'
# Convert the 'time' column to datetime type and extract the hour part into a new column 'hour'.
df['hour'] = pd.to_datetime(df['time'], unit='ms').dt.hour

# 按小时分组，计算每小时的数据量，并重置索引
# Group by hour and calculate the data volume per hour, then reset the index.
hourly_data = df.groupby('hour').size().reset_index(name='count')

# 创建折线图对象
# Initialize a line chart object.
line_chart = (
    Line()
    # 添加x轴数据
    # Add x-axis data.
    .add_xaxis(hourly_data['hour'].tolist())
    # 添加y轴数据，配置非平滑曲线，标记最大值点
    # Add y-axis data, configure non-smooth curve, and mark the maximum value point.
    .add_yaxis("小时访问量", hourly_data['count'].tolist(), is_smooth=False, markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]))
    # 配置全局选项，包括标题、x轴、y轴选项
    # Set global options including title, x-axis, and y-axis options.
    .set_global_opts(
        title_opts=opts.TitleOpts(title="每小时数据总数量折线图"),
        xaxis_opts=opts.AxisOpts(type_="category", name="小时"),
        yaxis_opts=opts.AxisOpts(type_="value", name="访问量")
    )
)

# 渲染图表到HTML文件
# Render the chart to an HTML file.
line_chart.render("Line_of_China.html")
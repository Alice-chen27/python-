# 导入Bar类和options模块，用于创建柱状图和配置图例选项
# Import the Bar class and options module for creating bar charts and configuring chart legends.
from pyecharts.charts import Bar
from pyecharts import options as opts

# 导入pandas库，用于处理Excel数据
# Import the pandas library for handling Excel data.
import pandas as pd

# 从Excel文件中读取数据，sheet_name=None表示读取所有工作表
# Read data from an Excel file, where sheet_name=None indicates to read all sheets.
excel_data = pd.read_excel("bg_test/data/AllData.xlsx", sheet_name=None)

# 将所有工作表的数据合并成一个DataFrame，ignore_index=True重新编排索引
# Concatenate data from all sheets into a single DataFrame, with ignore_index=True to reset the index.
all_data = pd.concat(excel_data.values(), ignore_index=True)

# 移除'device_type'列中的前后空格，确保数据一致性
# Remove leading and trailing spaces in the 'device_type' column to ensure data consistency.
all_data['device_type'] = all_data['device_type'].str.strip()

# 按'area'和'device_type'分组，统计每组的大小（即设备数量），并重置索引
# Group by 'area' and 'device_type', count the size of each group (i.e., device counts), and reset the index.
grouped_data = all_data.groupby(['area', 'device_type']).size().reset_index(name='counts')

# 获取所有区域和设备类型的唯一值，用于后续图表的分类轴设置
# Get unique values of all areas and device types for later categorization axis settings in the chart.
areas = grouped_data['area'].unique()
device_types = grouped_data['device_type'].unique()

# 初始化柱状图对象，设置图表的宽度和高度
# Initialize a bar chart object and set the width and height of the chart.
bar = Bar(init_opts=opts.InitOpts(width="1000px", height="800px"))

# 遍历每种设备类型，为每种设备类型添加一个系列数据
# Iterate through each device type and add a series of data for each device type.
for device_type in device_types:
    device_data = grouped_data[grouped_data['device_type'] == device_type]
    # 设置x轴数据，即所有区域的名称
    # Set x-axis data, which is the list of all area names.
    bar.add_xaxis(areas.tolist())
    # 添加y轴数据，即指定设备类型在各区域的设备数量
    # Add y-axis data, which is the device count of the specified device type in each area.
    bar.add_yaxis(device_type, device_data['counts'].tolist(), stack="stack1")
    
# 设置全局选项，包括图表标题
# Set global options, including the chart title.
bar.set_global_opts(title_opts=opts.TitleOpts(title="各经济大区在不同设备类型上的访问数量"))

# 设置系列选项，隐藏标签
# Set series options to hide labels.
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

# 生成并保存图表
# Generate and save the chart.
bar.render("bg_test/html of China/Bars of China.html")
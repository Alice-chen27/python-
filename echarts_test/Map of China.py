# 导入必要的库和模块，用于数据处理和地图可视化
# Import necessary libraries and modules for data processing and map visualization
from pyecharts.charts import Map
from pyecharts import options as opts
import pandas as pd
import os

# 检查数据文件是否存在，若不存在则给出提示
# Check if the data file exists, otherwise give a prompt
if not os.path.exists("data.xlsx"):
    print("data.xlsx not found")

# 定义一个字典，用于将省份简称映射到全称，确保数据的一致性和准确性
# Define a dictionary to map province abbreviations to full names, ensuring data consistency and accuracy
province_mapping = {
    '河南': '河南省', 
    '广东': '广东省', 
    '河北': '河北省', 
    # ... (remaining mappings)
    '南海诸岛': '南海诸岛'
}

# 读取Excel文件中的所有数据表，用于后续的数据处理和分析
# Read all sheets from the Excel file for subsequent data processing and analysis
all_data = pd.read_excel("data.xlsx",sheet_name=None)

# 遍历每个数据表，将省份简称转换为全称，以统一数据格式
# Iterate through each sheet, converting province abbreviations to full names for data format unification
for sheet_name,sheet_data in all_data.items():
    sheet_data['province'] = sheet_data['province'].map(province_mapping)

# 统计每个省份出现的次数，用于制作地图可视化
# Count the occurrences of each province for map visualization
province_count = {}
for sheet_name,sheet_data in all_data.items():
    for index,row in sheet_data.iterrows():
        province = row['province']
        if pd.notna(province):
            province_count[province] = province_count.get(province,0) + 1

# 提取省份名称和对应的访问量，用于地图标记
# Extract province names and corresponding visit counts for map markers
province_list = list(province_count.keys())
count_list = list(province_count.values())

# 创建地图图表，添加数据，并配置可视化选项
# Create a map chart, add data, and configure visualization options
map_chart = (
    Map()
    .add("访问量",[list(z) for z in zip(province_list,count_list)],"China")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国省份用户访问量分布"), # Set global options including chart title
        visualmap_opts=opts.VisualMapOpts(max_=max(count_list)) # Configure visual map with maximum count
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False,formatter="{c}") # Series options: hide labels but show counts
    )
)

# 渲染地图图表，生成HTML文件
# Render the map chart and generate an HTML file
map_chart.render("Map of China.html")
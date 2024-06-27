import pandas as pd
from pyecharts.charts import Bar, Timeline
from pyecharts import options as opts

# 加载包含数据的Excel文件 (Load the Excel file containing data)
excel_file = pd.ExcelFile("bg_test/data/AllData.xlsx")

# 初始化时间线对象，用于按顺序展示多个图表 (Initialize a timeline object to sequentially display multiple charts)
timeline = Timeline()

# 遍历Excel文件中所有的工作表 (Iterate through all the sheets in the Excel file)
for sheet_name in excel_file.sheet_names:
    # 解析指定工作表的数据到DataFrame (Parse the data from the specified sheet into a DataFrame)
    df = excel_file.parse(sheet_name)
    
    # 对数据按'area'列进行分组计数，并重命名计数列为'count'后重置索引 (Group the data by 'area', count occurrences, rename the count column to 'count', and reset the index)
    data = df.groupby(['area']).size().reset_index(name="count")
    # 打印处理后的数据以供查看 (Print the processed data for inspection)

    bar = (
        Bar()  # 创建柱状图实例 (Create a bar chart instance)
        .add_xaxis(list(data['area']))  # 设置x轴数据为地区列表 (Set x-axis data as a list of areas)
        .add_yaxis(  # 添加y轴数据系列
            series_name=sheet_name,  # 系列名称为工作表名 (Series name is the sheet name)
            y_axis=list(data['count']),  # y轴数据为各地区的计数列表 (Y-axis data is a list of counts for each area)
            label_opts=opts.LabelOpts(is_show=False)  # 不显示柱状图上的标签 (Do not show labels on the bars)
        )
        .set_global_opts(  # 设置全局配置项
            title_opts=opts.TitleOpts(title=f"访问量统计 - {sheet_name}"),  # 图表标题，包含工作表名 (Chart title, including the sheet name)
            xaxis_opts=opts.AxisOpts(type_="category"),  # x轴类型设置为分类轴 (Set x-axis type as category)
            yaxis_opts=opts.AxisOpts(type_="value")  # y轴类型设置为数值轴 (Set y-axis type as value)
        )
    )

    # 将当前工作表的柱状图添加到时间轴中 (Add the current sheet's bar chart to the timeline)
    timeline.add(bar, sheet_name)

# 渲染最终的时间线图表到HTML文件 (Render the final timeline chart to an HTML file)
timeline.render("Bar of China.html")
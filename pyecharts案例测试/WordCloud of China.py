# 导入pandas库，用于数据处理和分析
# Import the pandas library for data processing and analysis
import pandas as pd

# 导入WordCloud类，用于生成词云图
# Import the WordCloud class for creating word cloud charts
from pyecharts.charts import WordCloud

# 导入options模块，用于设置图表选项
# Import the options module for setting chart options
from pyecharts import options as opts

# 导入urlparse函数，用于解析URL并提取域名
# Import the urlparse function for parsing URLs and extracting domains
from urllib.parse import urlparse

# 将所有数据表合并为一个DataFrame，忽略索引
# Concatenate all data sheets into one DataFrame, ignoring the index
all_data = pd.concat(pd.read_excel("python数据处理与可视化/data/AllData.xlsx", sheet_name=None), ignore_index=True)

# 删除url列中为空值的行
# Drop rows where the 'url' column is null
all_data = all_data.dropna(subset=['url'])

# 使用apply函数和urlparse对url列进行处理，提取域名
# Process the 'url' column using apply function with urlparse to extract domains
all_data['domain'] = all_data['url'].apply(lambda x: urlparse(str(x)).netloc)

# 计算每个域名出现的次数
# Count the occurrences of each domain
domain_counts = all_data['domain'].value_counts()

# 创建词云图对象
# Create a WordCloud chart object
wordcloud = (
    WordCloud()
    .add("", domain_counts.items(), word_size_range=[20, 100])  # 添加数据到词云，设置词的大小范围
    # Add data to the word cloud with specified word size range
    .set_global_opts(
        title_opts=opts.TitleOpts(title="不同域名的用户访问量词云")  # 设置全局标题选项
        # Set global title options
    )
)

# 生成词云图HTML文件
# Render the word cloud chart to an HTML file
wordcloud.render("python数据处理与可视化/html of China/WordCloud of China.html")
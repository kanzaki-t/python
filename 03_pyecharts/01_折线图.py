# 导入Line功能构建折线图对象
from pyecharts.charts import Line
# 导入标题设置对象
from pyecharts.options import TitleOpts

# 得到折线图的实例对象
line = Line()

# 添加x轴数据
line.add_xaxis(["中国", "美国", "日本"])

# 添加y轴数据
line.add_yaxis("GDP", [30, 20, 10])

# 全局配置
line.set_global_opts(
    # 设置标题配置
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%")
)

# 生成图标
line.render()

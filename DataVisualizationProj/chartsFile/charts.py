from pyecharts import options as opts
from pyecharts.charts import Liquid

def liquid_chart1() -> Liquid:
    c = (
        Liquid()
        .add("", [0.85])  # 这里的 0.6 是填充比例，可以根据需要调整
        .set_global_opts(title_opts=opts.TitleOpts(title="水滴图示例1"))
    )
    return c.render_embed()
def liquid_chart2() -> Liquid:
    c = (
        Liquid()
        .add("", [0.85])  # 这里的 0.6 是填充比例，可以根据需要调整
        .set_global_opts(title_opts=opts.TitleOpts(title="水滴图示例2"))
    )
    return c.render_embed()

def liquid_chart3() -> Liquid:
    c = (
        Liquid()
        .add("", [0.85])  # 这里的 0.6 是填充比例，可以根据需要调整
        .set_global_opts(title_opts=opts.TitleOpts(title="水滴图示例3"))
    )
    return c.render_embed()

print(liquid_chart3())
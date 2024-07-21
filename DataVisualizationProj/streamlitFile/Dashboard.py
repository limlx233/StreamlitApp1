# import streamlit as st
# import os
# import base64
# import streamlit.components.v1 as components

# @st.cache_data
# def load_html():
#     # 获取 file1 的路径
#     file1_path = os.path.dirname(__file__)
#     # 生成 file2 中 HTML 文件的路径
#     dashboard_html_path = os.path.join(file1_path, '../frontendFile/dashboard.html')
#     # 打开并读取 HTML 文件
#     with open(dashboard_html_path, 'r', encoding='utf-8') as HtmlFile:
#         raw_html = HtmlFile.read().encode("utf-8")
#         raw_html = base64.b64encode(raw_html).decode()
#     return raw_html

# st.title('数据看板示例(待开发)')
# st.header('下列为简单图示!', divider="rainbow")

# raw_html = load_html()
# with st.container(border=True):
#     components.iframe(f"data:text/html;base64,{raw_html}", height=1400, width=900)



import random
import streamlit as st
from streamlit_echarts import st_echarts

# 月份映射字典
MONTH_NAMES = {
    1: "一月", 2: "二月", 3: "三月", 4: "四月",
    5: "五月", 6: "六月", 7: "七月", 8: "八月",
    9: "九月", 10: "十月", 11: "十一月", 12: "十二月"
}

# 生产达成进度图
def gauge_progress(Attainment):
    return {
        "series": [
            {
                "type": 'gauge',
                "startAngle": 180,
                "endAngle": 0,
                "min": 0,
                "max": 100,
                "splitNumber": 10,
                "itemStyle": {
                    "color": '#58D9F9',
                    "shadowColor": 'rgba(0,138,255,0.45)',
                    "shadowBlur": 8,
                    "shadowOffsetX": 2,
                    "shadowOffsetY": 2
                },
                "progress": {
                    "show": True,
                    "roundCap": True,
                    "width": 12
                },
                "pointer": {
                    "icon": 'path://M2090.36389,615.30999 L2090.36389,615.30999 C2091.48372,615.30999 2092.40383,616.194028 2092.44859,617.312956 L2096.90698,728.755929 C2097.05155,732.369577 2094.2393,735.416212 2090.62566,735.56078 C2090.53845,735.564269 2090.45117,735.566014 2090.36389,735.566014 L2090.36389,735.566014 C2086.74736,735.566014 2083.81557,732.63423 2083.81557,729.017692 C2083.81557,728.930412 2083.81732,728.84314 2083.82081,728.755929 L2088.2792,617.312956 C2088.32396,616.194028 2089.24407,615.30999 2090.36389,615.30999 Z',
                    "length": '55%',
                    "width": 8,
                    "offsetCenter": [0, '5%']
                },
                "axisLine": {
                    "roundCap": True,
                    "lineStyle": {
                        "width": 12
                    }
                },
                "axisTick": {
                    "splitNumber": 2,
                    "lineStyle": {
                        "width": 2,
                        "color": '#999'
                    }
                },
                "splitLine": {
                    "distance":4,
                    "length": 6,
                    "lineStyle": {
                        "width": 2,
                        "color": '#999'
                    }
                },
                "axisLabel": {
                    "distance": 20,
                    "color": '#999',
                    "fontSize": 12
                },
                "title": {
                    "show": False
                },
                "detail": {
                    "backgroundColor": '#fff',
                    "borderColor": '#999',
                    "borderWidth": 0,
                    "width": '120%',
                    "lineHeight": 25,
                    "height": 25,
                    "borderRadius": 8,
                    "offsetCenter": [0, '35%'],
                    "valueAnimation": True,
                    "formatter": '达成率：{value}%',  # 使用字符串代替 lambda 函数
                    "rich": {
                        "value": {
                            "fontSize": 6,
                            "fontWeight": 'bolder',
                            "color": '#777'
                        },
                        "unit": {
                            "fontSize": 6,
                            "color": '#999',
                            "padding": [0, 0, -20, 10]
                        }
                    }
                },
                "data": [
                    {
                        "value": Attainment
                    }
                ]
            }
        ]
    }

# 生成折-柱混合图
def line_bar_charts(evaporation_data, precipitation_data, temperature_data):
    return {
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {
                "type": "cross",
                "crossStyle": {
                    "color": "#999"
                }
            }
        },
        "toolbox": {
            "feature": {
                "dataView": {"show": True, "readOnly": False},
                "magicType": {"show": True, "type": ["line", "bar"]},
            }
        },
        "legend": {
            "data": ["Evaporation", "Precipitation", "Temperature"]
        },
        "xAxis": [
            {
                "type": "category",
                "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                "axisPointer": {
                    "type": "shadow"
                }
            }
        ],
        "yAxis": [
            {
                "type": "value",
                "name": "Precipitation",
                "min": 0,
                "max": 250,
                "interval": 50,
                "axisLabel": {
                    "formatter": "{value} ml"
                }
            },
            {
                "type": "value",
                "name": "Temperature",
                "min": 0,
                "max": 25,
                "interval": 5,
                "axisLabel": {
                    "formatter": "{value} °C"
                }
            }
        ],
        "series": [
            {
                "name": "Evaporation",
                "type": "bar",
                "tooltip": {
                    "formatter": "{b}: {c} ml"
                },
                "data": evaporation_data
            },
            {
                "name": "Precipitation",
                "type": "bar",
                "tooltip": {
                    "formatter": "{b}: {c} ml"
                },
                "data": precipitation_data
            },
            {
                "name": "Temperature",
                "type": "line",
                "yAxisIndex": 1,
                "tooltip": {
                    "formatter": "{b}: {c} °C"
                },
                "data": temperature_data
            }
        ]
    }

# 折线-柱混合图的示例数据
evaporation_data = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
precipitation_data = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
temperature_data = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

# 堆叠柱状图示例数据
def create_dynamic_echarts_option(month_data):
    """
    根据提供的月度数据生成动态的 ECharts 配置选项。

    :param month_data: 一个字典，其中键为月份（1-12），值为该月份内的产品销量数据字典。
    :return: 配置选项字典。
    """
    # 获取所有产品
    all_products = set()
    for data in month_data.values():
        all_products.update(data.keys())
    all_products = list(all_products)

    # 初始化图表配置
    option = {
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {
                "type": "shadow"
            }
        },
        "toolbox": {
            "feature": {
                "dataView": {"show": True, "readOnly": False},
                "magicType": {"show": True, "type": ["line", "bar"]},
            }
        },
        "legend": {
            "data": []  # 自动填充图例数据
        },
        "xAxis": [
            {
                "type": "category",
                "data": ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"],
                "axisPointer": {
                    "type": "shadow"
                }
            }
        ],
        "yAxis": [
            {
                "type": "value",
                "name": "销量",
                "min": 0,
                "axisLabel": {
                    "formatter": "{value} 单位"
                }
            }
        ],
        "series": []  # 自动填充柱状图数据
    }

    # 设置图例和柱状图数据
    for product_name in all_products:
        # 创建一个包含每个月销量数据的列表，同时处理为0的情况
        product_sales = [month_data.get(month, {}).get(product_name, 0) for month in range(1, 13)]
        
        # 检查销量是否大于0
        has_sales = any(sale > 0 for sale in product_sales)
        
        if has_sales:  # 如果该产品在某个月份有销量大于0的记录
            option["legend"]["data"].append(product_name)
            option["series"].append({
                "name": product_name,
                "type": "bar",
                "stack": "总量",
                "tooltip": {
                    "formatter": "{b}: {c} 单位"
                },
                "data": product_sales,
                "label": {
                    "show": True,
                    "position": "inside",
                    "formatter": "{c}",
                    "color": "black"
                }
            })

            # 遍历每个月的数据，设置显示标签的格式
            for i, sale in enumerate(product_sales):
                if sale == 0:
                    option["series"][-1]["data"][i] = {
                        "value": sale,
                        "label": {
                            "show": False
                        }
                    }
                else:
                    option["series"][-1]["data"][i] = {
                        "value": sale,
                        "label": {
                            "show": True,
                            "formatter": "{c}"
                        }
                    }

    return option

def generate_month_data():
    """
    生成一年中每个月的产品销量数据。

    :return: 包含月份和每个月产品销量数据的字典。
    """
    month_data = {}
    for month in range(1, 13):
        month_data[month] = {}
        num_of_products = random.randint(1, 5)  # 每个月有1到5个产品
        for _ in range(num_of_products):
            product_name = f"产品 {random.randint(1, 5)}"
            product_data = random.randint(10, 60)  # 随机销量
            month_data[month][product_name] = product_data
    return month_data

# 渐变折线图
def create_gradient_line_char(data):
    """
    根据输入数据生成渐变颜色折线图的配置选项。

    :param data: 二维列表，内部包含日期和对应的值，例如 [["2000-06-05", 116], ["2000-06-06", 129], ...]
    :return: 图表的配置选项字典。
    """
    date_list = [item[0] for item in data]
    value_list = [item[1] for item in data]
    
    option = {
        "visualMap": [
            {
                "show": False,
                "type": "continuous",
                "seriesIndex": 0,
                "min": 0,
                "max": 400
            }
        ],
        "toolbox": {
            "feature": {
                "dataView": {"show": True, "readOnly": False},
                "magicType": {"show": True, "type": ["line", "bar"]},
            }
        },
        "title": {
            "left": 'center',
            "text": 'Gradient Line Chart'
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "xAxis": {
            "data": date_list
        },
        "yAxis": {},
        "series": [
            {
                "type": 'line',
                "showSymbol": False,
                "data": value_list,
                "lineStyle": {
                    "color": {
                        "type": "linear",
                        "x": 0,
                        "y": 0,
                        "x2": 1,
                        "y2": 1,
                        "global": False,
                        "colorStops": [
                            {"offset": 0, "color": "#ff0000"},  # 颜色渐变起始
                            {"offset": 1, "color": "#0000ff"}   # 颜色渐变结束
                        ]
                    }
                }
            }
        ]
    }
    
    return option

# 线型图示例数据
data1 = [
    ["2000-06-05", 116],
    ["2000-06-06", 129],
    ["2000-06-07", 135],
    ["2000-06-08", 86],
    ["2000-06-09", 73],
    ["2000-06-10", 85],
    ["2000-06-11", 73],
    ["2000-06-12", 68],
    ["2000-06-13", 92],
    ["2000-06-14", 130],
    ["2000-06-15", 245],
    ["2000-06-16", 139],
    ["2000-06-17", 115],
    ["2000-06-18", 111],
    ["2000-06-19", 309],
    ["2000-06-20", 206],
    ["2000-06-21", 137],
    ["2000-06-22", 128],
    ["2000-06-23", 85],
    ["2000-06-24", 94],
    ["2000-06-25", 71],
    ["2000-06-26", 106],
    ["2000-06-27", 84],
    ["2000-06-28", 93],
    ["2000-06-29", 85],
    ["2000-06-30", 73],
    ["2000-07-01", 83],
    ["2000-07-02", 125],
    ["2000-07-03", 107],
    ["2000-07-04", 82],
    ["2000-07-05", 44],
    ["2000-07-06", 72],
    ["2000-07-07", 106],
    ["2000-07-08", 107],
    ["2000-07-09", 66],
    ["2000-07-10", 91],
    ["2000-07-11", 92],
    ["2000-07-12", 113],
    ["2000-07-13", 107],
    ["2000-07-14", 131],
    ["2000-07-15", 111],
    ["2000-07-16", 64],
    ["2000-07-17", 69],
    ["2000-07-18", 88],
    ["2000-07-19", 77],
    ["2000-07-20", 83],
    ["2000-07-21", 111],
    ["2000-07-22", 57],
    ["2000-07-23", 55],
    ["2000-07-24", 60]
]

# 南丁格尔玫瑰饼图
def create_nightingale_chart(data):
    option = {
        'legend': {
            # 'top': 'bottom'
            'bottom': -10,
            # 'distance':10,
        },
        'toolbox': {
            'show': True,
            'feature': {
                'mark': {'show': True},
                'dataView': {'show': True, 'readOnly': False},
            }
        },
        'series': [
            {
                'name': 'Nightingale Chart',
                'type': 'pie',
                'radius': [35, 180],
                'center': ['50%', '50%'],
                'roseType': 'area',
                'itemStyle': {
                    'borderRadius': 6
                },
                'data': data
            }
        ]
    }
    return option

# 饼图示例数据
data2 = [
    {'value': 40, 'name': 'rose 1'},
    {'value': 38, 'name': 'rose 2'},
    {'value': 32, 'name': 'rose 3'},
    {'value': 30, 'name': 'rose 4'},
    {'value': 28, 'name': 'rose 5'},
    {'value': 26, 'name': 'rose 6'},
    {'value': 22, 'name': 'rose 7'},
    {'value': 18, 'name': 'rose 8'}
]



st.markdown("<h1 style='text-align: center;'>数据看板图例</h1>", unsafe_allow_html=True)
# 在 Streamlit 中展示图表
with st.container(border=True):
    st.markdown("<h2 style='text-align: center;'>达成进度图示例</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        st_echarts(options=gauge_progress(67), height="225px", key="chart1")
    with col2:
        st_echarts(options=gauge_progress(80), height="225px", key="chart2")
    with col3:
        st_echarts(options=gauge_progress(78), height="225px", key="chart3")
    st.markdown("<h2 style='text-align: center;'>折-柱混合图示例</h1>", unsafe_allow_html=True)
    st_echarts(options=line_bar_charts(evaporation_data, precipitation_data, temperature_data), height="400px")
    st.markdown("<h2 style='text-align: center;'>堆叠柱状图示例</h1>", unsafe_allow_html=True)
    # 生成一年中每个月的产品销量数据
    month_data = generate_month_data()
    # 显示图表
    st_echarts(options=create_dynamic_echarts_option(month_data), height="400px")
    st.markdown("<h2 style='text-align: center;'>渐变折线图示例</h1>", unsafe_allow_html=True)
    st_echarts(options=create_gradient_line_char(data1), height="400px")
    
    st.markdown("<h2 style='text-align: center;'>饼图示例</h1>", unsafe_allow_html=True)
    st_echarts(options=create_nightingale_chart(data2), height="400px")
    
    st.write('以上图例均为使用st_echarts实现')
    
    

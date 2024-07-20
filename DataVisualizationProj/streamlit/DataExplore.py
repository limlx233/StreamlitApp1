import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.header("数据处理工具demo")
st.subheader("说明",divider="rainbow")
with st.container(border=True):
    st.write('此应用只是一个数据处理应用示例，处理文件为`csv`文件')
    st.markdown('''
                #### 主要功能目标：
                - 数据清洗与处理:对上传数据文件通过内置功能进行处理
                - 数据的计算分析：简单聚合透视处理，生成简单数据图表
                - 清洗处理的结果能够提供下载至本地
                #### 注意事项：
                - 本应用提供了示例下载文件(下载保存路径均默认为你的浏览器下载地址)，可以点击下载再进行上传处理
                - 此应用功能基于本网站提供的示例数据，
                - 选择分类列或聚合列可以合理选择尝试，不符合处理规则的可能会报错，默认选择了分类列选 `Country`,聚合列选 `Salary`
                ''')
# 定义文件路径
file_path = os.path.dirname(__file__)
    # 生成 file2 中 HTML 文件的路径
csv_path = os.path.join(file_path, '../ResourceFiles/test.csv')

# 读取文件内容
with open(csv_path, 'rb') as file:
    file_content = file.read()

# 创建下载按钮
st.download_button(
    label="下载 test.csv",
    data=file_content,
    file_name="test.csv",
    mime="text/csv"
)

# 文件上传
uploaded_file = st.file_uploader("请选择一个CSV文件上传", type=["csv"])

if uploaded_file is not None:
    # 读取文件
    df = pd.read_csv(uploaded_file)
    
    # 显示数据框的前几行
    st.subheader('数据预览')
    st.write(df.head())
    
    # 数据描述
    st.subheader('数据描述')
    st.write(df.describe())

    # 分类汇总
    st.subheader('分类汇总')
    group_col = st.selectbox("请选择一个分类列进行汇总", df.columns, index=df.columns.get_loc('Country'))
    agg_col = st.selectbox("请选择一个聚合列进行汇总", df.columns, index=df.columns.get_loc('Salary'))
    grouped_df = df.groupby(group_col)[agg_col].sum().reset_index()
    st.write(grouped_df)

    # 绘制柱状图
    st.subheader('柱状图')
    fig, ax = plt.subplots()
    grouped_df.plot(kind='bar', x=group_col, y=agg_col, ax=ax)
    st.pyplot(fig)
    
    # 透视表
    st.subheader('透视表')
    pivot_table = pd.pivot_table(df, values=agg_col, index=group_col, aggfunc='sum')
    st.write(pivot_table)
    
    # 绘制折线图
    st.subheader('折线图')
    fig, ax = plt.subplots()
    pivot_table.plot(kind='line', ax=ax)
    st.pyplot(fig)
    
    # 绘制饼图
    st.subheader('饼图')
    fig, ax = plt.subplots()
    grouped_df.set_index(group_col).plot(kind='pie', y=agg_col, ax=ax, autopct='%1.1f%%')
    st.pyplot(fig)

else:
    st.write("请上传一个CSV文件进行分析。")


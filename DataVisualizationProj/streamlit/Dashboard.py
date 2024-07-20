import streamlit as st
import os
import base64
import streamlit.components.v1 as components

@st.cache_data
def load_html():
    # 获取 file1 的路径
    file1_path = os.path.dirname(__file__)
    # 生成 file2 中 HTML 文件的路径
    dashboard_html_path = os.path.join(file1_path, '../frontendFile/dashboard.html')
    # 打开并读取 HTML 文件
    with open(dashboard_html_path, 'r', encoding='utf-8') as HtmlFile:
        raw_html = HtmlFile.read().encode("utf-8")
        raw_html = base64.b64encode(raw_html).decode()
    return raw_html

st.title('Dashboard')
st.header('Just a test!', divider="rainbow")

raw_html = load_html()
with st.container(border=True):
    with st.spinner('加载中...'):
        components.iframe(f"data:text/html;base64,{raw_html}", height=1400, width=900)
import streamlit as st 


st.title('主页')
st.header('数据应用说明', divider="rainbow")
st.write('下列为数据应用的主要功能，待开发完善')
with st.container(border=True):
    st.subheader('数据可视化')
    st.write('数据看板提供可视化功能，目前处于待开发状态，仅实现了一些基础图表的可视化')
    st.subheader('数据处理')
    st.write('可以自定义数据处理工作流，通过上传文件进行数据处理')
    st.subheader('用户登录')
    st.write('为保护数据隐私，可以实现用户登录权限管理')

import streamlit as st 

st.set_page_config(layout='wide',initial_sidebar_state='expanded')

homepage = st.Page("streamlit/HomePage.py",title="主页",icon=":material/home:")
dashboard = st.Page("streamlit/Dashboard.py",title="数据看板",icon=":material/dashboard:")
dataexplore = st.Page("streamlit/DataExplore.py",title="数据处理",icon=":material/explore:")
login= st.Page("streamlit/login.py",title="登录",icon=":material/login:")
logout= st.Page("streamlit/logout.py",title="登出",icon=":material/logout:")


pg = st.navigation(
    {
        "主页":[homepage,dashboard,dataexplore],
        "用户信息":[login,logout],
    }
)

pg.run()
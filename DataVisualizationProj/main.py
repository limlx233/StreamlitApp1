import streamlit as st 
from streamlitFile.login_logout import login_page,logout_fuc


st.set_page_config(layout='wide',initial_sidebar_state='expanded')

homepage = st.Page("streamlitFiles/HomePage.py",title="主页",icon=":material/home:")
dashboard = st.Page("streamlitFiles/Dashboard.py",title="数据看板",icon=":material/dashboard:")
dataexplore = st.Page("streamlitFiles/DataExplore.py",title="数据处理",icon=":material/explore:")
login= st.Page(login_page,title="登录",icon=":material/login:")
logout= st.Page(logout_fuc,title="退出",icon=":material/logout:")


pg = st.navigation(
    {
        "主页":[homepage,dashboard,dataexplore,logout],
    }
)

# 读取查询参数
query_params = st.query_params
logged_in_str = query_params.get("logged_in", "false")
st.session_state.logged_in = (logged_in_str == "true")

if 'username' not in st.session_state:
    st.session_state.username = None

if st.session_state.logged_in:
    pg.run()
else:
    login_page()

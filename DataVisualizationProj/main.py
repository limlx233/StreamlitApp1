import streamlit as st 
from streamlitFile.login_logout import login_page

# 函数：重新设置页面配置
def reset_page_config(wide_mode):
    if wide_mode:
        st.set_page_config(layout='wide', initial_sidebar_state='expanded')
    else:
        st.set_page_config(layout='centered', initial_sidebar_state='collapsed')

# 函数：显示登录页面
def display_login_page():
    reset_page_config(wide_mode=False)
    login_page()

# 函数：显示导航页面
def display_navigation_page():
    reset_page_config(wide_mode=True)
    pg = st.navigation({
        "主页": [homepage, dashboard, dataexplore, logout],
    })
    pg.run()
    
def logout_fuc():
    # 清除会话状态
    st.session_state.logged_in = False
    st.session_state.username = None
    
    # 更新查询参数
    st.experimental_set_query_params(logged_in="false")  # 这行需要被修改

    # 显示登录页面
    display_login_page()

# 页面定义
homepage = st.Page("streamlitFile/HomePage.py", title="主页", icon=":material/home:")
dashboard = st.Page("streamlitFile/Dashboard.py", title="数据看板", icon=":material/dashboard:")
dataexplore = st.Page("streamlitFile/DataExplore.py", title="数据处理", icon=":material/explore:")
login = st.Page(login_page, title="登录", icon=":material/login:")
logout = st.Page(logout_fuc, title="退出", icon=":material/logout:")

# 读取查询参数
query_params = st.query_params
logged_in_str = query_params.get("logged_in", "false")
st.session_state.logged_in = (logged_in_str == "true")

if 'username' not in st.session_state:
    st.session_state.username = None

# 页面选择逻辑
if st.session_state.logged_in:
    display_navigation_page()
else:
    display_login_page()
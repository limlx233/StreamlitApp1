import streamlit as st
from db import SessionLocal, UserInfo

# 页面定义
homepage = st.Page("streamlitFile/HomePage.py", title="主页", icon=":material/home:")
dashboard = st.Page("streamlitFile/Dashboard.py", title="数据看板", icon=":material/dashboard:")
dataexplore = st.Page("streamlitFile/DataExplore.py", title="数据处理", icon=":material/explore:")
logout = st.Page("streamlitFile/logout.py", title="退出", icon=":material/logout:")

# 登录状态检查
if "user" not in st.session_state:
    st.write("请登录")
    username = st.text_input("用户名")
    password = st.text_input("密码", type="password")

    if st.button("登录"):
        db = SessionLocal()
        user = db.query(UserInfo).filter(UserInfo.usrname == username, UserInfo.usrpwd == password).first()

        if user:
            st.session_state.user = username
            st.success("登录成功！")
            st.rerun()  # 重新运行应用以更新页面

        else:
            st.error("登录失败，请重试。")

# 已登录页面
else:
    st.write(f"欢迎回来，{st.session_state.user}")
    pg = st.navigation({
        "主界面": [homepage, dashboard, dataexplore],
        # "退出登录": [logout]
    })
    pg.run()


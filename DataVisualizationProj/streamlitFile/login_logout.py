import streamlit as st
import sqlite3

# 从 Streamlit secrets 获取数据库路径
db_path = st.secrets["db_path"]

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        st.error(f"Error: {e}")
    return conn

def verify_user(username, password):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM userinfo WHERE usrname = ? AND usrpwd = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        return user
    return None

def login_page():
    st.title("登录")
    username = st.text_input("用户名")
    password = st.text_input("密码", type="password")
    if st.button("登录"):
        user = verify_user(username, password)
        if user:
            st.session_state.logged_in = True
            st.session_state.username = username
            # 设置查询参数
            st.query_params = {"logged_in": "true"}
        else:
            st.error("用户名或密码错误")

def logout_fuc():
    st.session_state.logged_in = False
    st.session_state.username = None
    # 设置查询参数
    st.query_params = {"logged_in": "false"}
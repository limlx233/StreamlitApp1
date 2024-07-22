import streamlit as st
# 退出登录按钮
if st.button("退出登录"):
    del st.session_state.user
    st.success("已成功退出登录。")

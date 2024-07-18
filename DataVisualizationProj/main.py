import streamlit as st 


homepage = st.Page("streamlit/HomePage.py",title="Home",icon=":material/home:")
dashboard = st.Page("streamlit/Dashboard.py",title="Dashboard",icon=":material/dashboard:")
login= st.Page("streamlit/login.py",title="Login",icon=":material/login:")
logout= st.Page("streamlit/logout.py",title="Logout",icon=":material/logout:")

pg = st.navigation(
    {
        "HomePage":[homepage,dashboard],
        "UserInfo":[login,logout],
    }
)

pg.run()
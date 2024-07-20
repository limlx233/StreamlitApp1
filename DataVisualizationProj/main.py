import streamlit as st 

st.set_page_config(layout='wide',initial_sidebar_state='expanded')

homepage = st.Page("streamlit/HomePage.py",title="Home",icon=":material/home:")
dashboard = st.Page("streamlit/Dashboard.py",title="Dashboard",icon=":material/dashboard:")
dataexplore = st.Page("streamlit/DataExplore.py",title="Explore",icon=":material/explore:")
login= st.Page("streamlit/login.py",title="Login",icon=":material/login:")
logout= st.Page("streamlit/logout.py",title="Logout",icon=":material/logout:")


pg = st.navigation(
    {
        "HomePage":[homepage,dashboard,dataexplore],
        "UserInfo":[login,logout],
    }
)

pg.run()
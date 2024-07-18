import streamlit as st 
from chartsFile.charts import *
# st.write('dashboard todo')

with st.container(border=True):
    st.header('Dashboard',divider='rainbow')
    col1, col2, col3 = st.columns(3,gap="medium")
    with col1:
        st.components.v1.html(liquid_chart1(), height=200)
    with col2:
        st.components.v1.html(liquid_chart2(), height=200)
    with col3:
        st.components.v1.html(liquid_chart3(), height=200)
    
    
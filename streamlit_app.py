import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título del dashboard
st.title("Dashboard de Prueba - Demo2")

# url 
pwbi_url = 'https://app.powerbi.com/reportEmbed?reportId=9c7b8761-29dd-4ac1-a4f0-3442c1207269&autoAuth=true&ctid=9c5c8662-1bf5-4e94-a820-5e3ca126f752'


st.markdown(
    f"""
    <iframe src="{pwbi_url}" 
            width="100%" 
            height="600" 
            frameborder="0" 
            allowFullScreen="true"></iframe>
    """, 
    unsafe_allow_html=True
)
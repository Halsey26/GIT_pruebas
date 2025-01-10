import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar el diseño de la página
st.set_page_config(page_title="Dashboard de Prueba - Demo2", layout="wide")

# Título del dashboard
st.title("Dashboard - Demo 2")

# Descripción introductoria
st.markdown(
    """
    Bienvenidos a nuestro **dashboard interactivo**, en el cual mostramos un análisis de datos a través de visualizaciones dinámicas. 
    """
)

# Sección: Incrustar Power BI
st.header("📊 Informe Power BI")
st.markdown(
    """
    A continuación, puedes visualizar el informe interactivo de Power BI. 
    Si deseas abrirlo en una nueva pestaña, [haz clic aquí](https://app.powerbi.com/view?r=eyJrIjoiZGJhNTIwZmEtNmExYi00ZTg1LTlmNDgtMzU0YWJiMjI0ZTZhIiwidCI6IjljNWM4NjYyLTFiZjUtNGU5NC1hODIwLTVlM2NhMTI2Zjc1MiIsImMiOjR9&pageName=455fbd065761d7b4d03f).
    """
)

# Insertar Power BI como iframe
pwbi_url = 'https://app.powerbi.com/view?r=eyJrIjoiZGJhNTIwZmEtNmExYi00ZTg1LTlmNDgtMzU0YWJiMjI0ZTZhIiwidCI6IjljNWM4NjYyLTFiZjUtNGU5NC1hODIwLTVlM2NhMTI2Zjc1MiIsImMiOjR9&pageName=455fbd065761d7b4d03f'
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


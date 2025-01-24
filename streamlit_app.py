import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar el diseño de la página
st.set_page_config(page_title="Dashboard de Prueba - Demo2", layout="wide")

import streamlit as st

# Título del proyecto y dashboard
st.markdown("# 📊 Análisis Estratégico de Restaurantes en los Estados Unidos")

# Introducción
st.markdown("""
            -------
            Este dashboard ofrece un análisis detallado de los restaurantes, puntuaciones de usuarios y categorías más populares en diferentes condados y ciudades. 
            A través de gráficos y KPI, se identifican tendencias clave y áreas estratégicas para la toma de decisiones empresariales.
            -------
            """)

# Texto complementario
st.markdown("""
            El análisis se divide en tres hojas principales:  
            - **Hoja 2:** KPI de puntuaciones y análisis temporal por ciudad y condado.  
            - **Hoja 3:** Análisis de categorías y distribución de restaurantes.  
            - **Hoja 4:** Identificación de nichos relevantes para oportunidades de negocio.
            """)

# URL del Power BI
pbi_url = "https://app.powerbi.com/view?r=eyJrIjoiMDQ4MTRiZjMtMzA2ZS00MTEwLThhM2QtMmFmMzBkMjkzZjA0IiwidCI6IjljNWM4NjYyLTFiZjUtNGU5NC1hODIwLTVlM2NhMTI2Zjc1MiIsImMiOjR9&pageName=7701e774ca2abe2e8050"

st.components.v1.iframe(src=pbi_url, width=1000, height=700, scrolling=True)

# Conclusiones
st.markdown("## Conclusiones del Análisis")
st.markdown("""
            -------
            **Principales Insights:**  
            - Los condados con mayor cantidad de restaurantes tienden a tener puntuaciones promedio más altas.  
            - Las categorías más populares son clave para identificar tendencias de mercado.  
            - Las ciudades con pocos restaurantes y puntuaciones excelentes representan oportunidades de expansión.  
            -------
            """)

# # Botón para cambiar de página
# if st.button("Modelos", type='tertiary', icon="➡️", use_container_width=True):
#     st.switch_page("02_Asistente_de_predicción.py")



# # Título del dashboard
# st.title("Dashboard - Demo 2")

# # Descripción introductoria
# st.markdown(
#     """
#     Bienvenidos a nuestro **dashboard interactivo**, en el cual mostramos un análisis de datos a través de visualizaciones dinámicas. 
#     """
# )

# # Sección: Incrustar Power BI
# st.header("📊 Informe Power BI")
# st.markdown(
#     """
#     A continuación, puedes visualizar el informe interactivo de Power BI. 
#     Si deseas abrirlo en una nueva pestaña, [haz clic aquí](https://app.powerbi.com/view?r=eyJrIjoiZGJhNTIwZmEtNmExYi00ZTg1LTlmNDgtMzU0YWJiMjI0ZTZhIiwidCI6IjljNWM4NjYyLTFiZjUtNGU5NC1hODIwLTVlM2NhMTI2Zjc1MiIsImMiOjR9&pageName=455fbd065761d7b4d03f).
#     """
# )

# # Insertar Power BI como iframe
# pwbi_url = 'https://app.powerbi.com/view?r=eyJrIjoiZGJhNTIwZmEtNmExYi00ZTg1LTlmNDgtMzU0YWJiMjI0ZTZhIiwidCI6IjljNWM4NjYyLTFiZjUtNGU5NC1hODIwLTVlM2NhMTI2Zjc1MiIsImMiOjR9&pageName=455fbd065761d7b4d03f'
# st.markdown(
#     f"""
#     <iframe src="{pwbi_url}" 
#             width="100%" 
#             height="600" 
#             frameborder="0" 
#             allowFullScreen="true"></iframe>
#     """, 
#     unsafe_allow_html=True
# )


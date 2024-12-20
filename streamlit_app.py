import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título del dashboard
st.title("Dashboard de Prueba - Análisis Exploratorio")

# url 
pwbi_url = 'https://app.powerbi.com/view?r=eyJrIjoiZGI0ODNmZjQtYjZlNi00N2Q2LTg1NWItMzFiY2ViYWNkOGE3IiwidCI6IjljNWM4NjYyLTFiZjUtNGU5NC1hODIwLTVlM2NhMTI2Zjc1MiIsImMiOjR9&pageName=8cca638c5e039beccdf0'

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


''' 
# Carga de datos
uploaded_file = st.file_uploader('restaurantes csv/restaurantes_2024.csv', type="csv")

if uploaded_file:
    # Leer los datos
    df = pd.read_csv(uploaded_file)

    # Mostrar los datos
    st.write("Vista previa de los datos:")
    st.dataframe(df.head(5))

    # grafica
    # Título del dashboard
    st.title("Distribución de Puntuaciones de Usuarios")
    año= 2024
    # Gráfico de Seaborn
    st.write(f"Gráfico de la distribución de puntuaciones de usuarios en el año {año}")
    fig, ax = plt.subplots()
    sns.histplot(df['puntuacion_usuarios'], kde=True, color='purple', label=f'Puntuación usuarios ({año})', ax=ax)
    ax.set_title(f'Distribución de Puntuaciones Usuarios en {año}')
    ax.set_xlabel('Puntuación')
    ax.set_ylabel('Frecuencia')
    ax.legend()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

    # grafica 2
    # Filtrar el DataFrame para la ciudad de Miami y el año 2024
    año = 2024
    st.title(f"Categorías más populares en Miami {año}")
    
    
    df_miami = df[df['ciudad'].str.lower() == 'miami']

    # Procesar las categorías
    categorias = df_miami['categories'].apply(lambda x: x.split(', ') if isinstance(x, str) else [])
    full_categorias = categorias.explode().value_counts().reset_index()
    full_categorias.columns = ['categoria', 'cantidad_restaurantes']

    # Obtener las 10 categorías principales
    top_categorias = full_categorias.sort_values(by='cantidad_restaurantes', ascending=False).head(10)

    # Visualización con Matplotlib
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.barh(top_categorias['categoria'], top_categorias['cantidad_restaurantes'], color='chocolate', edgecolor='k')
    ax.set_title(f'Top 10 Categorías de Restaurantes en Miami ({año})', fontsize=16)
    ax.set_xlabel('Frecuencia', fontsize=14)
    ax.set_ylabel('Categoría', fontsize=14)
    ax.invert_yaxis()
    plt.tight_layout()

    # Mostrar gráfico en Streamlit
    st.pyplot(fig)





'''
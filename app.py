import streamlit as st

# Configuración de la aplicación
st.set_page_config(
    page_title="Encuesta de Registro",
    page_icon="📝",
    layout="centered"
)

st.title("Encuesta de Registro")

# URL del Google Form
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSc1PGpaEm37ns8m-aXN0XJx03FLLphVGIXY_7N_xPLO0_hC-A/viewform?usp=sf_link"

# Estilos CSS para las franjas y la barra
st.markdown("""
    <style>
        .barra {
            background-color: rgba(255, 255, 255, 0.8);  /* Color blanco con opacidad */
            height: 50px; /* Altura de la barra */
            position: absolute;
            top: 20px; /* Espacio desde la parte superior */
            left: 0;
            right: 0;
            z-index: 2;  /* Asegúrate de que esté encima del iframe */
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px; /* Tamaño de la fuente */
            font-weight: bold; /* Negrita */
        }
        .iframe-container {
            position: relative;
            z-index: 0;  /* Coloca el iframe detrás de las franjas */
            height: calc(100vh - 50px); /* Ajustar altura del iframe para que quede debajo de la barra */
            overflow: hidden; /* Oculta cualquier desbordamiento */
        }
        iframe {
            width: 100%;
            height: 100%;
            border: none; /* Eliminar borde */
        }
    </style>
""", unsafe_allow_html=True)

# Barra que cubre un poco el iframe
st.markdown('<div class="barra">Tu Mensaje Aquí</div>', unsafe_allow_html=True)

# Incrustar el formulario usando iframe
st.markdown(
    '<div class="iframe-container">'
    f'<iframe src="{form_url}">Cargando…</iframe>'
    '</div>',
    unsafe_allow_html=True
)

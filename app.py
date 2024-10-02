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

# Estilos CSS para la barra y el iframe
st.markdown("""
    <style>
        .barra {
            background-color: #ffffff;  /* Color blanco sólido */
            height: 100px; /* Aumentar altura de la barra */
            position: absolute;
            top: 0; /* La barra ahora está en la parte superior */
            left: 0;
            right: 0;
            z-index: 2;  /* Asegúrate de que esté encima del iframe */
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px; /* Aumentar tamaño de la fuente */
            font-weight: bold; /* Negrita */
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Sombra opcional para efecto */
        }
        .iframe-container {
            position: relative;
            z-index: 0;  /* Coloca el iframe detrás de la barra */
            height: calc(100vh - 100px); /* Ajustar altura del iframe para que ocupe el resto de la pantalla */
        }
        iframe {
            width: 100%;
            height: 100%; /* Asegurar que el iframe ocupe el 100% de la altura */
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

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

# Estilos CSS para las franjas
st.markdown("""
    <style>
        .franja-superior, .franja-inferior {
            background-color: rgba(255, 255, 255, 1);  /* Color blanco */
            height: 100px; /* Altura de las franjas */
            position: absolute;
            left: 0;
            right: 0;
            z-index: 1;  /* Asegúrate de que se superpongan al iframe */
        }
        .franja-superior {
            top: 0;  /* Posiciona la franja superior en la parte superior */
        }
        .franja-inferior {
            bottom: 0;  /* Posiciona la franja inferior en la parte inferior */
        }
        .iframe-container {
            position: relative;
            z-index: 0;  /* Coloca el iframe detrás de las franjas */
            height: calc(100vh - 200px); /* Ajustar altura del iframe para que quede entre las franjas */
            overflow: hidden; /* Oculta cualquier desbordamiento */
        }
        iframe {
            width: 100%;
            height: 100%;
            border: none; /* Eliminar borde */
        }
    </style>
""", unsafe_allow_html=True)

# Franjas superiores e inferiores
st.markdown('<div class="franja-superior"></div>', unsafe_allow_html=True)
st.markdown('<div class="franja-inferior"></div>', unsafe_allow_html=True)

# Incrustar el formulario usando iframe
st.markdown(
    '<div class="iframe-container">'
    f'<iframe src="{form_url}">Cargando…</iframe>'
    '</div>',
    unsafe_allow_html=True
)

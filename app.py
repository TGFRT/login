import streamlit as st

# Configuración de la aplicación
st.set_page_config(
    page_title="Encuesta de Registro",
    page_icon="📝",
    layout="centered"
)

st.title("Encuesta de Registro")

# URL del Google Form
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSc1PGpaEm37ns8m-aXN0XJx03FLLphVGIXY_7N_xPLO0_hC-A/viewform?embedded=true"

# Estilos CSS para las franjas
st.markdown("""
    <style>
        .franja-superior, .franja-inferior {
            background-color: rgba(255, 152, 0, 0.8);  /* Color naranja con transparencia */
            height: 50px; /* Altura de las franjas */
            position: relative;
            z-index: 1;  /* Para asegurarse de que se superponga al iframe */
        }
        .iframe-container {
            position: relative;
            z-index: 0;  /* Para colocar el iframe detrás de las franjas */
        }
    </style>
""", unsafe_allow_html=True)

# Franjas superiores e inferiores
st.markdown('<div class="franja-superior"></div>', unsafe_allow_html=True)

# Incrustar el formulario usando iframe
st.markdown(
    '<div class="iframe-container">'
    f'<iframe src="{form_url}" width="640" height="982" frameborder="0" marginheight="0" marginwidth="0">Cargando…</iframe>'
    '</div>',
    unsafe_allow_html=True
)

# Franjas inferiores
st.markdown('<div class="franja-inferior"></div>', unsafe_allow_html=True)

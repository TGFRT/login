import streamlit as st

# Configuración de la aplicación
st.set_page_config(
    page_title="Encuesta de Registro",
    page_icon="📝",
    layout="centered"
)

st.title("Encuesta de Registro")

# URL del Google Form (modificada para incrustar)
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSc1PGpaEm37ns8m-aXN0XJx03FLLphVGIXY_7N_xPLO0_hC-A/viewform?embedded=true"

# Incrustar el formulario usando iframe
st.markdown(f'<iframe src="{form_url}" width="640" height="982" frameborder="0" marginheight="0" marginwidth="0">Cargando…</iframe>', unsafe_allow_html=True)

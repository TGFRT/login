import streamlit as st
import pandas as pd

# Configuración de la aplicación
st.set_page_config(
    page_title="Registro de Cuenta",
    page_icon="📝",
    layout="centered"
)

# URL de la hoja de cálculo pública
url = 'https://docs.google.com/spreadsheets/d/1iMETFXotBdj_PUyln5LOMfiyR-Fhn2jeUaEifCErXkU/edit?gid=0#gid=0'

# Cargar datos existentes
dfUsuarios = pd.read_csv(url)

# Estilos CSS para mejorar el diseño
st.markdown("""<style>
    body {
        background-color: #f0f2f5;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        margin: 0;
    }
    .register-form {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 30px;
        width: 300px;
        background: white;
        border-radius: 10px;
    }
    .register-form h2 {
        margin-bottom: 20px;
        color: #ff9800;
        text-align: left;
    }
    .register-form input {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    .register-form button {
        background-color: #ff9800;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .register-form button:hover {
        background-color: #fb8c00;
    }
</style>""", unsafe_allow_html=True)

# Sección de registro
st.markdown("<div class='register-form'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: left;'>Crear Cuenta ⭐</h2>", unsafe_allow_html=True)

nombre = st.text_input("Nombre:")
celular = st.text_input("Número de Celular:")
contrasena = st.text_input("Contraseña:", type="password")

if st.button("Registrar"):
    # Verificar si el celular ya está registrado
    if celular in dfUsuarios['celular'].values:
        st.error("Este número de celular ya está registrado.", icon="❌")
    else:
        # Agregar el nuevo usuario a la hoja (esto requiere lógica para manejar CSV)
        new_row = pd.DataFrame([[nombre, celular, contrasena]], columns=['nombre', 'celular', 'contrasena'])
        new_row.to_csv(url, mode='a', header=False, index=False)  # Asegúrate de que esto funcione para tu configuración
        st.success("Cuenta creada exitosamente!")

st.markdown("</div>", unsafe_allow_html=True)

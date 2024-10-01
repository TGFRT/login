import streamlit as st
import pandas as pd
import os

# Configuración de la aplicación
st.set_page_config(
    page_title="Registro de Cuenta",
    page_icon="📝",
    layout="centered"
)

# Ruta del archivo CSV
csv_file_path = 'usuarios.csv'

# Cargar datos existentes
if os.path.exists(csv_file_path):
    dfUsuarios = pd.read_csv(csv_file_path)
else:
    dfUsuarios = pd.DataFrame(columns=['nombre', 'celular', 'contrasena'])

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
        # Agregar el nuevo usuario al DataFrame
        new_user = pd.DataFrame([[nombre, celular, contrasena]], columns=['nombre', 'celular', 'contrasena'])
        dfUsuarios = pd.concat([dfUsuarios, new_user], ignore_index=True)
        
        # Guardar en el archivo CSV
        dfUsuarios.to_csv(csv_file_path, index=False)
        st.success("Cuenta creada exitosamente!")

st.markdown("</div>", unsafe_allow_html=True)

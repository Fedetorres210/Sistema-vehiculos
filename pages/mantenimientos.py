import streamlit as st

st.set_page_config(
    page_title="Mantenimientos",
    page_icon="🚑",
    layout="wide")


st.title("Bienvenido a la seccion de Mantenimientos")
st.image("https://tallerexitoso.com/wp-content/uploads/2022/12/mejorar-taller-mecanico.jpg")

consulta = st.sidebar.selectbox("Selecciona la opcion que deseas",["Resumen","Registro de Mantenimiento", "Registro de Taller","Consulta de Mantenimientos","Edicion de mantenimientos"])

if consulta == "Registro de Mantenimiento":
    vehiculo = st.selectbox("Selecciona el vehiculo al que le hiciste el mantenimiento",[1,2,3])
    taller = st.selectbox("Selecciona el taller donde realizaste el mantenimiento",[1,2,3])
    nombre = st.text_input("Ingresa el mantenimiento que realizaste")
    descripcion = st.text_area("Ingresa la descripcion del mantenimiento")
    costo = st.number_input("Ingresa el costo del mantenimiento")
    kilometraje = st.number_input("Ingresa el kilometraje del vehiculo")
    fechaEntrada = str(st.date_input("Ingresa la fecha de ingreso del vehiculo al taller"))
    fechaSalida = str(st.date_input("Ingresa la fecha salida del taller"))




import streamlit as st
from logica import Conductor
from config import obtenerConductores,insertarCondcutor,obtenerConductor


st.set_page_config(
    page_title="Inicio",
    page_icon="",
    layout="wide")
st.title("Bienvenido al sistema de vehiculos!")
st.text("Este sistema fue desarrollado en su totalidad por T-Rento,para la gestión efectiva de los vehiculos de la")
st.text("empresa.")
st.image("https://img.freepik.com/vector-gratis/genial-pack-diferentes-tipos-vehiculos-dibujos-animados_23-2147610327.jpg")
st.title("Manual de Usuario")
st.subheader("Páginas")
st.text("Dentro de este sistema se encuentra las paginas del sistema, estas se dividen en: Pagos, talleres, vehiculos,mantenimientos y conductores. Cada página te permite acceder a un elemento distinto de los diferentes aspectos del sistema.")



st.image("https://imgur.com/j5s52Hm.jpeg")













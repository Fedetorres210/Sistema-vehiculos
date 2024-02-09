import streamlit as st
import pandas as pd
from logica import Mapa, Taller
from config import obtenerTallers,registrarTaller,obtenerTaller,editarTaller
consulta = st.sidebar.selectbox("Selecciona la opcion que deseas",["Resumen","Registro de Taller","Edicion de Taller","Consulta de Taller"])

st.title("Bienvenido a la seccion de talleres")
st.image("https://media.es.wired.com/photos/635800d4aeb677295fc63673/16:9/w_2560%2Cc_limit/Computerized-Cars-Killing-Auto-Repair-Shops-Business-1333765701.jpg")


if consulta == "Registro de Taller":
    nombre = st.text_input("Ingrese el nombre del taller")
    direccion = st.text_input("Ingrese los datos de la direccion del taller")
    mapa = Mapa()
    result = mapa.autocomplete_address(direccion)
    ubicacion = st.selectbox("Seleccione el punto más cercano de la dirección del taller", result)
    telefono1 = st.text_input("Ingrese el número 1 de telefono del taller")
    telefono2 = st.text_input("Ingrese el número  2 de telefono del taller")
    registrar = st.button("Registrar")
    if registrar:
        taller = Taller(nombre,ubicacion,telefono1,telefono2)
        registrarTaller(taller.generarDatosCsv())


if consulta == "Consulta de Taller":
    taller = st.selectbox("Selecciona el taller que deseas ver",[elem["Nombre"] for elem in obtenerTallers()])
    tallerSeleccionado = obtenerTaller({"Nombre":taller})
    df = pd.DataFrame(tallerSeleccionado) 
    df = df.drop("_id",axis=1)
    st.data_editor(df,hide_index=True)


if consulta == "Edicion de Taller":
    taller =st.selectbox("Seleccione el taller a editar",[elem["Nombre"] for elem in obtenerTallers()])
    tallerSeleccionado = obtenerTaller({"Nombre":taller})
    nombre = st.text_input("Ingrese el nuevo nombre del taller",value=tallerSeleccionado[0]["Nombre"])
    direccion = st.text_input("Ingrese los nuevos datos de la direccion del taller",value=tallerSeleccionado[0]["Ubicacion"])
    mapa = Mapa()
    result = mapa.autocomplete_address(direccion)
    ubicacion = st.selectbox("Seleccione el nuevo punto más cercano de la dirección del taller", result)
    telefono1 = st.text_input("Ingrese el nuevo número 1 de telefono del taller",value=tallerSeleccionado[0]["Telefono 1"])
    telefono2 = st.text_input("Ingrese el nuevo número  2 de telefono del taller",value=tallerSeleccionado[0]["Telefono 2"])
    editar = st.button("Editar")
    if editar:
        taller = Taller(nombre,ubicacion,telefono1,telefono2)
        editarTaller(tallerSeleccionado[0],{"$set":taller.generarDatosCsv()})

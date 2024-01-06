import streamlit as st
from logica import Conductor
from config import obtenerConductores,insertarCondcutor,obtenerConductor

menu = st.sidebar.selectbox("Seleccione la pagina que desea:", ["Resumen Mensual","Conductores","Vehiculos","Pagos"])

if (menu== "Conductores"):
    st.header("Bienvenido a la seccion de conductores")
    st.image("https://www.emagister.com/blog/wp-content/uploads/2019/04/ch%C3%B3fer-privado.jpg")
    opcionConductores = st.selectbox("Seleccione la accion por realizar",["Resumen","Registro de Conductor", "Consulta de informacion de conductor", "Registro de incidentes","Consulta de incidentes"])

    if (opcionConductores== "Resumen"):
        conductores = obtenerConductores()
        st.table(conductores)


    if (opcionConductores== "Registro de Conductor"):
        st.subheader("Bienvenido al registro de conductor")
        nombre = st.text_input("Nombre del conductor")
        apellido = st.text_input("Apellido del conductor")
        cedula = st.text_input("Cedula del conductor")
        fotoCedula = st.text_input("Ingrese el link de la foto de la cedula")
        licencia = st.text_input("Numero de licencia")
        fotoLicencia = st.text_input("Ingrese el link de la foto licencia")
        direccion = st.text_input("Direccion")
        vehiculo = st.selectbox("Vehiculo Otorgado", [1,2,3,4])
        fotoConductor = st.text_input("Link del foto del conductor")

        registrar = st.button("Registrar Conductor")

        if (registrar):
            try:
                nuevoConductor = Conductor(nombre, apellido, cedula, licencia, direccion, vehiculo, fotoConductor,fotoCedula, fotoLicencia)
                insertarCondcutor(nuevoConductor.generarDatosCsv())
                st.success("Nuevo Conductor Insertado!")
            except:
                st.warning("Ha ocurrido un fallo con la insercion del usuario")

    if (opcionConductores== "Consulta de informacion de conductor"):
        conductores = [(elem["Nombre"] + " " + elem["Apellido"]) for elem in obtenerConductores()]
        conductoresApellido = [elem["Apellido"] for elem in obtenerConductores()]
        conductorSeleccionado = st.selectbox("Seleccione el Nombre del Conductor al cual desea ver la informacion", conductores).split()
        datosConductor = [elem for elem in obtenerConductor({"Nombre": conductorSeleccionado[0], "Apellido":conductorSeleccionado[1]})]
        st.table(datosConductor)
        st.image(datosConductor[0]["FotoCedula"])

















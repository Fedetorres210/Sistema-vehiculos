import streamlit as st
from config import obtenerVehiculos,obtenerVehiculo,registrarMantenimiento,obtenerMantenimientos,obtenerMantenimiento,actualizarMantenimiento
from logica import Mantenimiento, Mapa, Incidente
import pandas as pd

st.set_page_config(
    page_title="Mantenimientos",
    page_icon="🚑",
    layout="wide")


st.title("Bienvenido a la seccion de Mantenimientos")
st.image("https://tallerexitoso.com/wp-content/uploads/2022/12/mejorar-taller-mecanico.jpg")

consulta = st.sidebar.selectbox("Selecciona la opcion que deseas",["Resumen","Registro de Mantenimiento","Consulta de Mantenimientos","Edicion de mantenimientos"])

if consulta == "Registro de Mantenimiento":
    
    vehiculoSeleccionado = st.selectbox("Selecciona el vehiculo al que le hiciste el mantenimiento",[elem["Placa"] for elem in obtenerVehiculos()])
    vehiculo = obtenerVehiculo({"Placa":vehiculoSeleccionado})
    taller = st.selectbox("Selecciona el taller donde realizaste el mantenimiento",[1,2,3])
    nombre = st.text_input("Ingresa el mantenimiento que realizaste")
    descripcion = st.text_area("Ingresa la descripcion del mantenimiento")
    costo = st.number_input("Ingresa el costo del mantenimiento")
    kilometraje = st.number_input("Ingresa el kilometraje del vehiculo")
    fechaEntrada = str(st.date_input("Ingresa la fecha de ingreso del vehiculo al taller"))
    fechaSalida = str(st.date_input("Ingresa la fecha salida del taller"))
    calificacion = st.select_slider("Ingresa una calificación al mantenimiento",[elem for elem in range(0,11)])
    registrar = st.button("Registrar")
    if registrar:
        mantenimiento = Mantenimiento(vehiculo[0],taller,nombre,descripcion,costo,kilometraje,fechaEntrada,fechaSalida,calificacion)
        registrarMantenimiento(mantenimiento.generarDatosCsv())


if consulta == "Consulta de Mantenimientos":
    consultaMantenimiento = st.selectbox("Seleccione el tipo de consulta",["General","Periodica","Por vehiculo","Por taller"])

    if consultaMantenimiento == "General":
        mantenimientos = [elem for elem in obtenerMantenimientos()]
        vehiculos = [elem.pop("Vehiculo") for elem in mantenimientos]
        dataMantenimientos = pd.DataFrame(mantenimientos)
        dataMantenimientos = dataMantenimientos.drop("_id",axis=1)
        
        vehiculos = pd.DataFrame(vehiculos)
        vehiculos = vehiculos.drop("Bitacora Conductores",axis=1)
        vehiculos = vehiculos.drop("_id",axis=1)
        vehiculos = vehiculos.drop("Especificaciones",axis=1)
        vehiculos = vehiculos.drop("Conductor",axis=1)
        df =  pd.concat([dataMantenimientos,vehiculos],axis=1)
        st.data_editor(df,column_config={"Foto Dekra": st.column_config.ImageColumn(), "Foto Marchamo": st.column_config.ImageColumn(), "Foto Vehiculo": st.column_config.ImageColumn()}, hide_index=True)
        
    if consultaMantenimiento == "Periodica":
        opcion = st.selectbox("Selecciona la opción que deseas:",["Fecha inicio", "Fecha Fin", "Mensual"])
        if opcion == "Fecha inicio":
            fecha = str(st.date_input("Ingresa la fecha inicio del mantenimiento"))
            mantenimientos = [elem for elem in obtenerMantenimientos() if elem["Fecha Inicio"] == fecha]
            try:
                vehiculos = [elem.pop("Vehiculo") for elem in mantenimientos]
                dataMantenimientos = pd.DataFrame(mantenimientos)
                dataMantenimientos = dataMantenimientos.drop("_id",axis=1)
                vehiculos = pd.DataFrame(vehiculos)
                vehiculos = vehiculos.drop("Bitacora Conductores",axis=1)
                vehiculos = vehiculos.drop("_id",axis=1)
                vehiculos = vehiculos.drop("Especificaciones",axis=1)
                vehiculos = vehiculos.drop("Conductor",axis=1)
                df =  pd.concat([dataMantenimientos,vehiculos],axis=1)
                st.data_editor(df,column_config={"Foto Dekra": st.column_config.ImageColumn(), "Foto Marchamo": st.column_config.ImageColumn(), "Foto Vehiculo": st.column_config.ImageColumn()}, hide_index=True)
            except:
                st.warning("No hay registros disponibles para la fecha de inicio que ingreso")

        if opcion == "Fecha Fin":
            fecha = str(st.date_input("Ingresa la fecha de finalización del mantenimiento"))
            mantenimientos = [elem for elem in obtenerMantenimientos() if elem["Fecha Fin"] == fecha]
            try:
                vehiculos = [elem.pop("Vehiculo") for elem in mantenimientos]
                dataMantenimientos = pd.DataFrame(mantenimientos)
                dataMantenimientos = dataMantenimientos.drop("_id",axis=1)
                vehiculos = pd.DataFrame(vehiculos)
                vehiculos = vehiculos.drop("Bitacora Conductores",axis=1)
                vehiculos = vehiculos.drop("_id",axis=1)
                vehiculos = vehiculos.drop("Especificaciones",axis=1)
                vehiculos = vehiculos.drop("Conductor",axis=1)
                df =  pd.concat([dataMantenimientos,vehiculos],axis=1)
                st.data_editor(df,column_config={"Foto Dekra": st.column_config.ImageColumn(), "Foto Marchamo": st.column_config.ImageColumn(), "Foto Vehiculo": st.column_config.ImageColumn()}, hide_index=True)
            except:
                st.warning("No hay registros disponibles para la fecha de fin que ingreso")


        if opcion == "Mensual":
            mes = st.selectbox("Ingresa el mes que deseas ver",["01","02","03","04","05","06","07","08","09","10","11","12"])
            year = st.selectbox("Seleccione el año que desea ver",[str(elem) for elem in range(2022,2025)])
            try:
                mantenimientos = [elem for elem in obtenerMantenimientos() if (elem["Fecha Inicio"][5:7] == mes or elem["Fecha Fin"][5:7] == mes) and (elem["Fecha Inicio"][0:4]==year or elem["Fecha Fin"][0:4]==year)]
                vehiculos = [elem.pop("Vehiculo") for elem in mantenimientos]
                dataMantenimientos = pd.DataFrame(mantenimientos)
                dataMantenimientos = dataMantenimientos.drop("_id",axis=1)
                vehiculos = pd.DataFrame(vehiculos)
                vehiculos = vehiculos.drop("_id",axis=1)
                vehiculos = vehiculos.drop("Bitacora Conductores",axis=1)
                vehiculos = vehiculos.drop("Especificaciones",axis=1)
                vehiculos = vehiculos.drop("Conductor",axis=1)
                df =  pd.concat([dataMantenimientos,vehiculos],axis=1)
                st.data_editor(df,column_config={"Foto Dekra": st.column_config.ImageColumn(), "Foto Marchamo": st.column_config.ImageColumn(), "Foto Vehiculo": st.column_config.ImageColumn()}, hide_index=True)
            except:
                st.warning("No hay registros disponibles para el periodo seleccionado")





    if consultaMantenimiento == "Por vehiculo":
        try:
            vehiculos =  [elem["Placa"] for elem in obtenerVehiculos()]
            placaSeleccionado = st.selectbox("Seleccione el vehiculo que desea consultar",vehiculos)
            vehiculoSeleccionado = obtenerVehiculo({"Placa": placaSeleccionado})[0]
            mantenimientos = [elem for elem in obtenerMantenimiento({"Vehiculo":vehiculoSeleccionado})]
            vehiculos = [elem.pop("Vehiculo") for elem in mantenimientos]
            dataMantenimientos = pd.DataFrame(mantenimientos)
            dataMantenimientos = dataMantenimientos.drop("_id",axis=1)
            vehiculos = pd.DataFrame(vehiculos)
            vehiculos = vehiculos.drop("Bitacora Conductores",axis=1)
            vehiculos = vehiculos.drop("_id",axis=1)
            vehiculos = vehiculos.drop("Especificaciones",axis=1)
            vehiculos = vehiculos.drop("Conductor",axis=1)
            df =  pd.concat([dataMantenimientos,vehiculos],axis=1)
            st.data_editor(df,column_config={"Foto Dekra": st.column_config.ImageColumn(), "Foto Marchamo": st.column_config.ImageColumn(), "Foto Vehiculo": st.column_config.ImageColumn()}, hide_index=True)
        
        except:
            st.warning("No hay registros relacionados con el Vehiculo seleccionado")
        

    if consultaMantenimiento == "Por taller":
        pass

if consulta == "Edicion de mantenimientos":
    mantenimiento = st.selectbox("Selecciona el mantenimiento que deseas editar",[str(elem["Numero Mantenimiento"]) + "-" + elem["Reparacion"] for elem in obtenerMantenimientos()]).split("-")
    numeroMantenimiento = int(mantenimiento[0])
    vehiculoSeleccionado = st.selectbox("Selecciona el vehiculo al que le hiciste el mantenimiento",[elem["Placa"] for elem in obtenerVehiculos()])
    vehiculo = obtenerVehiculo({"Placa":vehiculoSeleccionado})
    descripcion = st.text_area("Ingresa la nueva descripcion del mantenimiento")
    costo = st.number_input("Ingresa el nuevo costo del mantenimiento")
    kilometraje = st.number_input("Ingresa el kilometraje del vehiculo")
    fechaEntrada = str(st.date_input("Ingresa la fecha de ingreso del vehiculo al taller"))
    fechaSalida = str(st.date_input("Ingresa la fecha salida del taller"))
    calificacion = st.select_slider("Ingresa la nueva calificación al mantenimiento",[elem for elem in range(0,11)])
    registrar = st.button("Actualizar")
    if registrar:
        actualizarMantenimiento({"Numero Mantenimiento": numeroMantenimiento},{"$set":{"Detalles":descripcion,"Costo":costo,"Fecha Inicio":fechaEntrada, "Fecha Fin":fechaSalida,"Calificacion":calificacion,"Kilometraje":kilometraje,"Vehiculo":vehiculo[0]}})

    
    




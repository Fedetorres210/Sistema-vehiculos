import streamlit as st
import pandas as pd
from config import obtenerConductores,obtenerConductor,registrarPago,obtenerPagos,editarPago
from logica import Pago
from datetime import datetime
import altair as alt
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Pagos",
    page_icon="🚑",
    layout="wide")

consulta = st.sidebar.selectbox("Selecciona la opcion que deseas",["Resumen","Registro de Pago","Edicion de Pago","Consulta de Pagos"])

st.title("Bienvenido a la seccion de Pagos")
st.image("https://tynmagazine.com/wp-content/uploads/sites/3/2021/12/imagen-medios-de-pago-def.jpg")

if consulta =="Registro de Pago":
    conductores = [(elem["Nombre"] + " " + elem["Apellido"]) for elem in obtenerConductores()]
    conductoresApellido = [elem["Apellido"] for elem in obtenerConductores()]
    conductorSeleccionado = st.selectbox("Seleccione el Nombre del Conductor al cual desea ver la informacion", conductores).split()
    datosConductor = [elem for elem in obtenerConductor({"Nombre": conductorSeleccionado[0], "Apellido":conductorSeleccionado[1]})]
    fecha = str(st.date_input("Ingrese la fecha del pago"))
    hora = str(st.time_input("Ingresa la hora que se hizo el pago"))
    monto = st.number_input("Ingrese el monto del pago")
    metodo = st.selectbox("Seleccione el metodo de pago",["Efectivo","Sinpe"])
    detalles = st.selectbox("Seleccione el motivo del pago",["Pago semanal","Deposito","Otro"])
    if detalles == "Otro":
        de = st.text_input("Porfavor ingrese el motivo del pago")
        detalles = detalles + ":" + de
    registrar = st.button("Registrar")
    if registrar:
        try:
            pago = Pago(datosConductor[0],fecha,hora,monto,metodo,detalles)
            registrarPago(pago.generarDatosCsv())
            st.success("Se ha registrado el pago")
        except:
            st.warning("Hubo un fallo en el registro del pago")


if consulta == "Consulta de Pagos":
    consultaPagos = st.selectbox("Selecciona el tipo de consulta que deseas:",["General","Por Conductor", "Por Vehiculo", "Por fecha"])
    if consultaPagos == "General":
        pagos = [elem for elem in obtenerPagos()]
        conductores = [elem.pop("Conductor") for elem in pagos]
        dfPagos = pd.DataFrame(pagos)
        dfPagos = dfPagos.drop("_id",axis=1)
        dfConductores = pd.DataFrame(conductores).drop("_id",axis=1)
        dfPagos = pd.concat([dfPagos,dfConductores],axis=1)
        dfPagos = dfPagos.sort_values(by="Fecha")


        
        st.data_editor(dfPagos,hide_index=True,column_config={
        "FotoCedula": st.column_config.ImageColumn(
            "Foto Cedula",
            help= "Foto cedula del conductor",
        ),
        "FotoLicencia": st.column_config.ImageColumn(
            "Foto Licencia",
            help= "Foto de la licencia del conductor",
        ),
        "Foto": st.column_config.ImageColumn(
            "Foto ",
            help= "Foto del conductor",
        )

    })
        
    if consultaPagos == "Por Conductor":
        conductores = [(elem["Nombre"] + " " + elem["Apellido"]) for elem in obtenerConductores()]
        conductoresApellido = [elem["Apellido"] for elem in obtenerConductores()]
        conductorSeleccionado = st.selectbox("Seleccione el Nombre del Conductor al cual desea ver la informacion", conductores).split()
        datosConductor = [elem for elem in obtenerConductor({"Nombre": conductorSeleccionado[0], "Apellido":conductorSeleccionado[1]})]
        pagos = [elem for elem in obtenerPagos() if elem["Conductor"] == datosConductor[0]]
        consultaConductor =st.selectbox("Selecciona la opcion de consulta deseas realizar",["General","Por fecha","Por detalle"]) 
        if consultaConductor == "General":
            try:
                df = pd.DataFrame(pagos)
                df = df.drop("_id",axis=1)
                df = df.drop("Conductor",axis=1)
                st.data_editor(df,hide_index=True)
            except:
                    st.warning("No se tienen datos del dia seleccionado")

        if consultaConductor == "Por fecha":
            consultaConductorFecha = st.selectbox("Selecciona el tipo de consulta que deseas", ["Mensual","Diaria","Trimestral"])
            if consultaConductorFecha == "Diaria":
                try:
                    fechaPago = str(st.date_input("Selecciona la fecha que deseas ver el pago"))
                    pagosFecha = [elem for elem in pagos if elem["Fecha"] == fechaPago]
                    dfPagos = pd.DataFrame(pagosFecha)
                    dfPagos = dfPagos.drop("_id",axis=1)
                    dfPagos = dfPagos.drop("Conductor",axis=1)
                    
                    st.data_editor(dfPagos,hide_index=True)

                except:
                    st.warning("No se tienen datos del dia seleccionado")

            if consultaConductorFecha == "Mensual":
                try:
                    mes = st.selectbox("Selecciona el mes que deseas ver",["01","02","03","04","05","06","07","08","09","10","11","12"])
                    year = st.selectbox("Selecciona el año que deseas ver el mes",[str(elem) for elem in range(2022,2028)])     
                    pagosFecha = [elem for elem in pagos if elem["Fecha"][0:4] == year and elem["Fecha"][5:7] == mes ]
                    dfPagos = pd.DataFrame(pagosFecha)
                    dfPagos = dfPagos.drop("_id",axis=1)
                    dfPagos = dfPagos.drop("Conductor",axis=1)
                    
                    st.data_editor(dfPagos,hide_index=True)

                except:
                    st.warning("No se tienen datos del dia seleccionado")

            
            if consultaConductorFecha == "Trimestral":
                try:
                    trimestres = {
                        "01":["01","02","03"],
                        "02":["04","05","06"],
                        "03":["07","08","09"],
                        "04":["10","11","12"]

                    }
                    mes = st.selectbox("Selecciona el trimeste que deseas ver que deseas ver",["01","02","03","04"])
                    year = st.selectbox("Selecciona el año que deseas ver el mes",[str(elem) for elem in range(2022,2028)]) 

                    pagosFecha = [elem for elem in pagos if elem["Fecha"][0:4] == year and (elem["Fecha"][5:7] in trimestres[mes])]
                    dfPagos = pd.DataFrame(pagosFecha)
                    dfPagos = dfPagos.drop("_id",axis=1)
                    dfPagos = dfPagos.drop("Conductor",axis=1)
                    st.data_editor(dfPagos,hide_index=True)

                except:
                    st.warning("No se tienen datos del dia seleccionado")


        if consultaConductor == "Por detalle":
            detalles = ["Pago semanal","Deposito","Otro"]
            consultaDetalle =  st.selectbox("Selecciona el detalle que deseas ver",detalles)
            if consultaDetalle != "Otro":
                try:
                    pagosDetalle = [elem for elem in pagos if elem["Detalle"] == consultaDetalle]
                    dfPagos = pd.DataFrame(pagosDetalle)
                    dfPagos = dfPagos.drop("_id",axis=1)
                    dfPagos = dfPagos.drop("Conductor",axis=1)
                    st.data_editor(dfPagos,hide_index=True)
                except:
                    st.warning("No hay registro de pagos con ese detalle")
            else:
                try:
                    detalles.remove("Otro")
                    pagosDetalle = [elem for elem in pagos if elem["Detalle"] not in detalles]
                    dfPagos = pd.DataFrame(pagosDetalle)
                    dfPagos = dfPagos.drop("_id",axis=1)
                    dfPagos = dfPagos.drop("Conductor",axis=1)
                    st.data_editor(dfPagos,hide_index=True)
                except:  
                    st.warning("No hay registro de pagos con ese detalle")



if consulta =="Edicion de Pago":
    pago = st.selectbox("Selecciona el pago que deseas editar",[elem["Comprobante"] for elem in obtenerPagos()])
    pago = [elem for elem in obtenerPagos() if elem["Comprobante"] == pago][0]
    fecha = str(st.date_input("Ingrese la nueva fecha del pago"))
    hora = str(st.time_input("Ingresa la nueva hora que se hizo el pago"))
    monto = st.number_input("Ingrese el nuevo  monto del pago",value=pago["Monto"])
    metodo = st.selectbox("Seleccione el nuevo  metodo de pago",["Efectivo","Sinpe"])
    detalles = st.selectbox("Seleccione el nuevo motivo del pago",["Pago semanal","Deposito","Otro"])
    if detalles == "Otro":
        de = st.text_input("Porfavor ingrese el motivo del pago")
        detalles = detalles + ":" + de
    registrar = st.button("Editar")
    if registrar:
        try:
            csv = {
            "Comprobante": pago["Comprobante"],
            "Fecha":fecha,
            "Hora":hora,
            "Monto":monto,
            "Metodo":metodo,
            "Detalle": detalles
        }
            editarPago({"Comprobante":pago["Comprobante"]},{"$set":csv})
            st.success("Se ha editado el pago")
        except:
            st.warning("Hubo un fallo en la edicion del pago")


if consulta == "Resumen":
    pagos = [elem for elem in obtenerPagos()]
    conductores = [elem.pop("Conductor") for elem in pagos]
    dfPagos = pd.DataFrame(pagos)
    dfPagos = dfPagos.drop("_id",axis=1)
    dfConductores = pd.DataFrame(conductores).drop("_id",axis=1)
    dfPagos = pd.concat([dfPagos,dfConductores],axis=1)
    dfPagos = dfPagos.sort_values(by="Fecha")
    st.data_editor(dfPagos,hide_index=True,column_config={
        "FotoCedula": st.column_config.ImageColumn(
            "Foto Cedula",
            help= "Foto cedula del conductor",
        ),
        "FotoLicencia": st.column_config.ImageColumn(
            "Foto Licencia",
            help= "Foto de la licencia del conductor",
        ),
        "Foto": st.column_config.ImageColumn(
            "Foto ",
            help= "Foto del conductor",
        )

    })
    now = datetime.now()
    montos = [elem["Monto"] for elem in obtenerPagos() if elem["Fecha"][0:4] == str(now.year) and elem["Fecha"][5:7]== "0" + str(now.month)]
    
    nombre = [elem["Conductor"]["Nombre"]   for elem in obtenerPagos() if elem["Fecha"][0:4] == str(now.year) and elem["Fecha"][5:7]== "0" + str(now.month)]
    apellido = [ elem["Conductor"]["Apellido"]  for elem in obtenerPagos() if elem["Fecha"][0:4] == str(now.year) and elem["Fecha"][5:7]== "0" + str(now.month)]
    fecha = [ elem["Fecha"]  for elem in obtenerPagos() if elem["Fecha"][0:4] == str(now.year) and elem["Fecha"][5:7]== "0" + str(now.month)]
    data = {
        "nombre": nombre,
        "apellido":apellido,
        "monto":montos,
        "fecha":fecha
    }
    data

    df = pd.DataFrame(data)

    df['fecha'] = pd.to_datetime(df['fecha'])

    # Agrupar por conductor y fecha, y sumar los montos
    df_conductores = df.groupby(['nombre', 'apellido', 'fecha']).sum().reset_index()

    # Crear un diccionario para almacenar los datos de cada conductor
    data_dict = {}

    # Iterar sobre cada grupo de conductor y almacenar los datos en el diccionario
    for conductor, data in df_conductores.groupby(['nombre', 'apellido']):
        conductor_label = f"{conductor[0]} {conductor[1]}"
        data_dict[conductor_label] = data.set_index('fecha')['monto']

    # Mostrar el gráfico de líneas con st.line_chart()
    st.line_chart(pd.DataFrame(data_dict))
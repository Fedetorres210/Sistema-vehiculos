import streamlit as st
from config import obtenerConductor, obtenerIncidente, obtenerIncidentes, obtenerConductores, registrarVehiculo,obtenerVehiculos,obtenerVehiculo,editarVehiculo
from logica import Vehiculo, BitacoraRegistro
from datetime import datetime
import pandas as pd



st.title("Bienvenido a la seccion de Vehiculos")
st.image("https://www.revistaautocrash.com/wp-content/uploads/2019/10/carros-nuevos.jpg")
consulta = st.selectbox("Seleccione la opcion que desea",["Resumen","Registro de Vehiculo","Edicion de vehiculos", "Consulta de Vehiculos"])
if consulta == "Registro de Vehiculo":
    st.title("Registro de Vehiculo")
    placa = st.text_input("Ingrese la placa del vehiculo")
    marcas= Vehiculo.obtener_marcas()
    marca = st.selectbox("Ingrese la marca del vehiculo",marcas)
    modelos = Vehiculo.obtenerModelos(marca)
    modelo = st.selectbox("Ingrese el modelo del vehiculo",modelos)
    
    year = st.selectbox("Ingrese el año del vehiculo",[ elem for elem in range(2016,2021)])
    color = st.text_input("Ingrese el color del vehiculo")
    fechaDekra = str(st.date_input("Ingrese la fecha del vencimiento del dekra"))
    conductores = [(elem["Nombre"] + " " + elem["Apellido"]) for elem in obtenerConductores()]
    conductores.append("Sin Conductor Asignado")
    conductorSeleccionado = st.selectbox("Seleccione el conductor que se va encargar del vehiculo", conductores).split()
    datosConductor = [elem for elem in obtenerConductor({"Nombre": conductorSeleccionado[0], "Apellido":conductorSeleccionado[1]})]
    fotoVehiculo = st.text_input("Ingrese el link para la foto del vehiculo")
    fotoMarchamo = st.text_input("Ingrese el link de la foto del marchamo")
    fotoDekra = st.text_input("Ingrese el link de la foto del dekra")
    fechaInicioConductor = str(st.date_input("Ingrese la fecha de inicio del conductor con el vehiculo"))


    
    registro = st.button("Registrar")
    if registro:
        try:
            especificaciones = Vehiculo.obtenerEspecificaciones(marca,modelo,year)
            bitacora = BitacoraRegistro(datosConductor[0],placa,fechaInicioConductor,"")
            vehiculo = Vehiculo(placa,modelo, marca,year,color,fechaDekra,fotoVehiculo,fotoMarchamo, fotoDekra, datosConductor[0],[bitacora.generarDatosCsv()],especificaciones)
            csv = vehiculo.generarDatosCsv()
            registrarVehiculo(csv)
            st.success("Se ha registrado exitosamente")
        except:
            st.warning("Fallo en la creacion")


if consulta == "Edicion de vehiculos":
    vehiculos =  [elem["Placa"] for elem in obtenerVehiculos()]
    placaSeleccionado = st.selectbox("Seleccione el vehiculo que desea editar",vehiculos)
    vehiculoSeleccionado = obtenerVehiculo({"Placa": placaSeleccionado})
    tipoEdicion = st.selectbox("Seleccione lo que desea editar",["Fecha Dekra","Conductor Asignado","Fotos"])
    if tipoEdicion == "Fecha Dekra":
        fechaDekra = str(st.date_input("Ingrese la nueva fecha del vencimiento del dekra"))
        editar = st.button("Editar")
        if editar:
            try:
                editarVehiculo({"Placa": placaSeleccionado},{"$set":{"Fecha Vencimiento Dekra":fechaDekra}})
                st.success("Se ha realizado la edicion con exito")
            except:
                st.warning("Ha ocurrido un fallo en la edicion de los elementos")
    
    if tipoEdicion == "Conductor Asignado":
        conductores = [(elem["Nombre"] + " " + elem["Apellido"]) for elem in obtenerConductores()]
        conductores.append("Sin Conductor Asignado")
        conductorSeleccionado = st.selectbox("Seleccione el conductor que se va encargar del vehiculo", conductores).split()
        datosConductor = [elem for elem in obtenerConductor({"Nombre": conductorSeleccionado[0], "Apellido":conductorSeleccionado[1]})]
        fechaInicioConductor = str(st.date_input("Ingrese la fecha de inicio del conductor con el vehiculo"))
        editar = st.button("Editar")
        if editar:
            try:
                bitacoras = obtenerVehiculo({"Placa": placaSeleccionado})[0]["Bitacora Conductores"]
                bitacoras[-1]["Fecha Finalizacion"] = datetime.now().strftime("%Y-%m-%d")
                nuevaBitacora = BitacoraRegistro(datosConductor[0],placaSeleccionado,fechaInicioConductor,"").generarDatosCsv()
                bitacoras.append(nuevaBitacora)
                st.text(bitacoras)
                editarVehiculo({"Placa": placaSeleccionado},{"$set":{"Conductor":datosConductor[0],"Bitacora Conductores":bitacoras}})
                st.success("Se ha realizado la edicion con exito")
            except:
                st.warning("Ha ocurrido un fallo en la edicion de los elementos")


    if tipoEdicion == "Fotos":
        opcionFoto = st.selectbox("Ingrese la opcion que desea editar",["Foto Vehiculo", "Foto Marchamo", "Foto Dekra", "Todas"])
        if opcionFoto == "Foto Vehiculo":
            fotoVehiculo = st.text_input("Ingrese el link para la foto del vehiculo")
            editar = st.button("Editar")
            if editar:
                try:
                    editarVehiculo({"Placa": placaSeleccionado}, {"$set": {"Foto Vehiculo": fotoVehiculo}})
                    st.success("Se ha editado con exito")
                except:
                    st.warning("Ha ocurrido un error en la edicion")
        
        if opcionFoto == "Foto Marchamo":
            fotoMarchamo = st.text_input("Ingrese el link para la foto del Marchamo")
            editar = st.button("Editar")
            if editar:
                try:
                    editarVehiculo({"Placa": placaSeleccionado}, {"$set": {"Foto Marchamo": fotoMarchamo}})
                    st.success("Se ha editado con exito")
                except:
                    st.warning("Ha ocurrido un error en la edicion")

        if opcionFoto == "Foto Dekra":
            fotoDekra = st.text_input("Ingrese el link para la foto del Dekra")
            editar = st.button("Editar")
            if editar:
                try:
                    editarVehiculo({"Placa": placaSeleccionado}, {"$set": {"Foto Dekra": fotoDekra}})
                    st.success("Se ha editado con exito")
                except:
                    st.warning("Ha ocurrido un error en la edicion")
        
        if opcionFoto == "Todas":
            fotoVehiculo = st.text_input("Ingrese el link para la foto del vehiculo")
            fotoMarchamo = st.text_input("Ingrese el link de la foto del marchamo")
            fotoDekra = st.text_input("Ingrese el link de la foto del dekra")
            editar = st.button("Editar")
            if editar:
                try:
                    editarVehiculo({"Placa": placaSeleccionado}, {"$set": {"Foto Vehiculo": fotoVehiculo, "Foto Dekra":fotoDekra, "Foto Marchamo": fotoMarchamo}})
                    st.success("Se ha editado con exito")
                except:
                    st.warning("Ha ocurrido un error en la edicion")


if consulta == "Consulta de Vehiculos":
    vehiculos =  [elem["Placa"] for elem in obtenerVehiculos()]
    placaSeleccionado = st.selectbox("Seleccione el vehiculo que desea editar",vehiculos)
    vehiculoSeleccionado = obtenerVehiculo({"Placa": placaSeleccionado})[0]
    consultaVehiculo = st.selectbox("Selecciona la consulta de vehiculo que deseas realizar",["Consulta general","Especificaciones","Conductores"])
    if consultaVehiculo == "Consulta general":
        col1,col2 = st.columns(2)
        vehiculoSeleccionado.pop("_id")
        #fotos = [vehiculoSeleccionado.pop("Foto Dekra"),vehiculoSeleccionado.pop("Foto Marchamo"),vehiculoSeleccionado.pop("Foto Vehiculo")]
        conductor = vehiculoSeleccionado.pop("Conductor")
        bitacora = vehiculoSeleccionado.pop("Bitacora Conductores")
        especificaciones = vehiculoSeleccionado.pop("Especificaciones")
        conductor.pop("_id")
        df = pd.DataFrame([conductor])
        vehiculoSeleccionado = pd.DataFrame(vehiculoSeleccionado, index = [0])
        with col1:
            st.title("Vehiculo")
            st.data_editor(vehiculoSeleccionado, column_config={"Foto Dekra": st.column_config.ImageColumn(), "Foto Marchamo": st.column_config.ImageColumn(), "Foto Vehiculo": st.column_config.ImageColumn()}, hide_index=True, height=100)
        with col2:
            st.title("Conductor")
            st.data_editor(df,column_config={"FotoCedula": st.column_config.ImageColumn("Foto cedula"), "FotoLicencia": st.column_config.ImageColumn("Foto Licencia"), "Foto": st.column_config.ImageColumn("Foto")},hide_index=True,height=100)
        col3,col4 = st.columns(2)
        with col3:
            especificaciones = pd.DataFrame(especificaciones, index= [0])
            st.title("Especificaciones")
            st.data_editor(especificaciones,hide_index=True, height=100)
        
        with col4:
            #conductoresBitacora = [elem.pop("Conductor") for elem in bitacora]
          #  bitacora[0]
           # conductoresBitacora[0]
            #print(type(conductoresBitacora[0].update(bitacora[0])))
            #itacora = [bitacora[elem].update(conductoresBitacora[elem]) for elem in range(0, len(bitacora))]
            for elem in bitacora:
                conductor = elem.pop("Conductor", {})  # Extraer el diccionario "Conductor" o un diccionario vacío si no está presente
                elem.update(conductor) 
            
            bitacora = pd.DataFrame(bitacora)
            st.title("Bitacora")
            st.data_editor(bitacora,hide_index=True,height=100,column_config={"FotoCedula": st.column_config.ImageColumn("Foto cedula"), "FotoLicencia": st.column_config.ImageColumn("Foto Licencia"), "Foto": st.column_config.ImageColumn("Foto")})


if consulta =="Resumen":

    vehiculos = obtenerVehiculos()
    vehiculosdf = pd.DataFrame(vehiculos)
    conductores = [elem.pop("Conductor") for elem in obtenerVehiculos()]
    
    vehiculosdf.set_index("Placa", inplace=True)
    vehiculosdf = vehiculosdf.drop("_id",axis=1)
    vehiculosdf = vehiculosdf.drop("Conductor",axis=1)
    vehiculosdf = vehiculosdf.drop("Bitacora Conductores", axis=1)
    vehiculosdf = vehiculosdf.drop("Especificaciones", axis=1)
    col1,col2 = st.columns(2)
    with col1:
        st.title("Vehiculos")
        st.data_editor(vehiculosdf, column_config={"Foto Dekra": st.column_config.ImageColumn(), "Foto Marchamo": st.column_config.ImageColumn(), "Foto Vehiculo": st.column_config.ImageColumn()}, hide_index=True, height=100)
    with col2:
        st.title("Conductor")
        st.data_editor(conductores,column_config={"FotoCedula": st.column_config.ImageColumn("Foto cedula"), "FotoLicencia": st.column_config.ImageColumn("Foto Licencia"), "Foto": st.column_config.ImageColumn("Foto")},hide_index=True,height=100)
        
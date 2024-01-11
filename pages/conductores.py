import streamlit as st
from config import obtenerConductores,insertarCondcutor,obtenerConductor,registrarIncidente, obtenerIncidentes, obtenerIncidente, obtenerVehiculos, obtenerVehiculo
from logica import Conductor, Mapa, Incidente
import pandas as pd


st.set_page_config(page_title="Conductores", page_icon="📈")

st.header("Bienvenido a la seccion de conductores")
st.image("https://www.emagister.com/blog/wp-content/uploads/2019/04/ch%C3%B3fer-privado.jpg")
opcionConductores = st.selectbox("Seleccione la accion por realizar",["Resumen","Registro de Conductor", "Consulta de informacion de conductor", "Registro de incidentes","Consulta de incidentes"])

if (opcionConductores== "Resumen"):
    totalConductor = obtenerConductores()
    
    conductores = pd.DataFrame(totalConductor)
    conductores = conductores.drop("_id",axis=1)
    config ={
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

    }
   
    st.title("Conductores")
    st.data_editor(conductores,hide_index=True,column_config=config)

    st.title("Incidentes")
    datos = [elem for elem in obtenerIncidentes()]
    v = [elem.pop("_id") for elem in datos]
    st.data_editor(datos, hide_index= True, 
                               column_config= {
                                   "Costo": st.column_config.NumberColumn(
                                       "Costo",
                                       format="₡%d",
                                       help="Costo del incidente en colones "
                                       )})
    
        





if (opcionConductores== "Registro de Conductor"):
    st.subheader("Bienvenido al registro de conductor")
    nombre = st.text_input("Nombre del conductor")
    apellido = st.text_input("Apellido del conductor")
    cedula = st.text_input("Cedula del conductor")
    fotoCedula = st.text_input("Ingrese el link de la foto de la cedula")
    licencia = st.text_input("Numero de licencia")
    fotoLicencia = st.text_input("Ingrese el link de la foto licencia")
    direccion = st.text_input("Ingrese los datos de la direccion  de la vivienda del conductor")
    mapa = Mapa()
    result = mapa.autocomplete_address(direccion)
    direccionExacta = st.selectbox("Seleccione el punto mas exacto de la direccion del conductor", result)
    fotoConductor = st.text_input("Link del foto del conductor")
    cuotaSemanal = st.number_input("Ingrese la cuota semanal del conductor")
    registrar = st.button("Registrar Conductor")

    if (registrar):
        try:
            nuevoConductor = Conductor(nombre, apellido, cedula, licencia, direccionExacta, fotoConductor,fotoCedula, fotoLicencia,cuotaSemanal)
            insertarCondcutor(nuevoConductor.generarDatosCsv())
            st.success("Nuevo Conductor Insertado!")
        except:
            st.warning("Ha ocurrido un fallo con la insercion del usuario")

if (opcionConductores== "Consulta de informacion de conductor"):
        conductores = [(elem["Nombre"] + " " + elem["Apellido"]) for elem in obtenerConductores()]
        conductoresApellido = [elem["Apellido"] for elem in obtenerConductores()]
        conductorSeleccionado = st.selectbox("Seleccione el Nombre del Conductor al cual desea ver la informacion", conductores).split()
        datosConductor = [elem for elem in obtenerConductor({"Nombre": conductorSeleccionado[0], "Apellido":conductorSeleccionado[1]})]

        col1, col2 = st.columns(2)

        with col1:
             st.title(datosConductor[0]["Nombre"] + " " +  datosConductor[0]["Apellido"])
             st.image(datosConductor[0]["FotoCedula"])
             st.subheader("Cedula: " + datosConductor[0]["Cedula"])
             st.image(datosConductor[0]["FotoCedula"])
             st.subheader("Licencia: " + datosConductor[0]["Numero de Licencia"])
             st.image(datosConductor[0]["FotoLicencia"])
             st.subheader("Direccion: " + datosConductor[0]["Direccion"])
             mapa = Mapa()
             result = mapa.obtener_latitud_longitud(datosConductor[0]["Direccion"])
             df = pd.DataFrame({
                "col1" :result[0],
                "col2" :result[1]
             }, index=[0])
             
             st.map(df, latitude='col1', longitude= 'col2')
        with col2:
            pass

if (opcionConductores== "Registro de incidentes"):
    st.subheader("Registro de incidentes para conductores")
    conductores = [(elem["Nombre"] + " " + elem["Apellido"]) for elem in obtenerConductores()]
    conductoresApellido = [elem["Apellido"] for elem in obtenerConductores()]
    conductorSeleccionado = st.selectbox("Seleccione el Nombre del Conductor al cual desea ver la informacion", conductores).split()
    datosConductor = [elem for elem in obtenerConductor({"Nombre": conductorSeleccionado[0], "Apellido":conductorSeleccionado[1]})]
    nombreIncidente = st.text_input("Ingrese el nombre del incidente sucedido")
    detalleIncidente = st.text_area("Ingrese los detalles del incidente sucedido")
    fechaIncidente = str(st.date_input("Ingrese la fecha del incidente",format="YYYY/MM/DD"))
    costoIncidente = st.number_input("Ingrese el costo del incidente en colones")
    registro = st.button("Registrar")
    if registro:
        try:
            incidente = Incidente(nombreIncidente,detalleIncidente,fechaIncidente,costoIncidente,{"Nombre":datosConductor[0]["Nombre"],"Apellido":datosConductor[0]["Apellido"],"Cedula": datosConductor[0]["Cedula"]})
            incidenteCSV = incidente.generarDatosCsv()
            registrarIncidente(incidenteCSV)
            st.success("Se ha registrado exitosamente")
        except:
            st.warning("Ha fallado ")

if (opcionConductores== "Consulta de incidentes"):
    consulta = st.selectbox("Seleccione la opcion que desea",["Ultimos incidentes","Incidentes por Conductor","Incidentes por fecha"])
    if (consulta == "Ultimos incidentes"):
        col1,col2 = st.columns(2)
        datos = [elem for elem in obtenerIncidentes()]
        datos = pd.DataFrame(datos)
        datos = datos.drop("_id",axis=1)
        datos = datos.sort_values(by="Fecha",ascending=False)
        st.data_editor(datos, hide_index= True, 
                               column_config= {
                                   "Costo": st.column_config.NumberColumn(
                                       "Costo",
                                       format="₡%d",
                                       help="Costo del incidente en colones "
                                       )})
    
    if (consulta == "Incidentes por Conductor"):
        conductores = [(elem["Nombre"] + " " + elem["Apellido"]) for elem in obtenerConductores()]
        conductoresApellido = [elem["Apellido"] for elem in obtenerConductores()]
        conductorSeleccionado = st.selectbox("Seleccione el Nombre del Conductor al cual desea ver la informacion", conductores).split()
        datosConductor = [elem for elem in obtenerIncidente({"Nombre Conductor": conductorSeleccionado[0], "Apellido Conductor":conductorSeleccionado[1]})]
        
        id = [elem.pop("_id") for elem in datosConductor]
        st.data_editor(datosConductor,hide_index= True, 
                               column_config= {
                                   "Costo": st.column_config.NumberColumn(
                                       "Costo",
                                       format="₡%d",
                                       help="Costo del incidente en colones "
                                       )})
    
            
    if(consulta == "Incidentes por fecha"):
        tipoConsultaFecha = st.selectbox("Seleccione la opcion que desea",["Fecha exacta", "Periodos"])
        if (tipoConsultaFecha == "Fecha exacta"):
            fecha = st.date_input("Ingrese la fecha que desea ver")
            datosConductor = [elem for elem in obtenerIncidente({"Fecha": str(fecha)})]
            id = [elem.pop("_id") for elem in datosConductor]
            st.data_editor(datosConductor,hide_index= True, 
                               column_config= {
                                   "Costo": st.column_config.NumberColumn(
                                       "Costo",
                                       format="₡%d",
                                       help="Costo del incidente en colones "
                                       )})        
        if (tipoConsultaFecha == "Periodos"):
            periodo = st.selectbox("Seleccione el tipo de periodo que desea",["Mensual","Trimestre"])
            if periodo == "Mensual":
                mes = st.selectbox("Seleccione el mes que desea ver",["01","02","03","04","05","06","07","08","09","10","11","12"])
                year = st.selectbox("Seleccione el año que desea ver",[str(elem) for elem in range(2022,2025)])
                
                incidentesFecha = [elem for elem in obtenerIncidentes() if elem["Fecha"][0:4] == year and elem["Fecha"][5:7] == mes]
                ids = [elem.pop("_id") for elem in incidentesFecha]
                st.data_editor(incidentesFecha,hide_index= True, 
                               column_config= {
                                   "Costo": st.column_config.NumberColumn(
                                       "Costo",
                                       format="₡%d",
                                       help="Costo del incidente en colones "
                                       )})
                
            
            if periodo == "Trimestre":
                trimestre = st.selectbox("Seleccione el trimestre que desea ver",[str(elem) for elem in range(1,5)])
                year = st.selectbox("Seleccione el año que desea ver",[str(elem) for elem in range(2022,2025)])

                trimestres = {
                    "1":["01","02","03"],
                    "2":["04","05","06"],
                    "3":["07","08","09"],
                    "4":["10","11","12"]
                }


                incidentes = [elem for elem in obtenerIncidentes() if elem["Fecha"][5:7] in trimestres[trimestre] and elem["Fecha"][0:4]== year]
                st.data_editor(incidentes,hide_index= True, 
                               column_config= {
                                   "Costo": st.column_config.NumberColumn(
                                       "Costo",
                                       format="₡%d",
                                       help="Costo del incidente en colones "
                                       )})



            
            

        
       

        
        
    


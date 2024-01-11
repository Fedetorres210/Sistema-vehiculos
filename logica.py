from typing import Any
from geopy.geocoders import Nominatim
import requests
from config import obtenerIncidentes



class Conductor:
    def __init__(self,nombre,apellido, cedula, numLicencia, direccion,pagos,foto):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.numLicencia = numLicencia
        self.direccion = direccion
        # Placa vehiculo se refiere a el vehiculo que usa el conductor
        
        #Pagos es un atributo que confirma si el conductor se encuentra al dia con os pagos
        self.pagos = pagos
        self.foto = foto

    def __init__(self,nombre,apellido, cedula, numLicencia, direccion,foto, fotoCedula, fotoLicencia,cuotaSemanal):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.numLicencia = numLicencia
        self.direccion = direccion
        # Placa vehiculo se refiere a el vehiculo que usa el conductor
        self.vehiculo = vehiculo
        #Pagos es un atributo que confirma si el conductor se encuentra al dia con os pagos
        self.fotoCedula = fotoCedula
        self.fotoLicenia = fotoLicencia
        self.foto = foto
        self.pagos = []
        self.cuotaSemanal = cuotaSemanal



    def generarDatosCsv(self):
        dict = {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "Cedula": self.cedula,
            "Numero de Licencia": self.numLicencia,
            "Direccion": self.direccion,
            "Vehiculo": self.vehiculo,
            "Pagos": self.pagos,
            "FotoCedula": self.fotoCedula,
            "FotoLicencia": self.fotoLicenia,
            "Foto": self.foto,
            "Cuota Semanal": self.cuotaSemanal

        }

        return dict
    

    
    



class Vehiculo:
    def __init__(self,placa,marca,year,color,llantas,cilindrada,imagen):
        self.placa = placa,
        self.marca = marca,
        self.year = year,
        self.color = color,
        self.llantas = llantas,
        self.cilindrada = cilindrada
        self.imagen = imagen
    

    def generarDatosCsv(self):
        dict = {
            "Placa": self.placa,
            "Marca": self.marca,
            "year": self.year,
            "Color": self.color,
            "Llantas": self.llantas,
            "Cilindrada": self.cilindrada,
            "Imagen": self.imagen
        }
        return dict
    

class Reparacion:

    def __init__(self,nombre, fechaInicio, fechaFin, detalle, costo, vehiculo, taller):
        self.nombre = nombre,
        self.fechaInicio = fechaInicio,
        self.fechaFin = fechaFin,
        self.detalle = detalle,
        self.costo = costo,
        self.vehiculo = vehiculo
        self.taller = taller

    def generarDatosCsv(self):
        dict = {
            "Nombre": self.nombre,
            "Fecha Inicio": self.fechaInicio,
            "Fecha Fin": self.fechaFin,
            "Detalle": self.detalle,
            "Costo": self.costo,
            "Vehiculo": self.vehiculo,
            "Taller": self.taller
        }
        
        return dict
    


class Pago:

    def __init__(self, Conductor, Vehiculo, monto, fecha):
        self.Conductor = Conductor,
        self.Vehiculo = Vehiculo,
        self.monto = monto,
        self.fecha = fecha

    def generarDatosCsv(self):
        dict = {
            "Conductor":self.Conductor,
            "Vehiculo":self.Vehiculo,
            "monto": self.monto,
            "fecha": self.fecha
        }
        return dict

    
class PagoRebajado(Pago):

    def __init__(self, Conductor, Vehiculo, monto, fecha, desgloseRebaja):
        super().__init__(Conductor, Vehiculo, monto, fecha)
        self.desgloseRebaja = desgloseRebaja
    
    def generarDatosCsv(self):
        dict = {
            "Conductor":self.Conductor,
            "Vehiculo":self.Vehiculo,
            "Monto": self.monto,
            "Fecha": self.fecha,
            "Desglose de Rebaja": self.desgloseRebaja
        }
        return dict
    
class Mapa:

    def __init__(self):
        self.apiKey = "jKvc0uAOCixuQbL_8CqHW9AL6WxrI1U1suiTup1rTm4"

    def autocomplete_address(self, query):

        base_url = "https://geocode.search.hereapi.com/v1/geocode"
        params = {
            'apiKey': self.apiKey,
            'q': query,
        }

        response = requests.get(base_url, params=params)
        results = response.json().get('items', [])
        print(results)

        if results:
            addresses = [result['title'] for result in results]
            return addresses
        else:
            return []
        
    def obtener_latitud_longitud(self, lugar):
        base_url = "https://geocode.search.hereapi.com/v1/geocode"
        params = {
            'apiKey': self.apiKey,
            'q': lugar,
        }

        response = requests.get(base_url, params=params)
        data = response.json()
        print(data)

        if data.get('items'):
            ubicacion = data['items'][0]['position']
            latitud = ubicacion['lat']
            longitud = ubicacion['lng']
            return latitud, longitud
        else:
            return None

    
class Incidente:
    

    def obtenerNumeroIncidente():
        datos = [elem for elem in obtenerIncidentes()]
        print(datos)
        try:
            numero = int(datos[-1].pop("Numero Incidente")) + 1
        except:
            numero =0
        
        return numero
           

    def __init__(self,nombreIncidente,detalles,fecha,costo,conductor):
        self.numeroDeIncidente = Incidente.obtenerNumeroIncidente()
        self.incidente = nombreIncidente
        self.detalles = detalles
        self.fecha = fecha
        self.costo = costo
        self.conductor = conductor
        

    def generarDatosCsv(self):
        dict = {
            "Numero Incidente": self.numeroDeIncidente,
            "Incidente":self.incidente,
            "Detalles":self.detalles,
            "Fecha": self.fecha,
            "Costo":self.costo,
            "Nombre Conductor": self.conductor["Nombre"],
            "Apellido Conductor": self.conductor["Apellido"],
            "Cedula Conductor":self.conductor["Cedula"]

        }
        return dict


class Vehiculo:

    def __init__(self,placa,modelo, marca, year,color,fechaDekra,fotoVehiculo,fotoMarchamo,fotoDekra,conductor,bitacoraConductores,specs):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.year   = year
        self.color = color
        self.fechaDekra = fechaDekra
        self.fotoVehiculo = fotoVehiculo
        self.fotoMarchamo = fotoMarchamo
        self.fotoDekra = fotoDekra
        self.conductor = conductor
        self.bitacora = bitacoraConductores
        self.specs = specs
    def generarDatosCsv(self):
        csv = {
            "Placa": self.placa,
            "Modelo": self.modelo,
            "Marca": self.marca,
            "Year":self.year,
            "Fecha Vencimiento Dekra": self.fechaDekra,
            "Foto Vehiculo": self.fotoVehiculo,
            "Foto Marchamo": self.fotoMarchamo,
            "Foto Dekra": self.fotoDekra,
            "Conductor": self.conductor,
            "Bitacora Conductores": self.bitacora,
            "Especificaciones" :self.specs

        }
        return csv
    

    def obtener_marcas():
        url = "https://car-api2.p.rapidapi.com/api/makes"
        headers = {
            'X-RapidAPI-Key': '3dcfb11764mshc48ea40ecb6a0efp1fe268jsn4cf3d3d28ba2',
            'X-RapidAPI-Host': 'car-api2.p.rapidapi.com'
        }

        try:
            respuesta = requests.get(url, headers=headers)
            datos = respuesta.json()
            
            # Filtrar las marcas de automóviles
            marcas = [marca["name"] for marca in datos["data"]]
            marcas.append("Changan")
            marcas.append("Geely")
            marcas.append("BYD")
            return marcas
        except Exception as e:
            print(f"Error al obtener las marcas: {e}")
            return []
        
    def obtenerModelos(marca):
        url= "https://car-api2.p.rapidapi.com/api/models",
        params = {
            'make': marca,
            'sort': 'id',
            'year': ["2016","2018","2019"],
            'direction': 'asc',
            'verbose': 'yes'
            }
        headers = {
            'X-RapidAPI-Key': '3dcfb11764mshc48ea40ecb6a0efp1fe268jsn4cf3d3d28ba2',
            'X-RapidAPI-Host': 'car-api2.p.rapidapi.com'
        }
        


        try:
            respuesta = requests.get("https://car-api2.p.rapidapi.com/api/models", headers=headers,params=params)
            datos = respuesta.json()
            
            
            # Filtrar las marcas de automóviles
            marcas = [marca["name"] for marca in datos["data"]]
            if marca == "BYD":
                marcas.append("F3")
                marcas.append("F0")
                marcas.append("F1")
            elif marca == "Geely":
                marcas.append("GLC2")
            elif marca == "Changan":
                marcas.append("Benni")
                marcas.append("CS35")
            
            elif marca == "Suzuki":
                marcas.append("Alto")
                marcas.append("Celerio")
                marcas.append("Swift")
                

            return marcas
        except Exception as e:
            print(f"Error al obtener los modelos: {e}")
            return []
    

    def obtenerEspecificaciones(marca,modelo,year):
        
        url= "https://car-api2.p.rapidapi.com/api/bodies",
        params = {
            'sort': 'id',
            'model': modelo,
            'verbose': 'no',
            'direction': 'asc',
            'make': marca,
            'year': year
            }
        headers = {
            'X-RapidAPI-Key': '3dcfb11764mshc48ea40ecb6a0efp1fe268jsn4cf3d3d28ba2',
            'X-RapidAPI-Host': 'car-api2.p.rapidapi.com'
        }
        


        try:
            respuesta = requests.get("https://car-api2.p.rapidapi.com/api/bodies", headers=headers,params=params)
            datos = respuesta.json()
            
            
            # Filtrar las marcas de automóviles
            marcas =  datos["data"][0]
            if marca == "BYD":
                marcas.append("Se debe registrar la informacion de forma manual por el tipo de marca")
            elif marca == "Geely":
                marcas.append("Se debe registrar la informacion de forma manual por el tipo de marca")
            elif marca == "Changan":
                marcas.append("Se debe registrar la informacion de forma manual por el tipo de marca")
            
            elif marca == "Suzuki":
                marcas.append("Se debe registrar la informacion de forma manual por el tipo de marca")

                

            return marcas
        except Exception as e:
            print(f"Error al obtener los modelos: {e}")
            return []
        


class BitacoraRegistro:

    def __init__(self,Conductor,placa,fechaInicio, fechaFinalizacion):
        self.conductor = Conductor
        self.placa = placa
        self.fechaInicio = fechaInicio
        self.fechaFinalizacion = fechaFinalizacion
    

    def generarDatosCsv(self):
        csv = {
            "Conductor": self.conductor,
            "Placa": self.placa,
            "Fecha Inicio": self.fechaInicio,
            "Fecha Finalizacion": self.fechaFinalizacion
        }

        return csv
    



    

        
    





    



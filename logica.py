from typing import Any
from geopy.geocoders import Nominatim
import requests



class Conductor:
    def __init__(self,nombre,apellido, cedula, numLicencia, direccion,vehiculo,pagos,foto):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.numLicencia = numLicencia
        self.direccion = direccion
        # Placa vehiculo se refiere a el vehiculo que usa el conductor
        self.vehiculo = vehiculo
        #Pagos es un atributo que confirma si el conductor se encuentra al dia con os pagos
        self.pagos = pagos
        self.foto = foto

    def __init__(self,nombre,apellido, cedula, numLicencia, direccion,vehiculo,foto, fotoCedula, fotoLicencia,cuotaSemanal):
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
            "Foto": self.foto

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
    numeroIncidente =0

    def __init__(self,nombreIncidente,detalles,fecha,costo,conductor):
        Incidente.numeroIncidente+=1
        self.numeroDeIncidente = Incidente.numeroIncidente
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
    
        
    





    



from pymongo import MongoClient



def conectarBase(coleccion):
    client = MongoClient('mongodb+srv://admin:qFNmpXo6ZZhdhdlB@cluster0.gfywsfy.mongodb.net/',tls=True,tlsAllowInvalidCertificates=True)
    db = client.get_database('T-Rento')
    print(db)
    coll = db.get_collection(coleccion)
    return coll

def obtenerConductores():
    coleccion = conectarBase("Conductores")
    result = coleccion.find()
    return result


def insertarCondcutor(conductor):
    coleccion = conectarBase("Conductores")
    coleccion.insert_one(conductor)


def obtenerConductor(conductor):
    coleccion = conectarBase("Conductores")
    result = coleccion.find(conductor)
    return result


def registrarIncidente(incidente):
    coleccion = conectarBase("Incidentes")
    coleccion.insert_one(incidente)

def obtenerIncidentes():
    coleccion = conectarBase("Incidentes")
    result = coleccion.find()
    return result


def obtenerIncidente(incidente):
    coleccion = conectarBase("Incidentes")
    result = coleccion.find(incidente)
    return result


def registrarVehiculo(vehiculo):
    coleccion = conectarBase("Vehiculos")
    result = coleccion.insert_one(vehiculo)
    return result

def obtenerVehiculos():
    coleccion = conectarBase("Vehiculos")
    result = coleccion.find()
    return result

def obtenerVehiculo(vehiculo):
    coleccion = conectarBase("Vehiculos")
    result = coleccion.find(vehiculo)
    return result    

def editarVehiculo(placa,cambio):
    coleccion = conectarBase("Vehiculos")
    result = coleccion.update_one(placa,cambio)
    return result  


def registrarMantenimiento(mantenimiento):
    coleccion = conectarBase("Mantenimientos")
    result = coleccion.insert_one(mantenimiento)
    return result

def obtenerMantenimientos():
    coleccion = conectarBase("Mantenimientos")
    result = coleccion.find()
    return result


def obtenerMantenimiento(mantenimiento):
    coleccion = conectarBase("Mantenimientos")
    result = coleccion.find(mantenimiento)
    return result

def actualizarMantenimiento(numeroMantenimiento,cambio):
    coleccion = conectarBase("Mantenimientos")
    result = coleccion.update_one(numeroMantenimiento,cambio)
    return result  


def obtenerTallers():
    coleccion = conectarBase("Talleres")
    result = coleccion.find()
    return result



def registrarTaller(taller):
    coleccion = conectarBase("Talleres")
    result = coleccion.insert_one(taller)
    return result

def obtenerTaller(taller):
    coleccion = conectarBase("Talleres")
    result = coleccion.find(taller)
    return result
def editarTaller(taller,cambios):
    coleccion = conectarBase("Talleres")
    result = coleccion.update_one(taller,cambios)
    return result  


def registrarPago(pago):
    coleccion = conectarBase("Pagos")
    result = coleccion.insert_one(pago)
    return result


def obtenerPagos():
    coleccion = conectarBase("Pagos")
    result = coleccion.find()
    return result

def editarPago(comprobante,pago):
    coleccion = conectarBase("Pagos")
    result = coleccion.update_one(comprobante,pago)
    return result   

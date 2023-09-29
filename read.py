import json
import Clases

file_name="vuelos.json"

#Esta funcion lee los objetos de personas.json y los devuelve 
 
def read(file_name):
    objetos = []

    try:
        with open(file_name, "r") as archivo:
            contenido = archivo.read()
            objetos = json.loads(contenido) if contenido else []
        
        return objetos
    except FileNotFoundError:
        with open(file_name, "w") as archivo:
            archivo.write(json.dumps(objetos, indent=4))
        return []

#Esta funcion lee los objetos de personas.json y los devuelve lista

def read_objects(file_name):
    objetos = []

    try:

        with open(file_name, "r") as archivo:
            contenido = archivo.read()
            
            if contenido:
                datos = json.loads(contenido)

                for i in datos:
                    vuelo = Clases.vuelo()
                    vuelo.id_vuelo = i["dni"]
                    vuelo.destino = i["nombre"]
                    vuelo.hora_salida = i["apellidos"]
                    vuelo.plazas_libres = i["fecha_nacimiento"]

                    objetos.append(vuelo)
        
        return objetos
    except FileNotFoundError:
        with open(file_name, "w") as archivo:
            archivo.write(json.dumps(objetos, indent=4))
        return []

def read_pantalla(file_name):
    objetos = read_objects(file_name)

    for i in objetos:
        print("DNI: " + i.dni  +"\nNombre: " + i.nombre + "\nApellidos: " + i.apellidos + "\nFecha nacimiento: " + i.fecha_nacimiento)



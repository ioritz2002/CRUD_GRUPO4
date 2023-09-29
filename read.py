import json
import vuelo
import time

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
                    vuelos = vuelo.Vuelo()
                    vuelos.hora_salida = i["hora_salida"]
                    vuelos.id_vuelo = i["id_vuelo"]
                    vuelos.destino = i["destino"]
                    vuelos.plazas_libres = i["plazas_libres"]

                    objetos.append(vuelos)
        
        return objetos
    except FileNotFoundError:
        with open(file_name, "w") as archivo:
            archivo.write(json.dumps(objetos, indent=4))
        return []

def read_pantalla(file_name):
    objetos = read_objects(file_name)
    
    print("\nFecha de salida " + "\tId vuelo " + "\tDestino " + "\tPlazas libres ")
    for i in objetos:
        print(str(i.hora_salida) + "\t" +  str(i.id_vuelo) + "\t\t" + str(i.destino) + "\t\t" + str(i.plazas_libres))
    print("\n")

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
                    vuelo_obj = vuelo.Vuelo()
                    vuelo_obj.hora_salida = i["hora_salida"]
                    vuelo_obj.id_vuelo = i["id_vuelo"]
                    vuelo_obj.destino = i["destino"]
                    vuelo_obj.plazas_libres = i["plazas_libres"]

                    objetos.append(vuelo_obj)

        objetos_sorted = sorted(objetos, key=lambda x: x.hora_salida, reverse=True)
        
        return objetos_sorted

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

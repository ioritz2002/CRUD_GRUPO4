import json
import time
import datetime
import vuelo

def introducir_fecha(fecha_salida):
    try:
        fecha = datetime.datetime.strptime(fecha_salida, "%Y-%m-%d %H:%M:%S")
        return fecha.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("La fecha es incorrecta")
        raise Exception()
    pass

def read(file_name):
    vuelos = []

    try:
        with open(file_name, "r") as archivo:
            contenido = archivo.read()
            vuelos = json.loads(contenido) if contenido else []

        return vuelos
    except FileNotFoundError:
        with open(file_name, "w") as archivo:
            archivo.write(json.dumps(vuelos, indent=4))

        return []


def write(file_name, vuelo):
    vuelos = read(file_name)
    vuelos.append(vuelo.__dict__)

    with open(file_name, "w") as archivo:
        archivo.write(json.dumps(vuelos, indent=4))
    pass

def create(file_name):
    correct_value = False
    try:

        vu = vuelo.Vuelo()
        vu.id_vuelo = int(time.time())
        vu.destino = input("Introduce el destino del vuelo\n")

        fecha_salida = input("Introduce la fecha y hora de salida\n")
        vu.hora_salida = introducir_fecha(fecha_salida)
        while correct_value == False:
            try:
                vu.plazas_libres = int(input("Introduce el numero de plazas libres para el vuelo\n"))
                correct_value = True
            except ValueError:
                print("Tienes que introducir numeros\n")
                correct_value = False
        

        write(file_name, vu)
    except Exception as e:
        pass
    pass
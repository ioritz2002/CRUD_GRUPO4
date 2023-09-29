import json
import vuelo
file_name = "vuelos.json"

# Función para cargar los vuelos desde el archivo JSON
def cargar_vuelos(file_name):
    try:
        with open(file_name, "r") as archivo:
            vuelos = json.load(archivo)
    except FileNotFoundError:
        vuelos = []
    return vuelos

# Función para guardar los vuelos en el archivo JSON
def guardar_vuelos(vuelos):
    with open(file_name, "w") as archivo:
        json.dump(vuelos, archivo, indent=4)

# Función para modificar un vuelo existente
def actualizar_vuelo(file_name):
    vuelos = cargar_vuelos(file_name)  
    id_modificar = int(input("Ingrese el ID del vuelo que desea modificar: "))
    vuelo_encontrado = False
    for vuelo in vuelos:
        if vuelo['id_vuelo'] == id_modificar:
            vuelo_encontrado = True
            while True:
                print("¿Qué desea modificar?")
                print("1. Número de plazas libres")
                print("2. Destino")
                print("3. Salir")
                opcion = int(input("Ingrese su elección: "))
                if opcion == 1:
                    nuevas_plazas = int(input("Ingrese el nuevo número de plazas libres: "))
                    vuelo['plazas_libres'] = nuevas_plazas
                    print("Número de plazas libres modificado con éxito.")
                elif opcion == 2:
                    nuevo_destino = input("Ingrese el nuevo destino: ")
                    vuelo['destino'] = nuevo_destino
                    print("Destino modificado.")
                elif opcion == 3:
                    break  # Salir del bucle
                else:
                    print("Opción no válida.")
            guardar_vuelos(vuelos)  # Guarda los cambios en el archivo JSON
            print("Vuelo actualizado con éxito.")
            break
    if not vuelo_encontrado:
        print(f"No se encontró un vuelo con el ID {id_modificar}.")












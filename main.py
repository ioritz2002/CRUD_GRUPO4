#!/usr/bin/env python3
import json
file_name = "vuelos.json"

continuar = True
while continuar:

    print("1. Información de los vuelos")
    print("2. Añadir un vuelo")
    print("3. Modificar un vuelo existente")
    print("4. Borrar un vuelo")
    print("0. Salir")
    opcion = int(input("Selecciona una opción: "))


    if opcion == 1:
        print("Informacion de los vuelos")
    
    elif opcion == 2:
        print("Añadir un vuelo")

    elif opcion == 3:
        print("Modificar un vuelo existente")

    elif opcion == 4:
        print("Borrar un vuelo")
    
    elif opcion == 0:
        print("Salir")
        continuar = False
    else:
        print("Opcion no valida")

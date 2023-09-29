#!/usr/bin/env python3
import json
import read
import delete
import create


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
        read.read_pantalla(file_name)
    
    elif opcion == 2:
        create.create(file_name)

    elif opcion == 3:
        print("Modificar un vuelo existente")

    elif opcion == 4:
        delete.eliminar_vuelo(file_name)
    
    elif opcion == 0:
        print("Salir")
        continuar = False
    else:
        print("Opcion no valida")


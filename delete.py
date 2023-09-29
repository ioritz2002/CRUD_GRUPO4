import json
import vuelo
import read

def eliminar_vuelo(id_vuelo, file_name):
    try:
        objetos = read.read_objects(file_name)
        
        vuelo_usuario = input("\n¿Qué vuelo quieres eliminar? ").strip()  # Elimina espacios en blanco alrededor de la entrada del usuario

        vuelo_encontrado = False

        for vuelo in objetos:
            if vuelo_usuario == str(vuelo.id_vuelo).strip():  # Convierte vuelo.id_vuelo a cadena y elimina espacios en blanco alrededor
                objetos.remove(vuelo)
                vuelo_encontrado = True
                break

        if vuelo_encontrado:
            with open(file_name, "w") as archivo:
                # Convertir objetos Vuelo a diccionarios antes de escribir en el archivo
                vuelos_dict = [vuelo.__dict__ for vuelo in objetos]
                json.dump(vuelos_dict, archivo, indent=4)

            print("\nVuelo eliminado correctamente")
        else:
            print("\nVuelo no encontrado")

    except FileNotFoundError:
        print("El archivo no existe.")
        return []

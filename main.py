from lista_doble import ListaDoblementeEnlazada

def menu():
    lista = ListaDoblementeEnlazada()
    
    while True:
        print("\n--- MENÚ LISTA DOBLE ENLAZADA ---")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por valor (Carnet)")
        print("4. Mostrar lista en consola")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1" or opcion == "2":
            nom = input("Nombre: ")
            ape = input("Apellido: ")
            car = input("Carnet: ")
            if opcion == "1":
                lista.insertar_al_principio(nom, ape, car)
            else:
                lista.insertar_al_final(nom, ape, car)
            print("¡Nodo agregado y gráfica generada!")

        elif opcion == "3":
            car_eliminar = input("Ingrese el carnet del estudiante a eliminar: ")
            if lista.eliminar_por_valor(car_eliminar):
                print(f"¡Estudiante con carnet {car_eliminar} eliminado!")
            else:
                print("No se encontró ningún estudiante con ese carnet.")

        elif opcion == "4":
            print("\nEstado actual de la lista:")
            lista.mostrar_lista()

        elif opcion == "5":
            print("Cerrando programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
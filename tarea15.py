# Programa: Agenda Telefónica
# Descripción: Permite registrar, mostrar, buscar y eliminar contactos.
# Crear el diccionario vacío para almacenar los contactos
agenda = {}
# Función para agregar un contacto
def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    agenda[nombre] = telefono
    print("Contacto agregado correctamente.")
# Función para mostrar todos los contactos
def mostrar_contactos():
    if len(agenda) == 0:
        print("La agenda está vacía.")
    else:
        print("\n--- CONTACTOS ---")
        for nombre in agenda:
            print("Nombre:", nombre, "- Teléfono:", agenda[nombre])
# Función para buscar un contacto
def buscar_contacto():
    nombre = input("Ingrese el nombre que desea buscar: ")
    if nombre in agenda:
        print("Contacto encontrado.")
        print("Nombre:", nombre)
        print("Teléfono:", agenda[nombre])
    else:
        print("El contacto no existe en la agenda.")
# Función para eliminar un contacto
def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado correctamente.")
    else:
        print("El contacto no existe en la agenda.")
# Menú principal
while True:
    print("\n===== AGENDA TELEFÓNICA =====")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        mostrar_contactos()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
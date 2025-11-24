from GestionRegistros import GestionRegistros


gestor = GestionRegistros()

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar persona")
    print("2. Buscar persona por documento")
    print("3. Modificar email")
    print("4. Eliminar persona")
    print("5. Listar registros")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        documento = int(input("Documento: "))
        email = input("Email: ")
        gestor.registrar_persona(nombre, apellido, edad, documento, email)

    elif opcion == "2":
        doc = int(input("Documento: "))
        persona = gestor.buscar_por_documento(doc)
        if persona:
            gestor.mostrar_persona(persona)
        else:
            print(" No encontrada.")

    elif opcion == "3":
        doc = int(input("Documento: "))
        nuevo_email = input("Nuevo email: ")
        gestor.modificar_email(doc, nuevo_email)

    elif opcion == "4":
        doc = int(input("Documento: "))
        gestor.eliminar_persona(doc)

    elif opcion == "5":
        gestor.listar_registros()

    elif opcion == "6":
        print(" Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")


    
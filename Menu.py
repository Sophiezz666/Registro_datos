from GestionRegistros import GestionRegistros
from Persona import Persona

def mostrar_menu():
    print("\n--- Sistema de Registro ---")
    print("1. Registrar nueva persona")
    print("2. Buscar por documento")
    print("3. Modificar datos (Email)")
    print("4. Salir")
    return input("Seleccione una opción: ")

def obtener_datos_registro():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    documento = int(input("Documento: "))
    email = input("Email: ")
    return nombre, apellido, edad, documento, email

def main():
    gestor = GestionRegistros()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            try:
                nombre, apellido, edad, documento, email = obtener_datos_registro()
                gestor.registrar_persona(nombre, apellido, edad, documento, email)
            except ValueError:
                print("Error en el tipo de dato. Ingrese valores válidos.")
            
        elif opcion == "2":
            try:
                doc = int(input("Ingrese el documento a buscar: "))
                persona_encontrada = gestor.buscar_por_documento(doc)
                if persona_encontrada:
                    print(f"ENCONTRADO: {persona_encontrada.nombre} {persona_encontrada.apellido}, Email: {persona_encontrada.email}")
                else:
                    print("Persona no encontrada.")
            except ValueError:
                 print("Ingrese un número para el documento.")
                 
        elif opcion == "3":
            try:
                doc = int(input("Ingrese el documento de la persona a modificar: "))
                gestor.modificar_persona(doc)
            except ValueError:
                 print("Ingrese un número para el documento.")
                 
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
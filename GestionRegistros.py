from Persona import Persona   # Importamos la clase Persona para poder crear objetos de tipo Persona

class GestionRegistros:
    def __init__(self):
        # Lista privada donde se almacenan los objetos Persona
        self.__registros = []

    # --- Getter ---
    @property
    def registros(self):
        # Devuelve la lista de registros (solo lectura)
        return self.__registros

    # --- Setter ---
    @registros.setter
    def registros(self, lista):
        # Valida que lo que se asigne sea una lista
        if not isinstance(lista, list):
            raise ValueError("Los registros deben ser una lista.")
        self.__registros = lista

    # --- Métodos de gestión ---
    def registrar_persona(self, nombre, apellido, edad, documento, email):
        # Crea un nuevo objeto Persona y asigna sus atributos usando setters
        persona = Persona()
        try:
            persona.nombre = nombre
            persona.apellido = apellido
            persona.edad = edad
            persona.documento = documento
            persona.email = email

            # Se obtiene la lista actual de registros y se agrega la nueva persona
            registros_actuales = self.registros
            registros_actuales.append(persona)

            # Se actualiza la lista usando el setter
            self.registros = registros_actuales
            print(" Registro exitoso.")
        except ValueError as e:
            # Si algún setter lanza error (ejemplo: email inválido), se captura aquí
            print(f"Error: {e}")

    def buscar_por_documento(self, documento):
        # Recorre la lista de registros y devuelve la persona cuyo documento coincida
        for persona in self.registros:
            if persona.documento == documento:
                return persona
        return None  # Si no encuentra nada, devuelve None

    def modificar_email(self, documento, nuevo_email):
        # Busca la persona por documento
        persona = self.buscar_por_documento(documento)
        if persona:
            try:
                # Si existe, intenta actualizar el email usando el setter
                persona.email = nuevo_email
                print(" Email actualizado.")
            except ValueError as e:
                # Si el email no es válido, se muestra el error
                print(f"Error: {e}")
        else:
            print(" Persona no encontrada.")

    def eliminar_persona(self, documento):
        # Busca la persona por documento
        persona = self.buscar_por_documento(documento)
        if persona:
            # Si existe, se elimina de la lista
            registros_actuales = self.registros
            registros_actuales.remove(persona)
            self.registros = registros_actuales
            print(" Persona eliminada.")
        else:
            print(" Persona no encontrada.")

    def mostrar_persona(self, persona):
        # Muestra los datos de una persona usando getters
        print(f"Nombre: {persona.nombre}")
        print(f"Apellido: {persona.apellido}")
        print(f"Edad: {persona.edad}")
        print(f"Documento: {persona.documento}")
        print(f"Email: {persona.email}")
        print("-" * 30)

    def listar_registros(self):
        # Muestra todas las personas registradas
        if not self.registros:
            print("No hay registros.")
        else:
            for persona in self.registros:
                self.mostrar_persona(persona)

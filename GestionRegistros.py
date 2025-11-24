from Persona import Persona # Importamos la clase Persona

class GestionRegistros:
    def __init__(self):
        # La lista central donde se almacenan todos los objetos Persona
        self.registros = []

    def registrar_persona(self, nombre, apellido, edad, documento, email):
        """
        Crea una nueva instancia de Persona y utiliza los setters para inicializarla 
        y validar los datos.
        """
        nueva_persona = Persona() 
        
        try:
            # Utilizamos los setters para asignar y validar:
            nueva_persona.nombre = nombre
            nueva_persona.apellido = apellido
            nueva_persona.edad = edad
            nueva_persona.documento = documento  # Aquí se ejecuta la validación del documento
            nueva_persona.email = email          # Aquí se ejecuta la validación del email

            self.registros.append(nueva_persona)
            print("✅ Registro exitoso.")
            return nueva_persona
            
        except ValueError as e:
            # Capturamos errores de validacion (documento negativo, email invalido, etc.)
            print(f"Error al registrar: {e}")
            return None # Retorna None si el registro falla

    def buscar_por_documento(self, documento: int):
        for persona in self.registros:
            # Usamos el getter: persona.documento
            if persona.documento == documento:
                return persona
        return None

    def modificar_persona(self, documento: int):
        """Permite modificar el email de una persona buscada."""
        persona = self.buscar_por_documento(documento)
        
        if persona:
            print(f"\n--- Modificando a {persona.nombre} {persona.apellido} ---")
            nuevo_email = input("Ingrese el NUEVO EMAIL: ")
            
            try:
                # Usamos el setter para modificar y validar el nuevo email
                persona.email = nuevo_email 
                print("Email actualizado correctamente.")
            except ValueError as e:
                print(f"No se pudo actualizar el email: {e}")
        else:
            print("Persona no encontrada con ese documento.")
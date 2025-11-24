class Persona:
    def __init__(self):
        pass

    @property
    def nombre(self):
        return self._nombre 
    
    @nombre.setter
    def nombre(self,nombre:str):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self,apellido:str):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self,edad:int):
        if isinstance(edad, int) and edad > 0:
            self._documento = edad
        else:
            raise ValueError("La edad debe ser un numero entero positivo.")

    @property
    def documento(self):
        return self._documento
    
    @documento.setter
    def documento(self,documento:int):
        if isinstance(documento, int) and documento > 0:
            self._documento = documento
        else:
            raise ValueError("El documento debe ser un numero entero positivo.")

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email: str):
        email_valido = email.count('@') == 1 and '.' in email.split('@')[-1] # Verificacion
        if email_valido:

            self._email = email # Si es valido se asigna
        else:
            raise ValueError("Formato invalido. Debe contener un '@' y  '.") # Si NO es válido

    


    


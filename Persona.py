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
        self._edad = edad

    @property
    def documento(self):
        return self._documento
    @documento.setter
    def documento(self,documento:int):
        self._documento = documento
    
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,email:str):
        self._email = email

    


    


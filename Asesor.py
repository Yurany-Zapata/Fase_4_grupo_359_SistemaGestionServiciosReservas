class AsesorError(Exception):
    pass

class Asesor:
    def __init__(self, nombre, especialidad):
        try:
            if not nombre or not isinstance(nombre, str):
                raise AsesorError("El nombre no es válido")
            if not especialidad or not isinstance(especialidad, str):
                raise AsesorError("La especialidad no es válida")
            
            self.__nombre = nombre
            self.__especialidad = especialidad

        except AsesorError as error:
            with open("logs.txt", "a") as log:
                log.write(f"Error Asesor: {error}\n")
            print(f"Error: {error}")
    
    def get_nombre(self):
        return self.__nombre
    
    def get_especialidad(self):
        return self.__especialidad

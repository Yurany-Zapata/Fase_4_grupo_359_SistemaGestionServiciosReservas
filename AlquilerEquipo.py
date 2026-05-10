from Servicio import Servicio
from Cliente import Cliente
from Equipo import Equipo
from datetime import datetime

class AlquilerEquipoError(Exception):
    pass

class AlquilerEquipo(Servicio):
    def __init__(self, cliente, equipo, fecha, horas):
        try:
            if not isinstance(cliente, Cliente):
                raise AlquilerEquipoError("El cliente no es válido")
            if not equipo or not isinstance(equipo, Equipo):
                raise AlquilerEquipoError("El equipo no es válido")
            if not fecha or not isinstance(fecha, datetime):
                raise AlquilerEquipoError("La fecha no es válida")
            if not horas:
                raise AlquilerEquipoError("La cantidad de horas no puede estar vacía")
            
            self.__cliente = cliente
            self.__equipo = equipo
            self.__fecha = fecha
            self.__horas = horas

        except AlquilerEquipoError as error:
            with open("logs.txt", "a") as log:
                log.write(f"Error Alquiler Equipo: {error}\n")
            print(f"Error: {error}")

    def get_cliente(self):
        return self.__cliente
    
    def get_equipo(self):
        return self.__equipo

    def get_fecha(self):
        return self.__fecha

    def get_horas(self):
        return self.__horas

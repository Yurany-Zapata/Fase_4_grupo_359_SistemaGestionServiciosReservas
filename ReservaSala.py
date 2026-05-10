from Cliente import Cliente
from Servicio import Servicio
from Sala import Sala
from datetime import datetime

class ReservaSalaError(Exception):
    pass

class ReservaSala(Servicio):
    def __init__(self, cliente, sala, fecha, horas):
        try:
            if not isinstance(cliente, Cliente):
                raise ReservaSalaError("El cliente no es válido")
            if not sala or not isinstance(sala, Sala):
                raise ReservaSalaError("La sala no es válida")
            if not fecha or not isinstance(fecha, datetime):
                raise ReservaSalaError("La fecha no es válida")
            if not horas:
                raise ReservaSalaError("La cantidad de horas no puede estar vacía")
            
            self.__cliente = cliente
            self.__sala = sala
            self.__fecha = fecha
            self.__horas = horas

        except ReservaSalaError as error:
            with open("logs.txt", "a") as log:
                log.write(f"Error Reserva Sala: {error}\n")
            print(f"Error: {error}")

    def get_cliente(self):
        return self.__cliente
    
    def get_sala(self):
        return self.__sala
    
    def get_fecha(self):
        return self.__fecha

    def get_horas(self):
        return self.__horas

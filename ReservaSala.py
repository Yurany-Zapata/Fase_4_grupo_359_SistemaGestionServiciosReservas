from enum import Enum
from Cliente import Cliente
from Servicio import Servicio

class ReservaSalaError(Exception):
    pass

class Sala(Enum):
    SALA_ESTUDIOS = 1
    SALA_AUDIOVISUAL = 2
    SALA_INVESTIGACION = 3
    SALA_IA = 4

class ReservaSala(Servicio):
    def __init__(self, cliente, sala, horas):
        try:
            if not isinstance(cliente, Cliente):
                raise ReservaSalaError("El cliente no es válido")
            if not sala or not isinstance(sala, Sala):
                raise ReservaSalaError("La sala no es válida")
            if not horas:
                raise ReservaSalaError("La cantidad de horas no puede estar vacía")
            
            self.__cliente = cliente
            self.__sala = sala
            self.__horas = horas

        except ReservaSalaError as e:
            with open("logs.txt", "a") as log:
                log.write(f"Error Reserva Sala: {e}\n")
            print(f"Error: {e}")

    def get_cliente(self):
        return self.__cliente
    
    def get_sala(self):
        return self.__sala

    def get_horas(self):
        return self.__horas

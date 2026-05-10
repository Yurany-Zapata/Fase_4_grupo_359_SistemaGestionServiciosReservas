from Servicio import Servicio
from Cliente import Cliente
from Asesor import Asesor
from TipoAsesoria import TipoAsesoria
from datetime import datetime

class AsesoriaPersonalizadaError(Exception):
    pass

class AsesoriaPersonalizada(Servicio):
    def __init__(self, cliente, asesor, tipo_asesoria, fecha, horas):
        try:
            if not isinstance(cliente, Cliente):
                raise AsesoriaPersonalizadaError("El cliente no es válido")
            if not asesor or not isinstance(asesor, Asesor):
                raise AsesoriaPersonalizadaError("El asesor no es válido")
            if not tipo_asesoria or not isinstance(tipo_asesoria, TipoAsesoria):
                raise AsesoriaPersonalizadaError("El tipo de asesoría no es válido")
            if not fecha or not isinstance(fecha, datetime):
                raise AsesoriaPersonalizadaError("La fecha no es válida")
            if not horas:
                raise AsesoriaPersonalizadaError("La cantidad de horas no puede estar vacía")
            
            self.__cliente = cliente
            self.__asesor = asesor
            self.__tipo_asesoria = tipo_asesoria
            self.__fecha = fecha
            self.__horas = horas

        except AsesoriaPersonalizadaError as error:
            with open("logs.txt", "a") as log:
                log.write(f"Error Asesoría Personalizada: {error}\n")
            print(f"Error: {error}")

    def get_cliente(self):
        return self.__cliente
    
    def get_asesor(self):
        return self.__asesor
    
    def get_tipo_asesoria(self):
        return self.__tipo_asesoria
    
    def get_fecha(self):
        return self.__fecha

    def get_horas(self):
        return self.__horas

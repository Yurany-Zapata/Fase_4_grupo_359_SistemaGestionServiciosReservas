from enum import Enum

class ClienteError(Exception):
    pass

class TipoDocumento(Enum):
    TARJETA_IDENTIDAD = "TI"
    CEDULA_CIUDADANIA = "CC"
    PASAPORTE = "PA"
    CEDULA_EXTRANJERIA = "CE"

class Cliente:
    def __init__(self, tipo_documento, numero_documento, nombre, correo, telefono):
        try:
            if not tipo_documento or not isinstance(tipo_documento, TipoDocumento):
                raise ClienteError("El tipo de documento no es válido")
            if not numero_documento:
                raise ClienteError("El número de documento no puede estar vacío")
            if not nombre:
                raise ClienteError("El nombre no puede estar vacío")
            if not correo or "@" not in correo:
                raise ClienteError("Correo inválido")
            if not telefono:
                raise ClienteError("El teléfono no puede estar vacío")

            self.__tipo_documento = tipo_documento
            self.__numero_documento = numero_documento
            self.__nombre = nombre
            self.__correo = correo
            self.__telefono = telefono

        except ClienteError as e:
            with open("logs.txt", "a") as log:
                log.write(f"Error Cliente: {e}\n")
            print(f"Error: {e}")

    def get_tipo_documento(self):
        return self.__tipo_documento
    
    def get_numero_documento(self):
        return self.__numero_documento

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo
    
    def get_telefono(self):
        return self.__telefono

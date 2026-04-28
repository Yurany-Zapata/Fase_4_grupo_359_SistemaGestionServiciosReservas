class ClienteError(Exception):
    pass

class Cliente:
    def __init__(self, nombre, correo):
        try:
            if not nombre:
                raise ClienteError("El nombre no puede estar vacío")
            if "@" not in correo:
                raise ClienteError("Correo inválido")

            self.__nombre = nombre
            self.__correo = correo

        except ClienteError as e:
            with open("logs.txt", "a") as log:
                log.write(f"Error Cliente: {e}\n")
            print(f"Error: {e}")

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

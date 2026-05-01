from Cliente import Cliente

class ServicioError(Exception):
    pass

class Servicio:
    def __init__(self, cliente):
        try:
            if not isinstance(cliente, Cliente):
                raise ServicioError("El cliente no es válido")
            
            self.__cliente = cliente

        except ServicioError as e:
            with open("logs.txt", "a") as log:
                log.write(f"Error Servicio: {e}\n")
            print(f"Error: {e}")

    def get_cliente(self):
        return self.__cliente

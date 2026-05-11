from logger import log_error, log_evento

class GestorSistema:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def agregar_cliente(self, cliente):
        try:
            if not cliente:
                raise ValueError("Cliente inválido")

            self.clientes.append(cliente)
            log_evento("Cliente agregado correctamente")

        except Exception as e:
            log_error("GestorSistema - agregar_cliente", e)

    def agregar_servicio(self, servicio):
        try:
            if not servicio:
                raise ValueError("Servicio inválido")

            self.servicios.append(servicio)
            log_evento("Servicio agregado")

        except Exception as e:
            log_error("GestorSistema - agregar_servicio", e)

    def crear_reserva(self, servicio):
        try:
            if not servicio:
                raise ValueError("Servicio no válido")

            reserva = {
                "servicio": servicio,
                "estado": "PENDIENTE"
            }

            self.reservas.append(reserva)
            log_evento("Reserva creada")

            return reserva

        except Exception as e:
            log_error("GestorSistema - crear_reserva", e)

    def confirmar_reserva(self, reserva):
        try:
            if not reserva:
                raise ValueError("Reserva inválida")

            reserva["estado"] = "CONFIRMADA"
            log_evento("Reserva confirmada")

        except Exception as e:
            log_error("GestorSistema - confirmar_reserva", e)
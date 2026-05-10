from Cliente import Cliente
from Cliente import TipoDocumento
from ReservaSala import ReservaSala
from Sala import Sala
from datetime import datetime

mi_cliente = Cliente(TipoDocumento.CEDULA_CIUDADANIA, "123456", "Usuario Prueba", "usuario.prueba@gmail.com", "3111111")
mi_sala = Sala.SALA_AUDIOVISUAL
fecha = datetime.strptime("20-05-2026 10:00:00", "%d-%m-%Y %H:%M:%S")
mi_servicio = ReservaSala(mi_cliente, mi_sala, fecha, 2)
print(mi_servicio.get_cliente().get_tipo_documento().value)
print(mi_servicio.get_cliente().get_nombre())
print(mi_servicio.get_sala().value)
print(mi_servicio.get_fecha())

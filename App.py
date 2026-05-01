from Cliente import Cliente
from Cliente import TipoDocumento
from ReservaSala import ReservaSala
from ReservaSala import Sala

mi_cliente = Cliente(TipoDocumento.CEDULA_CIUDADANIA, "123456", "Usuario Prueba", "usuario.prueba@gmail.com", "3111111")
mi_sala = Sala.SALA_AUDIOVISUAL
mi_servicio = ReservaSala(mi_cliente, mi_sala)  
print(mi_servicio.get_cliente().get_tipo_documento().value)
print(mi_servicio.get_cliente().get_nombre())
print(mi_servicio.get_sala().value)
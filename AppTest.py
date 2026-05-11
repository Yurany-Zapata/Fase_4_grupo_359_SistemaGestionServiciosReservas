from Cliente import Cliente, TipoDocumento
from ReservaSala import ReservaSala, Sala
from GestorSistema import GestorSistema

def main():

    sistema = GestorSistema()

    # Caso válido
    try:
        c1 = Cliente(TipoDocumento.CEDULA_CIUDADANIA, "123", "Laura", "laura@gmail.com", "123")
        sistema.agregar_cliente(c1)

        s1 = ReservaSala(c1, Sala.SALA_AUDIOVISUAL, 2)
        sistema.agregar_servicio(s1)

        reserva = sistema.crear_reserva(s1)
        sistema.confirmar_reserva(reserva)

    except Exception as e:
        print("Error general:", e)


    # Caso con error
    try:
        c2 = Cliente(None, "", "", "correo", "")
        sistema.agregar_cliente(c2)
    except:
        pass


    print("Sistema funcionando")

if __name__ == "__main__":
    main()
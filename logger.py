import datetime

def log_error(origen, error):
    with open("logs.txt", "a") as log:
        log.write(f"{datetime.datetime.now()} - {origen} - ERROR: {error}\n")

def log_evento(mensaje):
    with open("logs.txt", "a") as log:
        log.write(f"{datetime.datetime.now()} - EVENTO: {mensaje}\n")
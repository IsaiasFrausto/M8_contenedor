import random

def procesar_turno(equipo, numero_aleatorio, tiempo):
    # Maneja las acciones de disparos y goles para un equipo
    if 1 <= numero_aleatorio <= 100:
        print(f"Minuto {tiempo}: {equipo} dispara desviado.")
    elif 101 <= numero_aleatorio <= 200:
        print(f"Minuto {tiempo}: {equipo} dispara y el portero ataja la pelota.")
    elif 201 <= numero_aleatorio <= 250:
        print(f"Minuto {tiempo}: {equipo} anoto gol de cabeza.")
        return 1
    elif 251 <= numero_aleatorio <= 300:
        print(f"Minuto {tiempo}: {equipo} anoto gol de penal.")
        return 1
    elif 301 <= numero_aleatorio <= 350:
        print(f"Minuto {tiempo}: {equipo} anoto gol con el pie.")
        return 1
    return 0

def cambiar_turno(turno_actual):
    # Alterna entre 'chivas' y 'atlas'
    if turno_actual == 'chivas':
        return 'atlas'
    else:
        return 'chivas'

def mostrar_resultado(goles_chivas, goles_atlas):
    # Imprime el resultado final del partido
    print("\nResultado final:")
    print(f"Chivas: {goles_chivas} - Atlas: {goles_atlas}")


def simular_partido():
    # Inicializacion de variables
    goles_chivas = 0
    goles_atlas = 0
    tiempo = 0
    turno_actual = random.choice(['chivas', 'atlas'])

    print("Iniciando el partido entre Chivas y Atlas...\n")

    #Simulacion del partido
    for tiempo in range(1, 91):
        numero_aleatorio = random.randint(1, 350)
        if turno_actual == 'chivas':
            goles_chivas += procesar_turno('Chivas', numero_aleatorio, tiempo)
        else: # Atlas
            goles_atlas += procesar_turno('Atlas', numero_aleatorio, tiempo)
        turno_actual = cambiar_turno(turno_actual)

    # Fin del partido
    mostrar_resultado(goles_chivas, goles_atlas)

simular_partido()
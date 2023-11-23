# Importar librerías necesarias
import random

# Definir la base de conocimiento
base_conocimiento = {
    'ruta1': {
       'paradas': ['estacion_A', 'estacion_B', 'estacion_C', 'estacion_D'],
        'horarios': {
            'estacion_A': [8, 10, 12, 14, 16],
            'estacion_B': [8, 10, 12, 14, 16],
            'estacion_C': [9, 11, 13, 15, 17],
            'estacion_D': [9, 11, 13, 15, 17]
        },
        'tarifas': {
            'estacion_A-estacion_B': 1000,
            'estacion_B-estacion_C': 1500,
            'estacion_C-estacion_D': 2000
        }
    },
    'ruta2': {
        'paradas': ['estacion_A', 'estacion_B', 'estacion_E', 'estacion_F', 'estacion_D'],
        'horarios': {
            'estacion_A': [9, 11, 13, 15, 17],
            'estacion_B': [9, 11, 13, 15, 17],
            'estacion_E': [10, 12, 14, 16, 18],
            'estacion_F': [10, 12, 14, 16, 18],
            'estacion_D': [11, 13, 15, 17, 19]
        },
        'tarifas': {
            'estacion_A-estacion_B': 1200,
            'estacion_B-estacion_E': 2000,
            'estacion_E-estacion_F': 1500,
            'estacion_F-estacion_D': 1800
        }
    }
}

# Definir las reglas de inferencia
def encontrar_mejor_ruta(origen, destino):
    rutas = list(base_conocimiento.keys())
    ruta = random.choice(rutas)
    paradas = base_conocimiento[ruta]['paradas']
    horarios = base_conocimiento[ruta]['horarios']
    tarifas = base_conocimiento[ruta]['tarifas']
    hora_salida = random.choice(horarios[origen])
    hora_llegada = random.choice(horarios[destino])
    precio = 0
    for i in range(paradas.index(origen), paradas.index(destino)):
        precio += tarifas[f"{paradas[i]}-{paradas[i+1]}"]
    return ruta, hora_salida, hora_llegada, precio

# Desarrollar la interfaz de usuario
print("Ingrese su punto de partida:")
origen = input()
print("Ingrese su destino:")
destino = input()
ruta, hora_salida, hora_llegada, precio = encontrar_mejor_ruta(origen, destino)
print(f"La mejor ruta para ir desde {origen} hasta {destino} es la ruta {ruta}.")
print(f"El horario de salida es a las {hora_salida} y el horario de llegada es a las {hora_llegada}.")
print(f"El precio del pasaje es {precio}.")


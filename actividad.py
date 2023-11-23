# Importar librerías necesarias
import random

# Definir la base de conocimiento
base_conocimiento = {
    'ruta1': {
        'paradas': ['A', 'B', 'C', 'D'],
        'horarios': {
            'A': [8, 10, 12, 14, 16],
            'B': [8, 10, 12, 14, 16],
            'C': [9, 11, 13, 15, 17],
            'D': [9, 11, 13, 15, 17]
        },
        'tarifas': {
            'A-B': 1000,
            'B-C': 1500,
            'C-D': 2000
        }
    },
    'ruta2': {
        'paradas': ['A', 'B', 'E', 'F', 'D'],
        'horarios': {
            'A': [9, 11, 13, 15, 17],
            'B': [9, 11, 13, 15, 17],
            'E': [10, 12, 14, 16, 18],
            'F': [10, 12, 14, 16, 18],
            'D': [11, 13, 15, 17, 19]
        },
        'tarifas': {
            'A-B': 1200,
            'B-E': 2000,
            'E-F': 1500,
            'F-D': 1800
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


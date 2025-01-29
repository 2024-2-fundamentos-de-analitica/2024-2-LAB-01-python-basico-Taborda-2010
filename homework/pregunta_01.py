"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    total = 0
    with open('files/input/data.csv', 'r') as archivo:
        for fila in archivo:
            partes = fila.split('\t')

            total += int(partes[1])

    return total

print(pregunta_01())

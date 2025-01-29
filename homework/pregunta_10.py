"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    salida = []
    with open('files/input/data.csv', 'r') as archivo:
        for fila in archivo:
            partes = fila.strip().split('\t')
            letra_col1 = partes[0]
            num_col4 = len(partes[3].split(","))
            num_col5 = len(partes[4].split(","))
            salida.append((letra_col1, num_col4, num_col5))

    return salida


print(pregunta_10())
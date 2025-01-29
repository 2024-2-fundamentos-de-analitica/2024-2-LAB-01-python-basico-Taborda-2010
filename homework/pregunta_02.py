"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    conteo = {}
    with open('files/input/data.csv', 'r') as archivo:
        for fila in archivo:
            inicial = fila[0]

            if inicial in conteo:
                conteo[inicial] += 1
            else:
                conteo[inicial] = 1

        ordenado = sorted(conteo.items())

    return (ordenado)

print(pregunta_02())

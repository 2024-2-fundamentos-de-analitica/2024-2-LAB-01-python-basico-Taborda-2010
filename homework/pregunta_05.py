"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    datos = {}
    with open('files/input/data.csv', 'r') as archivo:
        for fila in archivo:
            inicial = fila[0]
            partes = fila.split('\t')
            numero = int(partes[1])
            if inicial in datos:
                max_val, min_val = datos[inicial]
                datos[inicial] = max(max_val, numero), min(min_val, numero)
            else:
                datos[inicial] = numero, numero

        ordenado = [(clave, max_val, min_val) for clave, (max_val, min_val) in sorted(datos.items())]
    return (ordenado)

print(pregunta_05())

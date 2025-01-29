"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    total_por_letra = {}
    with open('files/input/data.csv', 'r') as archivo:
        for fila in archivo:
            partes = fila.strip().split('\t')
            valores = partes[4].split(",")
            for valor in valores:
                clave_valor = valor.split(":")
                num = int(clave_valor[1])

                letra_col1 = partes[0]
                if letra_col1 in total_por_letra:
                    total_por_letra[letra_col1] += num
                else:
                    total_por_letra[letra_col1] = num
        total_por_letra_ordenado = dict(sorted(total_por_letra.items()))

        return total_por_letra_ordenado

print(pregunta_12())

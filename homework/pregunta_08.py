"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
    (1, ['B', 'E']),
    (2, ['A', 'E']),
    (3, ['A', 'B', 'D', 'E']),
    (4, ['B', 'E']),
    (5, ['B', 'C', 'D', 'E']),
    (6, ['A', 'B', 'C', 'E']),
    (7, ['A', 'C', 'D', 'E']),
    (8, ['A', 'B', 'D', 'E']),
    (9, ['A', 'B', 'C', 'E'])]

    """
    registros = {}
    with open('files/input/data.csv', 'r') as archivo:
        for fila in archivo:
            partes = fila.strip().split('\t')
            valor_col2 = int(partes[1])
            letra_col1 = partes[0]
            if valor_col2 in registros:
                if letra_col1 not in registros[valor_col2]:
                    registros[valor_col2].append(letra_col1)
            else:
                registros[valor_col2] = [letra_col1]

    resultado = [(clave, sorted(lista_letras)) for clave, lista_letras in sorted(registros.items())]
    return resultado

print(pregunta_08())

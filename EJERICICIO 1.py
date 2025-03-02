def buscar_valor(matriz, valor):
    """Función para buscar un valor en una matriz bidimensional"""
    for i in range(len(matriz)):  # Recorre las filas
        for j in range(len(matriz[i])):  # Recorre las columnas
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz"

# Definir una matriz 3x3
matriz = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]

# Definir el número a buscar directamente en el código
valor_buscado = 30  # Puedes cambiar este número para probar

# Llamar a la función y mostrar el resultado
print(buscar_valor(matriz, valor_buscado))
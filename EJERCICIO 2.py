def bubble_sort_fila(matriz, fila):
    """Función que ordena una fila específica de la matriz usando Bubble Sort"""
    n = len(matriz[fila])
    for i in range(n - 1):
        for j in range(n - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:  # Comparación de elementos
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]  # Intercambio

# Definir una matriz 3x3
matriz = [
    [8, 3, 5],
    [2, 9, 4],
    [7, 6, 1]
]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (fila con índice 1)
fila_a_ordenar = 1
bubble_sort_fila(matriz, fila_a_ordenar)

# Mostrar matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
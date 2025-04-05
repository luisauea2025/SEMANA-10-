# Escritura de Archivo de Texto

# Abrimos (o creamos si no existe) el archivo 'my_notes.txt' en modo escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("1. Recordar estudiar para el examen de informática.\n")
    file.write("2. Revisar los conceptos de seguridad de la información.\n")
    file.write("3. Subir la tarea al repositorio de GitHub antes del lunes.\n")

# Lectura de Archivo de Texto

# Abrimos el archivo en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos línea por línea utilizando un bucle y el método readline()
    print("Contenido del archivo:")
    linea = file.readline()
    while linea:
        # Mostramos cada línea en la consola
        print(linea.strip())  # .strip() elimina el salto de línea al final
        linea = file.readline()

# El archivo se cierra automáticamente al salir del bloque 'with'
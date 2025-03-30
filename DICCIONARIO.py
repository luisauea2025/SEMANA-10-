# Crear un diccionario llamado informacion_personal con datos ficticios
informacion_personal = {
    "nombre": "Ana Gómez",
    "edad": 28,
    "ciudad": "Quito",
    "profesion": "Diseñadora Gráfica"
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Guayaquil"

# Verificar si la clave "telefono" existe en el diccionario y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminar la clave "edad" del diccionario porque no es necesaria
del informacion_personal["edad"]

# Imprimir el diccionario final
print("Información personal actualizada:")
print(informacion_personal)


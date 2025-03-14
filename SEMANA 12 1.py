# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)

temperaturas = [
    [   # Ciudad 1 - Tena
        [   # Semana 1
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 82},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 92}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 93}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 91},
            {"day": "Domingo", "temp": 95}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 91}
        ]
    ],
    [   # Ciudad 2 - Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 79}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [   # Ciudad 3 - Esmeraldas
        [   # Semana 1
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 94},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3 (añadida para igualar las demás ciudades)
            {"day": "Lunes", "temp": 88},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 4 (añadida para igualar las demás ciudades)
            {"day": "Lunes", "temp": 87},
            {"day": "Martes", "temp": 89},
            {"day": "Miércoles", "temp": 91},
            {"day": "Jueves", "temp": 88},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 82},
            {"day": "Domingo", "temp": 79}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Tena", "Quito", "Esmeraldas"]

for i, ciudad in enumerate(temperaturas):
    print(f"\nPromedio de temperaturas para {ciudades[i]}:")
    for j, semana in enumerate(ciudad):
        suma = sum(dia['temp'] for dia in semana)
        promedio = suma / len(semana)
        print(f"  Semana {j+1}: {promedio:.2f}°C")


        def calcular_temperatura_promedio(temperaturas, nombres_ciudades):
            """
            Calcula la temperatura promedio de cada ciudad a lo largo de todas las semanas.
            :param temperaturas: Lista 3D con datos de temperaturas por ciudad, semana y día.
            :param nombres_ciudades: Lista con los nombres de las ciudades.
            :return: Diccionario con los promedios de temperatura por ciudad.
            """
            promedios_ciudades = {}

            for i, ciudad in enumerate(temperaturas):
                total_temp = 0
                total_dias = 0

                for semana in ciudad:
                    for dia in semana:
                        total_temp += dia['temp']
                        total_dias += 1

                promedio = total_temp / total_dias
                promedios_ciudades[nombres_ciudades[i]] = round(promedio, 2)

            return promedios_ciudades


        # Datos de las temperaturas (se mantiene la estructura proporcionada)
        # Nombres de las ciudades
        ciudades = ["Tena", "Quito", "Esmeraldas"]

        # Llamar a la función y mostrar los resultados
        resultados = calcular_temperatura_promedio(temperaturas, ciudades)
        for ciudad, promedio in resultados.items():
            print(f"Temperatura promedio en {ciudad}: {promedio}°C")

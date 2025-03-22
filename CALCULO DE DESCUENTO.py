def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento en función del monto total de la compra y el porcentaje de descuento.
    :param monto_total: float - Monto total de la compra
    :param porcentaje_descuento: float - Porcentaje de descuento a aplicar (por defecto 10%)
    :return: tuple - Monto del descuento calculado y monto final a pagar
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final = monto_total - descuento
    return descuento, monto_final

# Llamada a la función con solo el monto total (usar descuento por defecto del 10%)
monto1 = 200
descuento1, monto_final1 = calcular_descuento(monto1)
print(f"Monto total: ${monto1:.2f}")
print(f"Descuento aplicado (10%): ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}\n")

# Llamada a la función con el monto total y un porcentaje de descuento diferente
monto2 = 500
descuento_personalizado = 15
descuento2, monto_final2 = calcular_descuento(monto2, descuento_personalizado)
print(f"Monto total: ${monto2:.2f}")
print(f"Descuento aplicado ({descuento_personalizado}%): ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")
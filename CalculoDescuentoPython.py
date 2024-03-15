def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100.0)
    monto_final = monto_total - descuento
    return int(descuento), int(monto_final)

# Llamada a la función con el valor predeterminado del descuento
monto_original = 1000
descuento_default, monto_final_default = calcular_descuento(monto_original)
print(f"Monto original: {monto_original} - Descuento por defecto: {descuento_default} - Monto final: {monto_final_default}")

# Llamada a la función con un porcentaje de descuento específico
descuento_especifico, monto_final_especifico = calcular_descuento(monto_original, 15)
print(f"Monto original: {monto_original} - Descuento específico: {descuento_especifico} - Monto final: {monto_final_especifico}")

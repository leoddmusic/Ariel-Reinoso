# Definir una función que tome un valor en grados centígrados y devuelva una tupla con los equivalentes en Fahrenheit y Kelvin
def convertir_temperatura(celsius):
  # Aplicar las fórmulas de conversión
  fahrenheit = celsius * 9/5 + 32
  kelvin = celsius + 273.15
  # Devolver una tupla con los resultados
  return (fahrenheit, kelvin)

# Probar la función
celsius = 20
fahrenheit, kelvin = convertir_temperatura(celsius)
print(f"{celsius}°C son {fahrenheit}°F y {kelvin}K")

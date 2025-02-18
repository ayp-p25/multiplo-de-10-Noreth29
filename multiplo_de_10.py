"""
Múltiplo de 10
"""
# Declaraciones
try:

# Entradas
    numero = int(input("Introduce numero "))

# Proceso
    if numero % 10 == 0:
        print("El número " + str(numero) + " sí es múltiplo de 10")

    else: 
        print("El número " + str(numero) + " no es múltiplo de 10")

except ValueError:
    print("Error. Introduce un valor válido.")
# Salida
#! /usr/bin/python3

# Inicializamos las variables
suma = 0
precio = int(input("Ingrese el precio del primer producto"))

# Cargamos los productos
while precio > 0:
    suma = suma + precio
    precio = int(input("Ingrese el precio del producto, 0 para finalizar: "))

# Mostramos resultados finales
print("El total es: $" , suma)



print("-" * 28)
print("¡¡Identificador de numeros!!")
print("-" * 28)

numero = int(input("Ingrese el numero: "))
resultado = numero % 2

if resultado == 0:
    print(f"El numero {numero} es par.")
    
elif resultado == 1:
    print(f"El numero {numero} es impar.")
    
print("Gracias por usar mi programa")
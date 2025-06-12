numeros = []
pares = []
impares = []
cant = int(input("que cantidad de numeros quieres ingresar: "))

print(f"Ingresa {cant} números:")

for i in range(cant):
    num = int(input(f"Número {i+1}: "))
    numeros.append(num)
    
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
        
    else:
        impares.append(num)

print("Números ingresados:", numeros)
print("Los numeros pares son:", pares)
print("Los numeros impares son:", impares)
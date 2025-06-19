numero = []
alto = []

print("Ingrese los numeros: ")
for i in range(4):
    num = int(input(f"Numero {i + 1}: "))
    numero.append(num)
    
    if num >= 10:
        alto.append(num)
    
mayor = max(numero)
menor = min(numero)

print(f"El numero mas alto de los que entraste es: {mayor}")
print(f"El numero mas bajito de los que entraste es: {menor}")
print(f"Los numeros mas alto que 10 son: {alto}")
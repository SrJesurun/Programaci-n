numeros = []

cant = int(input("ingresa la cantidad de numeros que quieres en la lista: "))
print("Ingresa los números: ")

for i in range(cant):
    num = int(input(f"Número {i + 1}: "))
    numeros.append(num)

mayor = max(numeros)
menor = min(numeros)

print(f"el numero mas alto de los que entraste es: {mayor}")
print(f"el numero mas bajito de los que entraste es: {menor}")
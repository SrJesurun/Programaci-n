caso = int(input("ingrese el numero de caso: "))

if caso == 1:
    num = int(input("ingrese el numero a calcular: "))
    resultado = num / 5
    print(f"el resultado del calculo es: ", resultado)
    
elif caso == 2:
    num = int(input("ingrese el numero a calcular: "))
    expo = int(input("ingrese el exponente: "))
    resultado = num ** expo
    print(f"el resultado del calculo es: ", resultado)
    
elif caso == 3:
    num = int(input("ingrese el numero a calcular: "))
    resultado = num * 6 / 2
    print(f"el ressultado del calculo es: ", resultado)

else:
    print("idiota los casos son del 1 al 3")
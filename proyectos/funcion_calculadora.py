def calculadora ():
    operador = int(input(f"Elige la operacion que quieres hacer: "))
    print("\n")

    if operador == 1:
        num1 = int(input("Ingrese en primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        print("\n")
        Operacion = num1 + num2
        print(f"el resultado de la suma es: ", Operacion)
        
    elif operador == 2:
        num1 = int(input("Ingrese en primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        print("\n")
        Operacion = num1 - num2
        print(f"el resultado de la resta es: ", Operacion)
        
    elif operador == 3:
        num1 = int(input("Ingrese en primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        print("\n")
        Operacion = num1 * num2
        print(f"el resultado de la multiplicacion es: ", Operacion)
            
    elif operador == 4:
        num1 = int(input("Ingrese en primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        print("\n")
        Operacion = num1 / num2
        print(f"el resultado de la division es: ", Operacion)
        
    elif operador == 5:
        num1 = int(input("Ingrese en primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        print("\n")
        Operacion = num1 ** num2
        print(f"el resultado del exponente es: ", Operacion)
        
    elif operador == 6:
        num1 = int(input("Ingrese en primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        print("\n")
        Operacion = num1 // num2
        print(f"el resultado de la division baja es: ", Operacion)
        
    elif operador == 7:
        num1 = int(input("Ingrese en primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        print("\n")
        Operacion = num1 % num2
        print(f"el resultado del modulo es: ", Operacion)
    else:
        print("\n")
print("---------------------------")
print("Bienvenido a mi calculadora")
print("---------------------------\n")
print("1 = Suma")
print("2 = Resta")
print("3 = Multiplicacion")
print("4 = Division")
print("5 = Exponente")
print("6 = Division baja")
print("7 = Porciento")
print("8 = Salir")
print("\n")
operador = int(input(f"Elige la operacion que quieres hacer: "))
print("\n")

while operador >= 1 <= 8:
    if operador == 1:
        num1 = int(input("Ingrese en primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        print("\n")
        Operacion = num1 + num2
        print(f"el resultado de la suma es: ", Operacion)
        operador = int(input(f"\nCual sera tu proxima operacion: "))
        
    elif operador == 2:
        num1 = int(input("Ingrese en primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        print("\n")
        Operacion = num1 - num2
        print(f"el resultado de la resta es: ", Operacion)
        operador = int(input(f"\nCual sera tu proxima operacion: "))
        
    elif operador == 3:
        num1 = int(input("Ingrese en primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        print("\n")
        Operacion = num1 * num2
        print(f"el resultado de la multiplicacion es: ", Operacion)
        operador = int(input(f"\nCual sera tu proxima operacion: "))
            
    elif operador == 4:
        num1 = int(input("Ingrese en primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        print("\n")
        Operacion = num1 / num2
        print(f"el resultado de la division es: ", Operacion)
        operador = int(input(f"\nCual sera tu proxima operacion: "))
        
    elif operador == 5:
        num1 = int(input("Ingrese en primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        print("\n")
        Operacion = num1 ** num2
        print(f"el resultado del exponente es: ", Operacion)
        operador = int(input(f"\nCual sera tu proxima operacion: "))
        
    elif operador == 6:
        num1 = int(input("Ingrese en primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        print("\n")
        Operacion = num1 // num2
        print(f"el resultado de la division baja es: ", Operacion)
        operador = int(input(f"\nCual sera tu proxima operacion: "))
        
    elif operador == 7:
        num1 = int(input("Ingrese en primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        print("\n")
        Operacion = num1 % num2
        print(f"el resultado del modulo es: ", Operacion)
        operador = int(input(f"\nCual sera tu proxima operacion: "))
        
    elif operador == 8:
        print("\nGracias por probar mi calculadora")
        break
        
    else:
        print("\ntu eres tan idiota que no puedes elejir un simple numero de los que estan hay")
        break
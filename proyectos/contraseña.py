contraseña_correcta = "contraseña"
intentos_maximos = 3

for intento in range(intentos_maximos):
    contraseña_ingresada = input("Ingresa la contraseña: ")
    
    if contraseña_ingresada == contraseña_correcta:
        print("¡Contraseña correcta! acceso concedido.")
        break
    
    else:
        intentos_restantes = intentos_maximos - (intento + 1)
        print(f"Contraseña incorrecta. Te quedan {intentos_restantes} intentos.")
        
else:
    print("Has excedido el numero maximo de intetos. Acceso denegado.")
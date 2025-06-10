nombre = input("Ingresa el nombre del empleado: ")
clave = int(input(f"Ingrese la clave de departamento del empleado: "))
antiguedad = int(input(f"Ingrese el tiempo del empleado en la empreza: "))

while clave == 1:
    if antiguedad == 1:
        print(f"El empleado", nombre, "tiene 6 dias de vacaciones aprobados")
        nombre = input("Ingresa el nombre del siguente empleado: ")
        clave = int(input(f"Ingrese la clave de departamento del empleado: "))
        antiguedad = int(input(f"Ingrese el tiempo del empleado en la empreza: "))
        
    elif antiguedad >=2 <=6:
        print(f"El empleado", nombre, "tiene 14 dias de vacaciones aprobados")
        nombre = input("Ingresa el nombre del siguente empleado: ")
        clave = int(input(f"Ingrese la clave de departamento del empleado: "))
        antiguedad = int(input(f"Ingrese el tiempo del empleado en la empreza: "))
        
    elif antiguedad >= 7:
        print(f"El empleado", nombre, "tiene 20 dias de vacaciones aprobados")
        nombre = input("Ingresa el nombre del siguente empleado: ")
        clave = int(input(f"Ingrese la clave de departamento del empleado: "))
        antiguedad = int(input(f"Ingrese el tiempo del empleado en la empreza: "))
        
if clave == 2:
    if antiguedad == 1:
        print(f"El empleado", nombre, "tiene 7 dias de vacaciones aprobados")
        nombre = input("Ingresa el nombre del siguente empleado: ")
        clave = int(input(f"Ingrese la clave de departamento del empleado: "))
        antiguedad = int(input(f"Ingrese el tiempo del empleado en la empreza: "))
        
    elif antiguedad >=2 <=6:
        print(f"El empleado", nombre, "tiene 15 dias de vacaciones aprobados")
        nombre = input("Ingresa el nombre del siguente empleado: ")
        clave = int(input(f"Ingrese la clave de departamento del empleado: "))
        antiguedad = int(input(f"Ingrese el tiempo del empleado en la empreza: "))
        
    elif antiguedad >= 7:
        print(f"El empleado", nombre, "tiene 22 dias de vacaciones aprobados")
        nombre = input("Ingresa el nombre del siguente empleado: ")
        clave = int(input(f"Ingrese la clave de departamento del empleado: "))
        antiguedad = int(input(f"Ingrese el tiempo del empleado en la empreza: "))
        
elif clave == 3:
    if antiguedad == 1:
        print(f"El empleado", nombre, "tiene 10 dias de vacaciones aprobados")
        nombre = input("Ingresa el nombre del siguente empleado: ")
        clave = int(input(f"Ingrese la clave de departamento del empleado: "))
        antiguedad = int(input(f"Ingrese el tiempo del empleado en la empreza: "))
        
    elif antiguedad >=2 <=6:
        print(f"El empleado", nombre, "tiene 20 dias de vacaciones aprobados")
        nombre = input("Ingresa el nombre del siguente empleado: ")
        clave = int(input(f"Ingrese la clave de departamento del empleado: "))
        antiguedad = int(input(f"Ingrese el tiempo del empleado en la empreza: "))
        
    elif antiguedad >= 7:
        print(f"El empleado", nombre, "tiene 30 dias de vacaciones aprobados")
        nombre = input("Ingresa el nombre del siguente empleado: ")
        clave = int(input(f"Ingrese la clave de departamento del empleado: "))
        antiguedad = int(input(f"Ingrese el tiempo del empleado en la empreza: "))
else:
    print("Clave de departamento incorreta")
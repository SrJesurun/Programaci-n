from datetime import datetime
actual = datetime.now().year

año = int(input("ingresa el año en que naciste: "))

edad = actual - año
if edad >= 18:
    print(f"Tu edad es: {edad}, eres mayor de edad.")
else:
    print(f"Tu edad es: {edad}, eres menor de edad.")
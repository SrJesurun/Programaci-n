#creando funcion que suma numeros
def sumar_dos():
    #iniciando un bucle
    while True:
        #pidiendo numeros
        a = input("numero 1: ")
        b = input("numero 2: ")
        #intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
        #si lanzo una excepcion, pedirle que reingrese los datos
        except ValueError as e:
            print("te pedi un numero animal")
            print(f"ERROR: {e}")
        #si todo salio bien terminamos el bucle
        else:
            break
        finally:
            print("Manejo de excepciones finalizado")
    #mostrando el resultado
    return resultado

print(sumar_dos())
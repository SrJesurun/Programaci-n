#creando una funcion simple
def saludo():
    print("Hola mario, bro ¿como estas?")
    
#ejecutando la funcion simple
saludo()

#crear una funcion que tenga parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "Reina"
    elif (sexo == "hombre"):
        adjetivo = "Rey"
    else:
        adjetivo = "Cariño"
    print(f"hola {nombre}, {adjetivo} ¿como estas?")

saludar("camila","mujer")
saludar("mario","hombre")
saludar("fran","no binario")

#creando una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdfghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

#desenpaquetando la funcion
passward,primer_numero = crear_contraseña_random(5)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu nueva contraseña es: {passward}")
print(f"El numero utilizado para crearla fue: {primer_numero}")
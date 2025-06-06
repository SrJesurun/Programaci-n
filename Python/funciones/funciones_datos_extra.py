#creando una funcion de 3 parametros
def frase1(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, eres un {adjetivo}"

#utilizando keyword arguments
frase_resultado = frase1(adjetivo = "crack",nombre = "mario",apellido = "jesurun")

#creando la misma funcion con un parametro opcional y un valor por defecto
def frase2(nombre,apellido,adjetivo = "tonto"):
    return f"Hola {nombre} {apellido}, eres un {adjetivo}"

frase_resultante = frase2("mario","jesurun","inteligente")
print(frase_resultante)
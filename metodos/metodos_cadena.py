cadena1 = "Hola soy mario"
cadena2 = "Bienvenido maquina"

#convierte a mayusculas
resultado1 = cadena1.upper()

#convierte a minusculas
resultado2 = cadena1.lower()

#primera letra mayuscula
resultado3 = cadena1.capitalize()

#busca cadena dentro de cadenas, si no hay coinsidencias devuelve -1
resultado4 = cadena1.find("Hola")

#busca cadena dentro de cadenas, si no hay cainsidencias lanza una excepcion
resultado5 = cadena1.index("m")

#si es numerio devuelve True, si no False
resultado6 = cadena1.isnumeric()

#si es alfanumerio devuelve True, si no False
resultado7 = cadena1.isalpha()

#cuenta coincidencias de una cadena, devuelve las veces que coincida
resultado8 = cadena1.count("a")

#cuanta cuantos caracteres tiene una cadena
resultado9 = len(cadena1)

#verifica si una cadena enpiesa con la cadena dada
resultado10 = cadena1.startswith("H")

#verifica si una cadena termina con la cadena dada
resultado11 = cadena1.endswith("o")

#remplaza un pedazo de la cadena dada por otra
resultado12 = cadena1.replace("H", "h")

#separar cadena por cadena dada
resultado13 = cadena1.split(",")

print(resultado1)
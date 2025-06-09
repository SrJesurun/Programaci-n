import re

texto = """Hola maestro, esta es la cadena 1, como estas mi capitan
Esta es la linea 2 de texto
y Esta es la final (linea 3) definitiva mi capitan"""

#haciendo una busqueda simple
resultado = re.findall("Esta",texto)

#\d = busca digitos numericos del 0 - 9
resultado = re.findall(r"\d",texto)

#\D = busca todo menos digitos numericos del 0 - 9
resultado = re.findall(r"\D",texto)

#\w = busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\w",texto)

#\W = busca todo menos caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\W",texto)

#\s = busca espacios en blanco - espacios, tabs, saltos de linea
resultado = re.findall(r"\s",texto)

#\S = busca todo menos espacios en blanco - espacios, tabs, saltos de linea
resultado = re.findall(r"\S",texto)

#. - busca todo menos saltos en linea
resultado = re.findall(r".",texto)

#\n - busca saltos en linea
resultado = re.findall(r"\n",texto)

#\ - cancelar caracteres especiales, cancelando la funciom del punto y buscando puntos
resultado = re.findall(r"\.",texto)

#armando uns cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(f"\d\.\s", texto)

#^ - busca el comienzo de una linea
#flags=re.M activa la multilinea
resultado = re.findall(f"^",texto,flags=re.M)

#$ - busca el final de una linea
resultado = re.findall(f"$",texto,flags=re.M)

#{n} - busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r"\d{3}",texto)

#{n,m} - al menos n, como maximo m
resultado = re.findall(r"\d{1,4}",texto)

# | - busca una cosa o la otra
resultado = re.findall(r"\d{1,4}|Hola",texto)

print(resultado)
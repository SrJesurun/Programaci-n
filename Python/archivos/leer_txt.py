#usando open para abrie un archivo
archivo_sin_leer = open("archivos\\texto_de_mario.txt")

#leer archivo completo
archivo = archivo_sin_leer.read()

#leer linea por linea
lineas = archivo_sin_leer.readlines()

#leer una sola linea
linea = archivo_sin_leer.readline()

#cerrar el archivo
archivo.close()

print(archivo)
#abriendo el archivo con whit open
with open("archivos\\texto_de_mario.txt") as archivo:
    
    #leemos el archivo
    print(archivo.read())
    
    #mostramos el archivo
    print(archivo)
    
#no es necesario cerrarlo al usar whith open
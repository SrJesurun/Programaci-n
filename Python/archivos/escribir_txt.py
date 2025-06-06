with open("archivo\\texto_de_mario.txt","w") as archivo:
    
    #sobreescribiendo el archivo
    archivo.write("no mames lo borre todo")
    
    #agregando lineas con writelines
    archivo.writelines("hola mario como estas\n","qlok")
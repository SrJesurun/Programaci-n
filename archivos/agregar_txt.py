with open("archivos\\texto_de_mario.txt","a") as archivo:
    
    #usando un bucle para agregar varias lineas
    archivo.write("\n")
    for i in range(5):
        
        #agregando lineas
        archivo.write(f"linea {i+1} agregada\n")
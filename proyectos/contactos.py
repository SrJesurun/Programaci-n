def contactos(cantidad_de_contactos):
    contactos = []
    cant = int(input("ingrese la cantidad de contactos a guardar"))
    
    with open("proyectos\\contactos.txt","a") as cont:
        cont.write("\n")
        for i in range(cantidad_de_contactos):
            nombre = input("ingrese el nombre del contacto")
            numero = input("ingrese el numero del contacto")
            contacto = (nombre,numero)
            
            contactos.append(contacto)
        
    contactos = cantidad_de_contactos(cant)
    
    cont.write(f"[{nombre},{numero}\n]")
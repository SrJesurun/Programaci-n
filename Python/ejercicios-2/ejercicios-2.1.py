#falto el prfesor y los chicos van a armar la clase

#funcion para obtener al asistente y al profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando la lista con los compañeros
    compañeros = []
    
    #ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero")
        edad = int(input("ingrese la edad del compañero"))
        compañero = (nombre,edad)
        
        #agregando la informacion a la lista
        compañeros.append(compañero)
        
    #ordenandolos de menor a mayor segun su edad
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir al asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor

#desenpaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

#mostrando el resultado
print(f"El profesor es: {profesor} y su asistente es: {asistente}")
#creando diccionario con dict()
diccionario = dict(nombre="mario",apellido="jesurun")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["mario","qlok" ]):"jajaja"}

#creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fronkeys(["nombre","apellido"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"no se")

print(diccionario)
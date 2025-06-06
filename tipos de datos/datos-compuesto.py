#creando una lista (se pueden modificar)
lista = ["mario jesurun", "overgame", True, 1.85]

#creando una lista (no pueden modificar)
tupla = ("mario jesurun", "overgame", True, 1.85)

#esto es valido
lista[3] = "maquinola"

#esto no
#tupla[3] = "maquinola"

print(lista[3])

#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)
conjunto = {"mario jesurun", "overgame", True, 1.85}

#print(conjunto[3]) - no puede acceder al elemento

#creando un diccionario (dict)
diccionario = {
    "nombre" : "mario jesurun",
    "canal" : "overgame",
    "esta_emocionado" : True,
    "altura" : 1.85,
    "dato_duplicado" : "overgame"
}

print(diccionario["altura"])

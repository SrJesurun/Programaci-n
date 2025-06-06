
#Creando una lista con list()
lista = list(["hola","mario",34,56,23,True])

#devuelve la cantidad de elementos de la lista
resultado1 = len(lista)

#agregando un elemento a la lista
lista.append("jajaja")

#agregando un elemento a la lista en un indicec especifico
lista.insert(2,"qlok")

#agregando varios elementos a la lista
lista.extend([False,2030])

#eliminando un elemento de la lista por su indice
lista.pop(0)

#removiendo un elemento de la lista por su valor
lista.remove("qlok")

#elimina todos los elementos de la lista
lista.clear()

#ordena toda la lista pero no str (reverse=True lo pone en reversa)
lista.sort()

#invierte los elementos de la lista
lista.reverse()

print(resultado1)
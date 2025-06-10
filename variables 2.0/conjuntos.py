#creando un conjunto con set()
conjunto = set(["mario 1"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["mario 1", "mario 2"])
conjunto2 = {conjunto1, "mario 3"}
print(conjunto2)

#teroria de conjunto
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto > conjunto1

#verificando si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)
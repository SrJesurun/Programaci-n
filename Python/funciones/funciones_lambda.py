numeros = [1,2,3,4,5,6,7,8,9]

#creando funcion lambda para multiplicar por dos
multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(5))

#creando funcion comun que diga si es par o no
def es_par(num):
    if (num%"==0"):
        return True

#usando filter con una funcion comun
numeros_pares1 = filter(es_par,numeros)
print(list(numeros_pares1))

#creando lo mismo que antes pero con lambda
numeros_pares2 = filter(lambda numero:numero%2 == 0,numeros)
print(list(numeros_pares2))
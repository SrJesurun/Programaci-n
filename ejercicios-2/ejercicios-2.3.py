#creando una funcion que muestre la serie fibonaacci entre 0 y  el numero dado

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = []
    for i in range(num):
        if a+b > num: return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a,b = b,a+b

resultado = fibonacci(144)
print(resultado)
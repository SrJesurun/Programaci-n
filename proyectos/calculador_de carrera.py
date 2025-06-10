cib = 114 * 520
siv = 105 * 520
tel = 105 * 520
ia = 105 * 520
ifo = 116 * 520
er = 129 * 520
rdi = 141 * 520
meca = 181 * 520
ma = 163 * 520
mddm = 154 * 520
di = 162 * 520
mul = 151 * 520
son = 146 * 520
ddf = 150 * 520
aycdd = 105 * 520
si = 122 * 520
ingles = 16000
reinscripsion = 6640
unico = 5800
menu = """1 - Tecnologo en Ciberseguridad
2 - Simulaciones Interativas y Videojuegos
3 - Telecomunicaciones
4 - Inteligencia Artificial
5 - Informatica forence
6 - Energia renovables
7 - Redes de Informacion
8 - Mecatronica
9 - Manufactura Automatizada
10 - Manufactura de Dispositivo Medico
11 - Diseño Industrial
12 - Multimedia
13 - Sonido
14 - Desarrollo de Software
15 - Analitica y Ciencias de Datos
16 - Seguridad Informatica
17 - Salir
"""
pagos = """Pago unico = 5800
Pago de Creditos = 520
Pago de Reinscripsion = 6640
Pago de Ingles = 4000
"""

print("-----------------------------------------------")
print("Bienvenidos a el calculador de carrera del itla")
print("-----------------------------------------------")
print("\n", menu)
carrera = int(input("Ingrese la carrera a calcular: "))
print(pagos, "\n")
while carrera >= 1 <= 17:
    if carrera == 1:
        rei = reinscripsion * 6
        total = ingles + rei + unico + cib
        print("La carrera que elegiste es: Ciberseguridad")
        print(f"El precio total de los creditos es de: ", cib)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))
        
    elif carrera == 2:
        rei = reinscripsion * 7
        total = ingles + rei + unico + siv
        print("La carrera que elegiste es: Simulaciones Interativas y Videojuegos")
        print(f"El precio total de los creditos es de: ", siv)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))
        
    elif carrera == 3:
        rei = reinscripsion * 7
        total = ingles + rei + unico + tel
        print("La carrera que elegiste es: Telecomunicaciones")
        print(f"El precio total de los creditos es de: ", tel)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))
        
    elif carrera == 4:
        rei = reinscripsion * 7
        total = ingles + rei + unico + ia
        print("La carrera que elegiste es: Inteligencia Artelificial")
        print(f"El precio total de los creditos es de: ", ia)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))
        
    elif carrera == 5:
        rei = reinscripsion * 7
        total = ingles + rei + unico + ifo
        print("La carrera que elegiste es: Informatica Forence")
        print(f"El precio total de los creditos es de: ", ifo)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))
        
    elif carrera == 6:
        rei = reinscripsion * 7
        total = ingles + rei + unico + er
        print("La carrera que elegiste es: Energias Renovable")
        print(f"El precio total de los creditos es de: ", er)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))

    elif carrera == 7:
        rei = reinscripsion * 7
        total = ingles + rei + unico + rdi
        print("La carrera que elegiste es: Redes de Informacion")
        print(f"El precio total de los creditos es de: ", rdi)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))

    elif carrera == 8:
        rei = reinscripsion * 7
        total = ingles + rei + unico + meca
        print("La carrera que elegiste es: Mecatronica")
        print(f"El precio total de los creditos es de: ", meca)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))

    elif carrera == 9:
        rei = reinscripsion * 7
        total = ingles + rei + unico + ma
        print("La carrera que elegiste es: Manufactura Automatizada")
        print(f"El precio total de los creditos es de: ", ma)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))

    elif carrera == 10:
        rei = reinscripsion * 7
        total = ingles + rei + unico + mddm
        print("La carrera que elegiste es: Manufactura de Dispositivos Medicos")
        print(f"El precio total de los creditos es de: ", mddm)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))

    elif carrera == 11:
        rei = reinscripsion * 7
        total = ingles + rei + unico + di
        print("La carrera que elegiste es: Diseño Industrial")
        print(f"El precio total de los creditos es de: ", di)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))

    elif carrera == 12:
        rei = reinscripsion * 7
        total = ingles + rei + unico + mul
        print("La carrera que elegiste es: Multimedia")
        print(f"El precio total de los creditos es de: ", mul)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))

    elif carrera == 13:
        rei = reinscripsion * 7
        total = ingles + rei + unico + son
        print("La carrera que elegiste es: Sonido")
        print(f"El precio total de los creditos es de: ", son)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))

    elif carrera == 14:
        rei = reinscripsion * 7
        total = ingles + rei + unico + ddf
        print("La carrera que elegiste es: Desarrollo de Sofware")
        print(f"El precio total de los creditos es de: ", ddf)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))

    elif carrera == 15:
        rei = reinscripsion * 7
        total = ingles + rei + unico + aycdd
        print("La carrera que elegiste es Analitica y Ciencias de Datos")
        print(f"El precio total de los creditos es de: ", aycdd)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))

    elif carrera == 16:
        rei = reinscripsion * 7
        total = ingles + rei + unico + si
        print("La carrera que elegiste es: Seguridad Informatica")
        print(f"El precio total de los creditos es de: ", si)
        print(f"El precio total por reinscripsion es de: ", rei)
        print(f"El precio total por el ingles es de: ", ingles)
        print(f"El precio total de pagos unicos es de: ", unico)
        print(f"El total a pagar por la carrera es de: ", total)
        print("\n", menu)
        carrera = int(input("ingrese la proxima carrera a calcular: "))

    elif carrera == 17:
        print("Gracias por probar mi calculador de carrera")
        break
    else:
        print("tu eres tan idiota que no puedes elejir un simple numero de los que estan hay")
        break
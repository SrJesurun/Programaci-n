#si el modulo estuviera dentro de una carpeta en la misma ruta
import funciones_buenas.saludar as m_saludar

print(m_saludar.saludar.saludo("mario"))

import sys

sys.path.append("c:\\Users\\mpick\\Desktop\\python\\funciones_buenas")

import saludar as hey
print(hey.saludar("mario"))
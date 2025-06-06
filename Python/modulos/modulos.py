#importando un modulo y asignandole el nombre "m_saludo"
import modulo_saludo as m_saludo

#desde el modulo, importamos dos funciones
from modulo_saludo import saludo,saludo_raro

#creamos las variables con los saludos
saludo = saludo("Mario")
saludo_raro = saludo_raro("Papa")

#mostramos los resultados
print(saludo)
print(saludo_raro)

#para ver las propiedades y metodos de el namespace
print(dir(m_saludo))

#accedemos al nombre de este modulo
print(__name__)

#accedemos al nombre del modulo llamado
print(m_saludo.__name__)
#esto esta funcionando hay que darmela coño soy el mejor casi casi programador mmg
print("qlok")

#promedio de duraciones
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#durcion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencia de duracion
respuesta1 = 100 - dalto_curso / otros_cursos_min * 100
respuesta2 = 100 - dalto_curso *1000 // otros_cursos_max / 10
respuesta3 = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando el porcentaje de tienpo vacio removido
respuesta4 = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
respuesta5 = 100 - dalto_curso * 1000 // crudo_dalto / 10

#mostrando las diferencias de datos (ejercicio A)
print(f"El curso de dalto dura un {respuesta1}% menos que el mas rapido")
print(f"El curso de dalto dura un {respuesta2}% menos que el mas lento")
print(f"El curso de dalto dura un {respuesta3}% menos que el promedio")
print("-------------------------")

#mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print(f"un curso promedio elimina un {respuesta4}% de tiempo vacio")
print(f"este curso elimino un {respuesta5}% de tiempo vacio")
print("-------------------------")

#mostrando diferencia si los cursos duraran 10 horas
print(f"ver 10 horas de este curso equivale a ver {otros_cursos_promedio *100 // dalto_curso / 10} horas de otros cursos")
print(f"ver 10 horas de otro curso equivale a ver {dalto_curso *100 // otros_cursos_promedio / 10} horas del curso de dalto")
print("-------------------------")
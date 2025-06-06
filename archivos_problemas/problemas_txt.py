#3 listas, una con nombres otra con apellidos y otra con edades
nombres = ["mario","jorbi","tatiana","daris","yaine"]
apellidos = ["jesurun","montero","asencio","jesurun","coplin"]
edades = [21,21,17,14,7]

#registrar esta informacion en un TXT de forma optima
with open("archivos_problemas\\nombres_apellidos_y_edades.txt","w") as arch:
    arch.writelines("los datos son: \n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\nEdad: {e}\n-------------\n")for n,a,e in zip(nombres,apellidos,edades)]
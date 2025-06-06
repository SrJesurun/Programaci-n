#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas\\datos.csv")

#convirtiendo a string los datos de una columna
df["edad"] = df["edad"].astype(str)

#mostrando el tipo de dato del primer elemento de la edad
print(type(df["edad"][0]))

#remplazando los datos "mario" por "maestro"
df["apellido"].replace("jesurun","maestro",inplace=True)

#borrando filas con datos faltantes
df = df.dropna()

#borrando filas repetidas
df = df.drop_duplicates()

#creando un csv con el dataframe resultante (limpio)
df.to_csv("archivos_problemas\\datos_limpio.csv")

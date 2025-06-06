import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\mario_ingresos.csv")

#ordenandolo segun la cantidad de ingresos
df_orden_descendente = df.sort_values("ingresos",ascending=False)

#creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df_orden_descendente)

#obteniendo el total de ingresos
total_ingresos = df["ingresos"].sum()

#mostrando el total
print(f"El total de ingresos es de: ${total_ingresos} usd")

#mostrando el grafico
plt.show()
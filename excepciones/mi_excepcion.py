#creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"impresionante, cometiste el siguiente error: {err}")

#lanzando mi propia excepcion
raise MiExcepcion("idiota")

#manejandola
try:
    raise MiExcepcion("idiota")
except:
    print("Como vas a cometer ese error? maldito ñame🤣")
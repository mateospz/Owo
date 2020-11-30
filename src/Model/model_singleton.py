# Implementacion Básica de patrón singleton en Python

# Definimos el decorador al que llamamos singleton y lo hacemos privado pasando como parámetro la clase
# que se quiere instanciar
def singleton(cls):
    # Definimos el diccionario instancias
    instances = dict()

    # Creamos el método "envoltorio" y le pasamos como parámetro argumento y diccionarios
    def wrap(*args, **kwargs):

        # Preguntamos si la clase que pasamos como parámetro no esta dentro del diccionario
        if cls not in instances:

            # Si efectivamente no está se añade
            instances[cls] = cls(*args, **kwargs)

            # En caso que no lo este
        else:

            # En caso de que exista se continua con la ejecución
            pass

        # Devolvemos el diccionario
        return instances[cls]

    # Se devuelve la llamada del método
    return wrap

# Implementacion Básica de patrón singleton en Python

# Definimos el decorador al que llamomos singleton y lo hacemos privado pasando como parametro la clase
# que se quiere instanciar
def singleton(cls):
    # Definimos el diccionario instacias
    instances = dict()

    # Creamos el metodo "envoltorio" y le pasamos como parametro argumento y diccionarios
    def wrap(*args, **kwargs):

        # Preguntamos si la clase que pasamos como parametro no esta dentro del diccionario
        if cls not in instances:

            # Si efectivamente no está se añade
            instances[cls] = cls(*args, **kwargs)

            # En caso que no lo este
        else:

            # En caso de que exista se continua con la ejecucíon
            pass

        # Devolvemos el diccionario
        return instances[cls]

    # Se devuelve la llamada del metodo
    return wrap

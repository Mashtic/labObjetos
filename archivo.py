# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 19/10/2022 08:31 pm
# Última modificación: 20/10/2022 11:20 am
# Versión: 3.10.8

# Importar librerías
import pickle # Para poder usar archivos

# Funciones archivos
'----------------- Función Leer archivo  -----------------'

def leerArchivo(nomArchLeer):
    """
    Funcionalidad: lee los datos del archivo y los retorna como
                   lista
    Entradas: nomArchLeer (str): nombre que se le da al archivo
    Salidas: listaDatos (list): datos del archivo como lista
    """
    listaDatos = [] # Inicializa lista
    try:
        file = open(nomArchLeer, "rb") # Abre el archivo para leer
        listaDatos = pickle.load(file) # Carga los datos en la lista
        file.close() # Lo cierra
    except:
        print("El archivo " + nomArchLeer + " no existe o se encuentra vacío.") # Avisa al usuario
    return listaDatos

'--------------- Fin función Leer archivo  ---------------'


'------------ Función Actualizar datos del archivo  ------------'

def actualizarArchivo(nomArchAct, datosAct):
    """
    Funcionalidad: sobreescribe los datos del archivo actualizándolo
    Entradas: nomArchAct (str): nombre del archivo a actualizar
    Salidas: N/A
    """
    try:
        file = open(nomArchAct, "wb")
        pickle.dump(datosAct, file) # Sobreescribe los archivos con el parámetro
                                    # datosAct
        file.close()
    except:
        print("Error al actualizar el archivo " + nomArchAct) # En caso de problemas
    return ""

'---------- Fin función Actualizar datos del archivo  ----------'
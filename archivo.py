# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 12/10/2022 06:57 am
# Última modificación: 12/10/2022 07:26 am
# Versión: 3.10.7

# Importar librerías
import pickle # Para poder usar archivos

# Funciones archivos
'----------------- Función Leer archivo  -----------------'

def leerArchivo(nomArchLeer):
    """
    Funcionalidad: lee los datos del archivo y los retorna como
                   diccionario
    Entradas: nomArchLeer (str): nombre que se le da al archivo
    Salidas: diccDatos (dict): datos del archivo como dict
    """
    listaDatos = [] # Inicializa diccionario
    try:
        file = open(nomArchLeer, "rb") # Abre el archivo para leer
        listaDatos = pickle.load(file) # Carga los datos en el diccionario
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

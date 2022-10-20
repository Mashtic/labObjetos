###########################################################
#Elaborado por: XXX
#Fecha de Realización: XX/XX/XXXX XX:XX
#Ultima actualización: XX/XX/XXXX XX:XX
###########################################################

#Librerías
from names import *
import random
from laboratorioObjetos import *
from archivo import *

#Definición de variables globales
listaCategorias=[]
listaCategorias=[["ar", "lo", "co", "in"], ["ab", "me", "pr", "ac"], ["lo", "de", "ej", "co"], ["vi", "av", "em", "an"]]
#Funciones

def insertarMiembro(cant):
    global listaCategorias
    num=0
    listaMiembros=[]
    for i in range (cant):
        miembro=Compa()
        miembro.asignarNombre(get_first_name(), get_last_name(), get_last_name())
        miembro.asignarCedula(random.randint(100000000,999999999))
        num=random.randint(1,4)
        miembro.asignarCategoria(num, listaCategorias[num-1])
        miembro.asignarEstado(bool(random.getrandbits(1)))
        listaMiembros.append(miembro)
    actualizarArchivo("Miembros", listaMiembros)
    return "Los miembros han sido creados exitosamente."

def insertarMiembroAux(cant):
    try:
        cant=int(cant)
        if cant<=0:
            return "Debe digitar una cantidad de meimbros mayor que 0"
        else:
            return insertarMiembro(cant)
    except:
        return "Debe digitar un número entero"

def insertarMiembroES():
    cant=input("Digite la cantidad de personas que van a conformar el grupo de trabajo: ")
    return print(insertarMiembroAux(cant))

insertarMiembroES()
    


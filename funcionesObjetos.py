# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 19/10/2022 08:31 pm
# Última modificación: 20/10/2022 6:00 pm
# Versión: 3.10.8

# Librerías utilizadas
from names import *
import random
import re
from laboratorioObjetosv2 import *
from archivo import *

# Definición de variables globales

listaPersIniciales = [] # Se inicializan
listaPersCompleto = []
listaPersIniciales = [["ar", "lo", "co", "in"], ["ab", "me", "pr", "ac"], ["lg", "de", "ej", "co"], ["vi", "av", "em", "an"]]
listaPersCompleto = [["arquitecto", "lógico", "comandante", "innovador"], ["abogado", "mediador", "protagonista", "activista"], 
["logista", "defensor", "ejecutivo", "cónsul"], ["viruoso", "aventurero", "emprendedor", "animador"]] # Para poder ser usada
                                                                                                      # en varias funciones


# Funciones auxiliares

def confirmar():
    """
    Funcionalidad: Función que se encarga, de confirmar 
                   si el usuario quiere hacer un proceso
    Entradas: resp (str)
    Salidas: True/False (bool)
    """
    resp = input("\n¿Está usted seguro de continuar con el proceso?\n1. Sí\n2. No\nSeleccione una opción: ")
    if resp == "1":
        return True
    elif resp == "2":
        return False
    else:
        print("Ingrese una opción válida.")
    return confirmar()

def esNombre(pNombre):
    """
    Funcionalidad: comprueba que sea un nombre, y si
                   lo es, retorna True
    Entradas: pNombre (str)
    Salidas: True/False (bool)
    """
    if re.match(r"^([A-ZÁÉÍÓÚ][a-záéíóú]+\s?){3}$", pNombre) == None:
        return False
    return True

def validarNombre():
    """
    Funcionalidad: comprueba que sea un nombre, solamente letras
                   con mayúscula y minúscula
    Entradas: nombre (str)
    Salidas: nombre.split(" ") (list)
    """
    while True:
        nombre = input("\nEscriba el nombre y dos apellidos: ")
        if esNombre(nombre):
            break
        print("Ingrese una mayúscula seguido de letras minúsculas," + 
        "\nluego deje un espacio por cada nombre/apellido.")
    return nombre.split(" ")

def esCedula(pCedula):
    """
    Funcionalidad: comprueba que cumpla con el formato de cédula
                   de Costa Rica, si lo cumple, retorna True
    Entradas: pCedula (str)
    Salidas: True/False (bool)
    """
    if re.match("^[1-9][0-9]{8}$", pCedula) == None:
        return False
    return True

def validarCedula():
    """
    Funcionalidad: comprueba que cumpla con el formato de cédula
                   de Costa Rica, lo retorna hasta que ocurra
    Entradas: cedula (str)
    Salidas: cedula (int)
    """
    while True:
        cedula = input("\nIngrese la cédula del miembro: ")
        if esCedula(cedula):
            return int(cedula)
        print("Ingrese una cédula válida (9 dígitos, el primero diferente de 0).")
    return

def encontrarMiembro(listaMiembros, pCedula):
    """
    Funcionalidad: comprueba que el miembro con pCedula exista en la lista de miembros,
                   en caso que sí, retorna True
    Entradas: listaMiembros (list)
              pCedula (int)
    Salidas: True/False (bool)
    """
    for miembro in listaMiembros:
        if pCedula == miembro.obtenerCedula():
            return True
    return False

def estadoMiembro(pEstado):
    """
    Funcionalidad: cambia el valor que representa pEstado (bool) a
                   texto como Activo o Inactivo (str)
    Entradas: pEstado (bool)
    Salidas: texto indicando estado (str)
    """
    if pEstado == True:
        return "Activo/a"
    return "Inactivo/a"
    
def categoriaMiembro(pCateg):
    """
    Funcionalidad: cambia el valor que representa pCateg (int) a
                   texto como su categoría correspondiente (str)
    Entradas: pCateg (int)
    Salidas: texto indicando categoría (str)
    """
    if pCateg == 1:
        return "analista"
    elif pCateg == 2:
        return "diplomático"
    elif pCateg == 3:
        return "centinela"
    else:
        return "explorador"

def persMiembro(pPersonalidad):
    """
    Funcionalidad: de acuerdo a la categoría como iniciales, lo devuelve como palabra 
    Entradas: pPersonalidad (str)
    Salidas: texto indicando personalidad de categoria (str)
    """
    global listaPersIniciales, listaPersCompleto
    for posicion, listaPersInicial in enumerate(listaPersIniciales): # Da el int por posición y evalúa la lista
        if pPersonalidad in listaPersInicial: # Si se encuentra en esa lista
            return listaPersCompleto[posicion][listaPersInicial.index(pPersonalidad)] # Busca en la lista con las palabras
                                                                                      # de personalida y la devuelve de
                                                                                      # acuerdo a la misma posición
# Funciones principales
'------------------ Insertar miembro --------------------'

def insertarMiembro(cant):
    """
    Funcionalidad: crea el archivo con la cantidad de miembros indicada
    Entradas: cant (int)
    Salidas: listaMiembros (list)
    """
    global listaPersIniciales
    num = 0
    listaMiembros = []
    for numMiembro in range(cant):
        miembro = Miembro()
        miembro.asignarNombre(get_first_name(), get_last_name(), get_last_name())
        miembro.asignarCedula(random.randint(100000000,999999999))
        num=random.randint(1,4)
        miembro.asignarCategoria(num, listaPersIniciales[num-1][random.randint(0,3)])
        miembro.asignarEstado(bool(random.getrandbits(1)))
        listaMiembros.append(miembro)
    actualizarArchivo("Miembros", listaMiembros)
    print("\nLos miembros han sido creados exitosamente.")
    return listaMiembros

'------------------ 1. Modificar miembro --------------------'

def modificarMiembro(listaMiembros, pCedula):
    """
    Funcionalidad: modifica el nombre de un miembro según su cédula
    Entradas: listaMiembros (list)
              pCedula (int)
              nombreCompleto (list)
    Salidas: listaMiembros (list)
    """
    for miembro in listaMiembros:
        if pCedula == miembro.obtenerCedula():
            nombreCompleto = validarNombre()
            if confirmar() == False: # Si no se confirma, no se realiza
                return print("\nNo se realizó ninguna modificación.")
            miembro.asignarNombre(nombreCompleto[0], nombreCompleto[1], nombreCompleto[2]) # Lo modifica
            print("\nEl nombre de cédula " + str(pCedula) + " ha sido modificado.")
            return listaMiembros

'------------------ 2. Eliminar miembro --------------------'

# Funciones
def eliminarMiembro(listamiembros, cedula):
    """
    Funcionalidad: Elimina un miembro de la reunión
    Entradas: listamiembros (list), cedula (str)
    Salidas: un string confirmando si se ejecutó o no la función
    """
    conf=False
    for miembro in listamiembros:
        cedulamiembro=miembro.obtenerCedula()
        if cedulamiembro==cedula:
            estado=miembro.obtenerEstado()
            if estado==True:
                conf=confirmar()
                if conf==True:
                    miembro.asignarEstado(False)
                    return "La persona ha sido eliminada."
                else:
                    return "No se eliminó a la persona."
            else:
                return "No es posible eliminarla, pues ya estaba eliminada."
    return "El número de cédula no se encuentra registrado."

'------------------ 3. Reporte completo --------------------'

def reporteMiembro(miembro):
    """
    Funcionalidad: imprime los datos de un miembro
    Entradas: miembro (Miembro)
    Salidas: salida con todos los datos del miembro (str)
    """
    nombre, cedula, categoria, estado = miembro.obtenerInfo()
    return (f'''
    Nombre: {nombre[0]} {nombre[1]} {nombre[2]}.
    Cédula: {cedula}.
    Categoría: {categoriaMiembro(categoria[0])}, {persMiembro(categoria[1])}.
    Estado: {estadoMiembro(estado)}.
    ''')

def reporteCompleto(listaMiembros):
    """
    Funcionalidad: imprime los datos de todos los miembros de la planilla
    Entradas: listaMiembros (list)
    Salidas: salida con todos los datos de los miembros (str)
    """
    print("\nLa cantidad de miembros es de " + str(len(listaMiembros)) + ":\n")
    for indice, miembro in enumerate(listaMiembros):
        print("Miembro " + str(indice+1) + reporteMiembro(miembro))
    return "\nReporte finalizado."

'------------------ 4. Reporte categorías --------------------'

# Funciones

def reporteCategoria(listamiembros, categoria):
    """
    Funcionalidad: imprime los datos de un miembro de una categoría específica
    Entradas: listamiembros (list), categoria (int)
    Salidas: salida con todos los datos del miembro (str)
    """
    for miembro in listamiembros:
        catmiembro=miembro.obtenerCategoria()
        if catmiembro[0] == categoria:
            print(reporteMiembro(miembro))
    return "\nReporte finalizado."

'------------------ 5. Reporte individual --------------------'

def reporteIndividual(listaMiembros, pCedula):
    """
    Funcionalidad: imprime los datos de un miembro específico
    Entradas: listaMiembros (list)
              pCedula (int)
    Salidas: salida de los datos de ese miembro de pCedula (str)
    """
    print("\nReporte individual: ")
    for miembro in listaMiembros:
        if pCedula == miembro.obtenerCedula():
            print(reporteMiembro(miembro))
    return "\nReporte finalizado."

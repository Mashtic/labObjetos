#Elaborado por: Ian Coto Soto, Fabián Araya Ortega
#Fecha de creación: 19/10/2022 3:35 pm
#Fecha de modificación 20/10/2022 6:00 pm
#Versión de Python 3.10.6
#Variables globales

# Librerias importadas
from funcionesObjetos import * # Se importan las funciones del archivo para ser llamadas
                               # según la opción solicitada
import re

# Definir funciones E/S y validaciones

'------------------ Insertar miembro --------------------'

def insertarMiembroAux(cant):
    """
    Funcionalidad: valida datos de entrada
    Entradas: cant (int) (cant > 50 o cant <=0)
    Salidas: resultado insertarMiembro(cant) (list)
    """
    try:
        cant=int(cant)
        if cant > 50 or cant <=0: # Equipos tradicionales de máximo 50 personas y mínimo 1
            return "Debe digitar una cantidad de miembros entre 1 y 50."
        return insertarMiembro(cant)
    except:
        return "La cantidad de miembros debe ser un número entero positivo."

def insertarMiembroES():
    """
    Funcionalidad: entrada y salida de datos
    Entradas: cant (str)
    Salidas: resultado insertarMiembroAux (list) o mensaje de retroalimentación
             para realizar corrección (str)
    """
    cant=input("\nDigite la cantidad de personas conforman el grupo de trabajo: ")
    return insertarMiembroAux(cant)

'------------------ 1. Modificar miembro --------------------'

def modificarMiembroAux(listaMiembros, pCedula):
    """
    Funcionalidad: valida datos de entrada
    Entradas: listaMiembros (list)
              pCedula (int)
    Salidas: resultado modificarMiembro(cant) (list)
    """
    if not encontrarMiembro(listaMiembros, pCedula): # Verifica que se encuentre en la planilla
        return "Asegúrese que la cédula sea de un miembro existente."
    return modificarMiembro(listaMiembros, pCedula)

def modificarMiembroES(listaMiembros):
    """
    Funcionalidad: entrada y salida de datos
    Entradas: listaMiembros (list)
    Salidas: resultado modificarMiembroAux (list) o mensaje de retroalimentación
             para realizar corrección (str)
    """
    cedula = validarCedula()
    return modificarMiembroAux(listaMiembros, cedula)

'------------------ 2. Eliminar miembro --------------------'

def eliminarMiembroAux(listamiembros, cedula):
    """
    Funcionalidad: valida datos de entrada
    Entradas: listaMiembros (list)
              cedula (int)
    Salidas: resultado eliminarMiembro o un string
    """
    if esCedula(cedula)==True:
        cedula=int(cedula)
        return eliminarMiembro(listamiembros, cedula)
    else:
        return "El formato de la cédula es incorrecto"

def eliminarMiembroES(listamiembros):
    """
    Funcionalidad: entrada y salida de datos
    Entradas: listaMiembros (list)
    Salidas: resultado eliminarMiembroAux
    """
    cedula=input("Digite el número de cedula de la paersona que quiere eliminar: ")
    return print(eliminarMiembroAux(listamiembros, cedula))

'------------------ 3. Reporte completo --------------------'
# No se hacen funciones de E/S o validaciones

'------------------ 4. Reporte categorías --------------------'

def reporteCategoriaAux(listamiembros, categoria):
    if re.match("[1-4]", categoria):
        categoria=int(categoria)
        return reporteCategoria(listamiembros, categoria) 
    else:
        return "La categoría indicada no es válida."

def reporteCategoriaES(listamiembros):
    print("Categorías:\n1. Analista\n2. Diplomáticos\n3. Centinelas\n4. Exploradores")
    categoria=input("Digite el número de la categoría: ")
    return print(reporteCategoriaAux(listamiembros, categoria))

'------------------ 5. Reporte individual --------------------'

def reporteIndividualAux(listaMiembros, pCedula):
    """
    Funcionalidad: valida datos de entrada
    Entradas: listaMiembros (list)
              pCedula (int)
    Salidas: resultado reporteIndividual(cant) (list) / mensaje retroalimentación (str)
    """
    if not encontrarMiembro(listaMiembros, pCedula):
        return "Asegúrese que la cédula sea de un miembro existente."
    return reporteIndividual(listaMiembros, pCedula)

def reporteIndividualES(listaMiembros):
    """
    Funcionalidad: entrada y salida de datos
    Entradas: listaMiembros (list)
              cedula (int)
    Salidas: resultado reporteIndividualAux (str)
    """
    cedula = validarCedula()
    return reporteIndividualAux(listaMiembros, cedula)


# Función menú
def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario.
                    Se sale del mismo al introducir la opción 0.
    Entradas: opcion (str): opción que quiere realizar el usuario 
    Salidas: Resultado según la opción solicitada (se llama a la
             función del archivo "Funciones") 
    """
    print('\n------------------------------------\n' +
          "\n       Laboratorio de Objetos\n" + 
          '\n------------------------------------')
    listamiembros = insertarMiembroES()
    while True: # Muestra el menú al usuario de manera repetida
        print("\n************************************\n" +
               "\n         Opciones\n" +
               "\n************************************\n" +
               "\n1. Modificar miembro" +
               "\n2. Eliminar miembro" +
               "\n3. Reporte completo" +
               "\n4. Reporte categorías" +
               "\n5. Reporte individual" +
               "\n0. Salir") # Muestra las opciones
        opcion = input("\nEscoja una opción: ")
        if opcion == '1': # Si es igual a la opción, entra y llama a la respectiva función
                          # Muestra al usuario el número de reto
                          # y qué hace
            print("\nOpción 1.")
            modificarMiembroES(listamiembros)
        elif opcion == '2':
            print("\nOpción 2.")
            eliminarMiembroES(listamiembros)
        elif opcion == '3':
            print("\nOpción 3.")
            print(reporteCompleto(listamiembros))
        elif opcion == '4':
            print("\nOpción 4.")
            reporteCategoriaES(listamiembros)
        elif opcion == '5':
            print("\nOpción 5.")
            print(reporteIndividualES(listamiembros))
        elif opcion == '0': # Cuando se introduce 0, termina el ciclo con un break
            break  
        else: # Si no selecciona ninguna de las opciones, muestra el mensaje y
              # vuelve al comienzo del ciclo
            print("Indique una opción según las indicadas previamente.")
    return print("\n¡Gracias por usar el programa!")


# Programa principal

menu()
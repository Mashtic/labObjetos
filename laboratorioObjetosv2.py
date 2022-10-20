###########################################################
#Elaborado por: XXX
#Fecha de Realización: XX/XX/XXXX XX:XX
#Ultima actualización: XX/XX/XXXX XX:XX
###########################################################

#Importación de librerías
import pickle

#Definición de variables globales

#Definción de clases
class Compa:
    """Definición de Atributos de la clase"""

    """Definición de los métodos de la clase"""
    def __init__(self):
        """
        Método constructor = Crea la estructura de la clase perro
        Método que se llama al instanciar
        """
        self.nombre=()
        self.cedula=0
        self.categoria=[]
        self.estado=True
   
    def asignarNombre(self, nom, ape1, ape2):
        """
        F: Asigna el nombre a una mascota
        E: el nombre del perro (string)
        S: Asigna un nombre al atributo nombre del perro
        """   
        nombrecom=[]
        nombrecom.append(nom)
        nombrecom.append(ape1)
        nombrecom.append(ape2)
        self.nombre=tuple(nombrecom)
        return
    
    def asignarCedula(self,pcedula):
        """
        F: Asigna la raza de la mascota
        E: Nombre de la raza del perro (string)
        S: Asigna la raza al atributo raza del perro
        """
        self.cedula=pcedula
        return
    
    def asignarCategoria(self, pnum, pstring):
        """
        F: Asigna la Edad de la mascota
        E: La edad del perro (int)
        S: Asigna la edad al atributo edad del perro
        """
        
        self.categoria.append(pnum)
        self.categoria.append(pstring)
        return
    
    def asignarEstado(self,pestado):
        """
        F: Define el color del pelo del perro
        E: El código del color del perro (int)
        S: Asigna el color del pelo al atributo color del perro
        """ 
        self.estado=pestado
        return
    
    def obtenerInfo(self):
        """
        F:Devuelve sólo el nombre del perro. 
        E:NA
        S:Nombre del perro
        """
        return self.nombre, self.cedula, self.categoria, self.estado

##########################
####Programa Principal####
##########################
    


















        

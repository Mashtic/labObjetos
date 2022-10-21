# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 19/10/2022 08:31 pm
# Última modificación: 20/10/2022 01:43 pm
# Versión: 3.10.8

# Definción de clases

class Miembro:

    """Definición de los métodos de la clase"""
    def __init__(self):
        """
        Método constructor = Crea la estructura de la clase Miembro
        Método que se llama al instanciar
        """
        self.nombre = ()
        self.cedula = 0
        self.categoria = []
        self.estado = True
   
    def asignarNombre(self, pNom, pApe1, pApe2):
        """
        Función: asigna el nombre al miembro
        Entrada: nom, ape1, ape2 (string): nombre y dos apellidos
        Salida: asigna un nombre al atributo nombre del miembro
        """   
        nombrecom = []
        nombrecom.append(pNom)
        nombrecom.append(pApe1)
        nombrecom.append(pApe2)
        self.nombre = tuple(nombrecom)
        return
    
    def asignarCedula(self, pCedula):
        """
        Función: asigna la cédula al miembro
        Entrada: pCedula (int)
        Salida: asigna la cédula al atributo cédula del miembro
        """   
        self.cedula = pCedula
        return
    
    def asignarCategoria(self, pCateg, pPersIniciales):
        """
        Función: asigna la categoría al miembro
        Entrada: pCateg (int) (1-4)
                 pPersIniciales (str)
        Salida: asigna la categoría al atributo categoria del miembro
        """   
        self.categoria.append(pCateg)
        self.categoria.append(pPersIniciales)
        return
    
    def asignarEstado(self, pEstado):
        """
        Función: asigna el estado al miembro
        Entrada: pEstado (bool)
        Salida: asigna el estado al atributo estado del miembro
        """  
        self.estado = pEstado
        return

    def obtenerNombre(self):
        """
        Función: devuelve el atributo nombre del miembro
        Entrada: N/A
        Salida: self.nombre (tuple)
        """  
        return self.nombre
    
    def obtenerCedula(self):
        """
        Función: devuelve el atributo cedula del miembro
        Entrada: N/A
        Salida: self.cedula (int)
        """  
        return self.cedula

    def obtenerCategoria(self):
        """
        Función: devuelve el atributo categoria del miembro
        Entrada: N/A
        Salida: self.categoria (list)
        """  
        return self.categoria

    def obtenerEstado(self):
        """
        Función: devuelve el atributo estado del miembro
        Entrada: N/A
        Salida: self.estado (bool)
        """  
        return self.estado
    
    def obtenerInfo(self):
        """
        Función: devuelve todos los atributos del miembro
        Entrada: N/A
        Salida: self.nombre (tuple) 
                self.cedula (int)
                self.categoria (list)
                self.estado (bool)
        """  
        return self.nombre, self.cedula, self.categoria, self.estado
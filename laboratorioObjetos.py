###########################################################
#Elaborado por: XXX
#Fecha de Realización: XX/XX/XXXX XX:XX
#Ultima actualización: XX/XX/XXXX XX:XX
###########################################################

#Importación de librerías
import pickle

#Definición de variables globales
caninos=[]

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
    
    def mostrarNombre(self):
        """
        F:Devuelve sólo el nombre del perro. 
        E:NA
        S:Nombre del perro
        """
        return self.nombre
    
    def indicarDatos(self):
        """
        F:ColordePelo,
        E:el codigo del color del perro (int)
        S:Asigna el color del pelo al atributo color del perro
        """
        return "El perro: "+self.nombre+", es de la raza: "+self.raza+",su color de pelaje es:"+self.color+" y su edad es:"+self.edad

#definición de funciones
def graba(nomArchGrabar,lista):
    #Función que graba un archivo con una lista de estudiantes
    try:
        f=open(nomArchGrabar,"wb")
        print("1.Voy a grabar el archivo: ", nomArchGrabar)
        pickle.dump(lista,f)
        print("1.Voy a cerrar el archivo: ", nomArchGrabar)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)

def lee (nomArchLeer):
    #Función que lee un archivo con una lista de estudiantes
    lista=[]
    try:
        f=open(nomArchLeer,"rb")
        print("2. Voy a leer el archivo: ", nomArchLeer)
        lista = pickle.load(f)
        print("2. Voy a cerrar el archivo: ", nomArchLeer)
        f.close()
    except:
        print("Error al leer el archivo: ", nomArchLeer)
    return lista    
  
##########################
####Programa Principal####
##########################
    
vnombre=input("Ingrese el nombre del perro: ")
perrito=Perro(vnombre)#instaciación de la variable, llama al método init
#perrito.asignarNombre(vnombre) #por ende, ya no se ocupa. 

vraza=input("Ingrese la raza del perro: ")
perrito.asignarRaza(vraza)

vedad=input("Ingrese la edad del perro: ")
perrito.asignarEdad(vedad)

print("---COLORES DE PELAJE---")
print("1-Negro")
print("2-Blanco")
print("3-Gris")
print("4-Café")
print("5-Combinado")
vcolor=int(input("Digite el número correspondiente al color del pelo: "))
perrito.asignarColor(vcolor)

print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Se ha registrado correctamente el perro: ", perrito.mostrarNombre())
print("Todos sus datos son: ")
print(perrito.indicarDatos())
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
caninos.append(perrito) #Almacena el objeto en la lista
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")


vnombre=input("Ingrese el nombre del perro: ")
perrito2=Perro(vnombre) #instaciación de la variable, llama al método init
perrito2.asignarNombre(vnombre)

vraza=input("Ingrese la raza del perro: ")
perrito2.asignarRaza(vraza)

vedad=input("Ingrese la edad del perro: ")
perrito2.asignarEdad(vedad)

print("---COLORES DE PELAJE---")
print("1-Negro")
print("2-Blanco")
print("3-Gris")
print("4-Café")
print("5-Combinado")
vcolor=int(input("Digite el número correspondiente al color del pelo del perro: "))
perrito2.asignarColor(vcolor)

print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Se ha registrado correctamente el perro: ", perrito2.mostrarNombre())
print("Todos sus datos son: ")
print(perrito2.indicarDatos())
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
caninos.append(perrito2)

print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
graba("veterinaria",caninos)
lista = lee("veterinaria")
"""
#Representa la función de guardar
archivo =open("veterinaria","wb")
pickle.dump(caninos,archivo)
archivo.close()
"""

"""
#reprenta función de leer de archivo
with open("veterinaria","rb") as f:
    print("2. Voy a leer el archivo: veterinaria")
    lista = pickle.load(f)
    print("2. Voy a cerrar el archivo: veterinaria")
"""
#Saca los datos de cada elemento de la lista
print(lista[0].indicarDatos())
print(lista[1].indicarDatos())
print(lista)
print(caninos)


##########################
######RECOMENDACION#######
##########################
#Cree esta programación en 3 archivos: clase.py, archivo.py, veterinaria.py






















        

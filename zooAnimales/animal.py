from .anfibio import Anfibio
from .ave import Ave
from .mamifero import Mamifero
from .pez import Pez
from .reptil import Reptil
class Animal:
    _totalAnimales=0
    def __init__(self,nombre=None,edad=0,habitat=None,genero=None):
        Animal._totalAnimales+=1
        self.nombre=nombre
        self.edad=edad
        self.habitat=habitat
        self.genero=genero
        self.zona=None
        
    def movimiento(self):
        return"desplazarse"
    
    @classmethod
    def totalPorTipo(cls):
        return "Mamiferos: " + Mamifero.cantidadMamiferos() + "\n"+"Aves: " + Ave.cantidadAves() + "\n"+"Reptiles: " + Reptil.cantidadReptiles() + "\n"+"Peces: " + Pez.cantidadPeces() + "\n"+"Anfibios: " + Anfibio.cantidadAnfibios()
    
    def __str__(self):
        return "Mi nombre es "+ self.nombre +", tengo una edad de "+ self.edad+", habito en "+self.habitat+" y mi genero es "+self.genero
    
    @classmethod
    def setTotalAnimales(cls,t):
        cls._totalAnimales=t
        
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    
    def setNombre(self,n):
        self.nombre=n
        
    def getNombre(self):
        return self.nombre
    
    def setHabitat(self,h):
        self.habitat=h
        
    def getHabitat(self):
        return self.habitat
    
    def setGenero(self,g):
        self.genero=g
    
    def getGenero(self):
        return self.genero
    
    def setZona(self, z):
        self.zona=z
        
    def getZona(self):
        return self.zona
from .animal import Animal
class Mamifero(Animal):
    _listado=[]
    caballos=0
    leones=0
    def __init__(self,nombre=None,edad=0,habitat=None,genero=None,pelaje=False,patas=4):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero._listado.append(self)
    @classmethod 
    def cantidadMamiferos(cls):
        return len(cls._listado)
    @classmethod
    def crearCaballo(cls,x,y,z):
        a=Mamifero(x, y, "pradera", z, True, 4)
        cls.caballos+=1
        return a
    @classmethod
    def crearLeon(cls,x,y,z):
        a=Mamifero(x, y, "selva", z, True, 4)
        cls.leones+=1
        return a
    
    @classmethod
    def setListado(cls,l):
        cls._listado=l
        
    @classmethod
    def getListado(cls):
        return cls._listado
    
    def setPelaje(self,c):
        self._pelaje=c
        
    def isPelaje(self):
        return self._pelaje
    
    def setPatas(self,p):
        self._patas=p
        
    def getPatas(self):
        return self._patas
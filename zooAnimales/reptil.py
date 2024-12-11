from .animal import Animal
class Reptil(Animal):
    _listado=[]
    iguanas=0
    serpientes=0
    def __init__(self,nombre=None,edad=0,habitat=None,genero=None,colorEscamas=None,largoCola=0):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil._listado.append(self)
    @classmethod 
    def cantidadReptiles(cls):
        return len(cls._listado)
    def movimiento(self):
        return "reptar"
    @classmethod
    def crearIguana(cls,x,y,z):
        a=Reptil(x, y, "humedal", z, "verde", 3)
        cls.iguanas+=1
        return a
    @classmethod
    def crearSerpiente(cls,x,y,z):
        a=Reptil(x,y,"jungla",z,"blanco",1)
        cls.serpientes+=1
        return a
    
    @classmethod
    def setListado(cls,l):
        cls._listado=l
        
    @classmethod
    def getListado(cls):
        return cls._listado
    
    def setColorEscamas(self,c):
        self._colorEscamas=c
        
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setLargoCola(self,p):
        self._largoCola=p
        
    def getLargoCola(self):
        return self._largoCola
    
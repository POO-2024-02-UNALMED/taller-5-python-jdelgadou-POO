from zooAnimales.animal import Animal
class Anfibio(Animal):
    _listado=[]
    ranas=0
    salamandras=0
    def __init__(self,nombre=None,edad=0,habitat=None,genero=None,colorPiel=None,venenoso=False):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._listado.append(self)
    @classmethod 
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "saltar"
    
    @classmethod
    def crearRana(cls,x,y,z):
        a=Anfibio(x, y, "selva", z, "rojo", True)
        cls.ranas+=1
        return a
    @classmethod
    def crearSalamandra(cls,x,y,z):
        a=Anfibio(x, y, "selva", z, "negro", False)
        cls.salamandras+=1
        return a
    
    @classmethod
    def setListado(cls,l):
        cls._listado=l
        
    @classmethod
    def getListado(cls):
        return cls._listado
    
    def setColorPiel(self,c):
        self._colorPiel=c
        
    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenoso(self,v):
        self._venenoso=v
        
    def isVenenoso(self):
        return self._venenoso
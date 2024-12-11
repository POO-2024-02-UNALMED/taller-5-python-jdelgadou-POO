from zooAnimales.animal import Animal
class Ave(Animal):
    _listado=[]
    halcones=0
    aguilas=0
    def __init__(self,nombre=None,edad=0,habitat=None,genero=None,colorPlumas=None):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas=colorPlumas
        Ave._listado.append(self)
    @classmethod 
    def cantidadAves(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "volar"
    
    @classmethod
    def crearHalcon(cls,x,y,z):
        a=Ave(x, y, "montanas", z, "cafe glorioso")
        cls.halcones+=1
        return a
    @classmethod
    def crearAguila(cls,x,y,z):
        a=Ave(x, y, "montanas", z, "blanco y amarrillo")
        cls.aguilas+=1
        return a
    
    @classmethod
    def setListado(cls,l):
        cls._listado=l
        
    @classmethod
    def getListado(cls):
        return cls._listado
    
    def setColorPlumas(self,c):
        self._colorPlumas=c
        
    def getColorPlumas(self):
        return self._colorPlumas

from animal import Animal
class Pez(Animal):
    _listado=[]
    salmones=0
    bacalaos=0
    def __init__(self,nombre=None,edad=0,habitat=None,genero=None,colorEscamas=None,cantidadAletas=0):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Pez._listado.append(self)
    @classmethod 
    def cantidadPeces(cls):
        return len(cls._listado)
    def movimiento(self):
        return "nadar"
    @classmethod
    def crearSalmon(self,x,y,z):
        a=Pez(x, y, "oceano", z, "rojo", 6)
        salmones+=1
        return a
    @classmethod
    def crearBacalao(self,x,y,z):
        a=Pez(x, y, "oceano", z, "gris", 6)
        bacalaos+=1
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
    
    def setCantidadAletas(self,p):
        self._cantidadAletas=p
        
    def getCantidadAletas(self):
        return self._cantidadAletas
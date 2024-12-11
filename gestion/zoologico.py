class Zoologico:
    def __init__(self,nombre=None, ubicacion=None):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zona=[]
        
    def agregarZonas(self,zona):
        self._zona.append(zona)
        
    def cantidadTotalAnimales(self):
        c=0
        for i in self._zona:
            c+=i.cantidadAnimales()
        return c
    
    def setNombre(self,nombre):
        self._nombre=nombre
        
    def getNombre(self):
        return self._nombre
    
    def setUbicacion(self,ubicacion):
        self._ubicacion=ubicacion
        
    def getUbicacion(self):
        return self._ubicacion
    
    def getZona(self):
        return self._zona
    
    def setZona(self,zona):
        self._zona=zona
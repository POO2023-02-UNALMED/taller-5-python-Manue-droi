
from zooAnimales.animal import Animal

class Pez(Animal):
    salmones: int = 0
    bacalaos: int = 0
    listado = []
    
    def _init_(self, nombre: str, edad: int, habitat: str, genero: str, colorEscamas: str, cantidadAletas: int):
        super()._init_(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        Pez.listado.append(self)
    
    def _init_(self):
        Pez.listado.append(self)
    
    @staticmethod
    def cantidadPeces() -> int:
        return len(Pez.listado)
    
    def movimiento(self) -> str:
        return "nadar"
    
    @staticmethod
    def crearSalmon(nombre: str, edad: int, genero: str):
        Pez.salmones += 1
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.listado.append(salmon)
        return salmon
    
    @staticmethod
    def crearBacalao(nombre: str, edad: int, genero: str):
        Pez.bacalaos += 1
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.listado.append(bacalao)
        return bacalao
    
    def getColorEscamas(self) -> str:
        return self.colorEscamas
    
    def getCantidadAletas(self) -> int:
        return self.cantidadAletas
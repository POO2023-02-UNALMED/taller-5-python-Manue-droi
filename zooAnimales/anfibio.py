from typing import List

class Animal:
    def _init_(self, nombre: str, edad: int, habitat: str, genero: str):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero

    def movimiento(self) -> str:
        pass

class Anfibio(Animal):
    ranas: int = 0
    salamandras: int = 0
    listado: List[anfibio] = []
    
    def _init_(self, nombre: str, edad: int, habitat: str, genero: str, colorPiel: str, venenoso: bool):
        super()._init_(nombre, edad, habitat, genero)
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        Anfibio.listado.append(self)

    def _init_(self):
        Anfibio.listado.append(self)

    @staticmethod
    def cantidadAnfibios() -> int:
        return len(Anfibio.listado)

    def movimiento(self) -> str:
        return "saltar"

    @staticmethod
    def crearRana(nombre: str, edad: int, genero: str) -> Anfibio:
        Anfibio.ranas += 1
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.listado.append(rana)
        return rana

    @staticmethod
    def crearSalamandra(nombre: str, edad: int, genero: str) -> anfibio:
        Anfibio.salamandras += 1
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio.listado.append(salamandra)
        return salamandra

    def getColorPiel(self) -> str:
        return self.colorPiel

    def isVenenoso(self) -> bool:
        return self.venenoso
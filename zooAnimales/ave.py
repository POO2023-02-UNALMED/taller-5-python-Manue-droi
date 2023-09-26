from typing import List

class Animal:
    def __init__(self, nombre: str, edad: int, habitat: str, genero: str):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero

class Ave(Animal):
    plural = "Aves"
    listado: List[Ave] = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre: str = None, edad: int = 0, habitat: str = None, genero: str = None, colorPlumas: str = None):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPlumas = colorPlumas
        Ave.listado.append(self)

    @staticmethod
    def cantidadAves() -> int:
        return len(Ave.listado)

    def movimiento(self) -> str:
        return "volar"

    @staticmethod
    def getListado() -> List[Ave]:
        return Ave.listado

    def getColorPlumas(self) -> str:
        return self.colorPlumas

    @staticmethod
    def setListado(listado: List[Ave]) -> None:
        Ave.listado = listado

    def setColorPlumas(self, colorPlumas: str) -> None:
        self.colorPlumas = colorPlumas

    @staticmethod
    def crearHalcon(nombre: str, edad: int, genero: str) -> Ave:
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @staticmethod
    def crearAguila(nombre: str, edad: int, genero: str) -> Ave:
        Ave.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
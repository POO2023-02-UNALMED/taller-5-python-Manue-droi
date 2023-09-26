from typing import List
from zooAnimales import Animal


class Ave(Animal):
    plural = "Aves"
    listado = []
    halcones = 0
    aguilas = 0

    def _init_(self, nombre: str = None, edad: int = 0, habitat: str = None, genero: str = None, colorPlumas: str = None):
        super()._init_(nombre, edad, habitat, genero)
        self.colorPlumas = colorPlumas
        Ave.listado.append(self)

    @staticmethod
    def cantidadAves() -> int:
        return len(Ave.listado)

    def movimiento(self):
        return "volar"

    @staticmethod
    def getListado():
        return Ave.listado

    def getColorPlumas(self) -> str:
        return self.colorPlumas

    @staticmethod
    def setListado(listado) -> None:
        Ave.listado = listado

    def setColorPlumas(self, colorPlumas: str) -> None:
        self.colorPlumas = colorPlumas

    @staticmethod
    def crearHalcon(nombre: str, edad: int, genero: str) :
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @staticmethod
    def crearAguila(nombre: str, edad: int, genero: str):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
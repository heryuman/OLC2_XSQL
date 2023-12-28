from abc import ABCMeta, abstractmethod
class Iexpresion:
    @abstractmethod
    def getTipo(controlador,tablaSimbolo):
        pass
    @abstractmethod
    def getValor(controlador,tablaSimbolo):
        pass
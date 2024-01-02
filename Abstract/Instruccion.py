from abc import ABC, abstractmethod
from enviroment import enviroment
from Arbol.Nodo import Nodo

from Simbolo.Ambito import Ambito
#from TablaSimbolos.Tabla_Simbolos import *

class Instruccion(ABC):
    
    def __init__(self, fila, colum):
        self.fila = fila
        self.colum = colum
        self.env = enviroment()
    
    @abstractmethod
    def compilar(self, tree, tablaSim:Ambito,nodo:Nodo,output:[]):
        pass
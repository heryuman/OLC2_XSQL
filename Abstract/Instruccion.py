from abc import ABC, abstractmethod
#from TablaSimbolos.Tabla_Simbolos import *

class Instruccion(ABC):
    
    def __init__(self, fila, colum):
        self.fila = fila
        self.colum = colum
    
    @abstractmethod
    def compilar(self, tree, table):
        pass
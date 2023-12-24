from typing import List
from Abstract.Instruccion import Instruccion
class AST:
    def __init__(self, instrucciones:[]) -> None:
        self.instrucciones = instrucciones

    
    def getInstrucciones(self):
        return self.instrucciones
    
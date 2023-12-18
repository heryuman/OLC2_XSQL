from typing import List
from Simbolo.Simbolo import Simbolo
class Ambito:

    def __init__(self):
        self._ambito:str = None
        self.simbolos: List[Simbolo] = None
    
    def addSimbolo(self, simbolo:Simbolo):
        self.simbolos.append(simbolo)
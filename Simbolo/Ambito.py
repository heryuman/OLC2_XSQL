from typing import List
from Simbolo.Simbolo import Simbolo
class Ambito:

    def __init__(self, ambitoPadre = None):
        self.padre = ambitoPadre
        self.simbolos:List[Simbolo] = [] 
    
    def addSimbolo(self, simbolo:Simbolo):
        self.simbolos.append(simbolo)

    def getValueFromSimbolo(self, id)->Simbolo:

        for sim in self.simbolos:
            if sim._identificador == id:
                return sim
            
        return None
    
    def setValueFromId(self, id:str, newValue:str):

        for sim in self.simbolos:
            if sim._identificador == id:
                sim._valor = newValue



        
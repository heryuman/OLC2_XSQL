from typing import List

class Nodo:

    def __init__(self, token:str, lexema:str, linea:int, columna:int):
        self._token = token
        self._lexema = lexema
        self._linea = linea
        self._columna = columna
        self._hijos: List[Nodo] =[]  
    
    def addHijo(self, nodo):
        self._hijos.append(nodo)



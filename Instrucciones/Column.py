from Abstract.Instruccion import Instruccion
from typing import List

class column(Instruccion):

    def __init__ (self,id:str, tipo:str, tamanios:str,presicion:str, restriciones:List[str], fila, colum):
        super().__init__(fila, colum)
        self.id = id
        self.tipo = tipo
        self.tamanio = 0 if tamanios== None else tamanios
        self.presicion = presicion
        self.restriccion = []
    
    def compilar(self, tree, table):
        
        print
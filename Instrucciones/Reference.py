from Abstract.Instruccion import Instruccion
from Arbol.Nodo import Nodo
from Simbolo.Ambito import Ambito

class Reference(Instruccion):

    def __init__(self,tabla:str,column:str, fila, colum):
        super().__init__(fila, colum)
        self.tablaReference:str = tabla
        self.columReference:str = column


    def compilar(self, tree, tablaSim: Ambito, nodo: Nodo, output: []):
        return super().compilar(tree, tablaSim, nodo, output)
    
    
from Abstract.Instruccion import Instruccion
from Arbol.Nodo import Nodo
from Simbolo.Ambito import Ambito

class Variable(Instruccion):

    def __init__(self, id:str, tipo:str, fila, colum):
        super().__init__(fila, colum)
        self.id = id
        self.tipo = str

    def compilar(self, tree, tablaSim: Ambito, nodo: Nodo, output: []):
        return super().compilar(tree, tablaSim, nodo, output)
        #return super().compilar(tree, table)

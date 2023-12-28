from Abstract.Instruccion import Instruccion
from Arbol.Nodo import Nodo
from Simbolo.Ambito import Ambito
class Expresion(Instruccion):

    def __init__(self, fila, colum):
        super().__init__(fila, colum)

    def compilar(self, tree, tablaSim: Ambito, nodo: Nodo, output: []):
        return super().compilar(tree, tablaSim, nodo, output)
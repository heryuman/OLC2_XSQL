from Abstract.Instruccion import Instruccion

class Delete(Instruccion):

    def __init__(self, fila, colum):
        super().__init__(fila, colum)

    
    def compilar(self, tree, table):
        return super().compilar(tree, table)
from Abstract.Instruccion import Instruccion

class Use(Instruccion):
    def __init__(self, fila, colum):
        super().__init__(fila, colum)

    def compilar(self, tree, table):
        pass
        #return super().compilar(tree, table)
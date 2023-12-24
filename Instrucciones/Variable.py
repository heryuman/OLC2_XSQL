from Abstract.Instruccion import Instruccion

class Variable(Instruccion):

    def __init__(self, id:str, tipo:str, fila, colum):
        super().__init__(fila, colum)
        self.id = id
        self.tipo = str

    def compilar(self, tree, table):
        return super().compilar(tree, table)

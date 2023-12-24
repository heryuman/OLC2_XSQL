from Abstract.Instruccion import Instruccion

class Reference(Instruccion):

    def __init__(self,tabla:str,column:str, fila, colum):
        super().__init__(fila, colum)
        self.tablaReference:str = tabla
        self.columReference:str = column


    def compilar(self, tree, table):
        return super().compilar(tree, table)
    
    
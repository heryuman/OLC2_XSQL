from Abstract.Instruccion import Instruccion
from Instrucciones.Variable import Variable

class CreateSP (Instruccion):

    def __init__(self, sp_name:str,parametros:[Variable],instrucciones:[] ,fila, colum):
        super().__init__(fila, colum)
        self.sp_name = sp_name
        self.parametros = parametros
        self.instrucciones:[Variable] = instrucciones 
    
    def compilar(self, tree, table):
        return super().compilar(tree, table)

from Abstract.Instruccion import Instruccion
from Arbol.Nodo import Nodo
from Instrucciones.Variable import Variable
from Simbolo.Ambito import Ambito

class CreateSP (Instruccion):

    def __init__(self, sp_name:str,parametros:[Variable],instrucciones:[] ,fila, colum):
        super().__init__(fila, colum)
        self.sp_name = sp_name
        self.parametros = parametros
        self.instrucciones:[Variable] = instrucciones 
    
    def compilar(self, tree, tablaSim: Ambito, nodo: Nodo, output: []):
        return super().compilar(tree, tablaSim, nodo, output)

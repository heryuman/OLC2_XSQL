from Abstract.Instruccion import Instruccion

class Restriccion(Instruccion):

    def __init__(self, tipoRest:str ,fila, colum):
        super().__init__(fila, colum)
        self.tipoRest = tipoRest
        
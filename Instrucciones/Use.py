from Abstract.Instruccion import Instruccion
from Simbolo.Ambito import Ambito

class Use(Instruccion):
    def __init__(self, db_name,fila, colum):
        super().__init__(fila, colum)
        self.db_name = db_name

    def compilar(self, tree, table:Ambito):

        ambito = self.getAmbitoPadre(table)

        ambito.setValueFromId(self.env.useDB, self.db_name)
        
        #return super().compilar(tree, table)

    ##El useDB, solo debe de estar dentro del padre
    def getAmbitoPadre(self, ambito:Ambito)->Ambito:
        if ambito.padre == None:
            return ambito
        return ambito.padre

from Abstract.Instruccion import Instruccion
from Arbol.Nodo import Nodo
from Simbolo.Ambito import Ambito
from util.manipulador_xml import CREATE_XML

class Use(Instruccion):
    def __init__(self, db_name,fila, colum):
        super().__init__(fila, colum)
        self.db_name = db_name
        self.manipulador:CREATE_XML = CREATE_XML()

    def compilar(self, tree, tablaSim: Ambito, nodo: Nodo, output: []):
        #return super().compilar(tree, tablaSim, nodo, output)
        if not self.manipulador.exist_db(self.db_name):
            output.append(self.env.dbNotFound)
            return
        nodo._token = "USE"
        nodo._lexema = "use"
        nodo._linea = self.fila
        nodo._columna = self.colum

        hijo = Nodo("ID", self.db_name, self.fila, self.colum)

        nodo.addHijo(hijo)
        ambito = self.getAmbitoPadre(tablaSim)

        ambito.setValueFromId(self.env.useDB, self.db_name)
        output.append("Se ha selecionado una base de datos.")
        #return super().compilar(tree, table)

    ##El useDB, solo debe de estar dentro del padre
    def getAmbitoPadre(self, ambito:Ambito)->Ambito:
        if ambito.padre == None:
            return ambito
        return ambito.padre

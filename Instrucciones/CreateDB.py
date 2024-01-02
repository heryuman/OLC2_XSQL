from Abstract.Instruccion import Instruccion
from Arbol.Nodo import Nodo
from Simbolo.Ambito import Ambito
from util.manipulador_xml import CREATE_XML
class CreateDB (Instruccion):

    def __init__(self,dbName:str ,fila, colum):
        super().__init__(fila, colum)
        self.dbName:str = dbName
        self.manipulador: CREATE_XML = CREATE_XML()

    def compilar(self, tree, tablaSim: Ambito, nodo: Nodo, output: []):
        #return super().compilar(tree, tablaSim, nodo, output)
        nodo._token = "CREATE DB"
        nodo._lexema = "create_db"
        nodo._linea = self.fila
        nodo._columna = self.colum

        hijo = Nodo("ID",self.dbName, self.fila, self.colum)

        nodo.addHijo(hijo)
        try:
            self.manipulador.create_db(self.dbName)
        except Exception as e:
            print(f"Error al crear la BBDD {e}")

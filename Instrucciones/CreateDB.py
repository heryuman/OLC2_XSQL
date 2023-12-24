from Abstract.Instruccion import Instruccion
from util.manipulador_xml import CREATE_XML
class CreateDB (Instruccion):

    def __init__(self,dbName:str ,fila, colum):
        super().__init__(fila, colum)
        self.dbName:str = dbName
        self.manipulador: CREATE_XML = CREATE_XML()

    def compilar(self, tree, table):

        try:
            self.manipulador.create_db(self.dbName)
        except Exception as e:
            print(f"Error al crear la BBDD {e}")

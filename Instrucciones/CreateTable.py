from Abstract.Instruccion import Instruccion
from util.manipulador_xml import CREATE_XML
from typing import List
from Instrucciones.Column import column
from util.column import COLUM
from util.table import TBL
class CreateTable (Instruccion):


    def __init__(self, identificador:str, dbName:str, listaColumns:List[column],fila:int, colum:int, newLine = False):
        super().__init__(fila, colum)
        #nombre de la tabla
        self.id = identificador
        self.newLine = newLine
        self.dbAplied = "BasePrueba"
        self.manipulador = CREATE_XML()
        self.columnas:List[column] = listaColumns

    def compilar(self, tree, tableSim):
        
        
        table = TBL(self.dbAplied,self.id)

        for col in self.columnas:
            column = COLUM(col.id, col.tipo, None, None,col.tamanio,None)
            table.insert_column(column)

        self.manipulador.insert_table(table)


        


    

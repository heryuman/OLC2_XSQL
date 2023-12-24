from Abstract.Instruccion import Instruccion
from util.manipulador_xml import CREATE_XML
from typing import List
from Instrucciones.Column import column
from util.column import COLUM
from util.table import TBL
from Simbolo.Ambito import Ambito
class CreateTable (Instruccion):


    def __init__(self, identificador:str, dbName:str, listaColumns:List[column],fila:int, colum:int, newLine = False):
        super().__init__(fila, colum)
        #nombre de la tabla
        self.id = identificador
        self.newLine = newLine
        self.dbAplied = dbName
        self.manipulador = CREATE_XML()
        self.columnas:List[column] = listaColumns

    def compilar(self, tree, tablaSim:Ambito):
        table = TBL(self.dbAplied,self.id)
        
        if self.dbAplied == None:
            simbolo = tablaSim.getValueFromSimbolo(self.env.useDB)

            self.dbAplied = simbolo._valor
            table._db_name = self.dbAplied

        if self.dbAplied == None:
            print("No hay una BBDD previamente selecionada")
            return
        
        for col in self.columnas:
            
            column = COLUM(col.id, col.tipo, None, None,None,col.tamanio,"",None,col.presicion)
            
            restricciones:List[str] = col.restriccion
            for res in restricciones:
                if isinstance(res,Instruccion):
                    column._tab_refernce = res.tablaReference
                    column._col_fer = res.columReference

                else:
                    if res.upper() =="FOREING KEY":
                        print("se hara referencia a una tabla")
                    elif res.upper()=="PRIMARY KEY":
                        column._pk = True
                    elif res.upper() == "NOT NULL":
                        column._isNull = False
                    elif res.upper == "NULL":
                        column._isNull = True


            table.insert_column(column)



        self.manipulador.insert_table(table)


        


    

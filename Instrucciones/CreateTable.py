from Abstract.Instruccion import Instruccion
from Arbol.Nodo import Nodo
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

    def compilar(self, tree, tablaSim: Ambito, nodo: Nodo, output: []):
        #return super().compilar(tree, tablaSim, nodo, output)

        
        nodo._token = "CREATE_TABLE"
        nodo._lexema = "create_table"
        nodo._columna = self.colum
        nodo._linea = self.fila

        hijo = Nodo("Table",self.id,self.fila, self.colum)


        nodo.addHijo(hijo)

        for col in self.columnas:
            tipo = Nodo("TIPO",col.tipo,col.fila,col.colum)
            identi = Nodo("ID",col.id,col.fila, col.colum)
            tipo.addHijo(identi)
            hijo.addHijo(tipo)
        

        table = TBL(self.dbAplied,self.id)
        
        if self.dbAplied == None:
            simbolo = tablaSim.getValueFromSimbolo(self.env.useDB)

            self.dbAplied = simbolo._valor
            table._db_name = self.dbAplied

        if self.dbAplied == None:
            print("No hay una BBDD previamente selecionada")
            return
        
        for col in self.columnas:
                                            #el pk es de tipo False, posterior se hará el cambio sí así amerita
            column = COLUM(col.id, col.tipo, False, "","",col.tamanio,"",True,col.presicion)
            
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


        


    

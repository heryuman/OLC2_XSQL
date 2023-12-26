from Abstract.Instruccion import Instruccion
from Simbolo.Ambito import Ambito
from util.generic import INSERT
from util.manipulador_xml import CREATE_XML

class Insert(Instruccion):

    def __init__(self, tbl_name,lcolumns:[], lvalues:[],fila, colum):
        super().__init__(fila, colum)
        self.tb_name = tbl_name
        self.lcolumns = lcolumns
        self.lvalues = lvalues
        self.dbAplied = None
        self.manipulador:CREATE_XML = CREATE_XML()


    
    def compilar(self, tree, tablaSim:Ambito):
        
        if self.dbAplied == None:
            simbolo = tablaSim.getValueFromSimbolo(self.env.useDB)

            self.dbAplied = simbolo._valor

        if self.dbAplied == None:
            print("No hay una BBDD previamente selecionada")
            return
        
        #validamos que exista la tabla y la base

        if not self.manipulador.exist_table(self.dbAplied,self.tb_name):
            print("No existe la base de datos o la tabla")
            return
        
        obj_insert = INSERT(self.dbAplied, self.tb_name,self.lcolumns,self.lvalues)

        self.manipulador.insert_ontbl(obj_insert)
    

    
    

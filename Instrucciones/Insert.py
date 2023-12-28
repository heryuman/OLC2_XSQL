from Abstract.Instruccion import Instruccion
from Arbol.Nodo import Nodo
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


    
    def compilar(self, tree, tablaSim: Ambito, nodo: Nodo, output: []):
        #return super().compilar(tree, tablaSim, nodo, output)

        nodo._token = "INSERT"
        nodo._lexema = "insert"
        nodo._linea = self.fila
        nodo._columna = self.colum

        


        if self.dbAplied == None:
            simbolo = tablaSim.getValueFromSimbolo(self.env.useDB)

            self.dbAplied = simbolo._valor

        if self.dbAplied == None:
            print("No hay una BBDD previamente selecionada")
            return
        
        hijo1=Nodo("DBAPLIED", self.dbAplied,self.fila, self.colum)
        hijo2=Nodo("TBLAPLIED", self.tb_name,self.fila, self.colum)
        
        nodo.addHijo(hijo1)
        nodo.addHijo(hijo2)
        c:int = 0
        for col in self.lcolumns:
            named = Nodo("Name",col,self.fila,self.colum)
            valor = self.lvalues[c] if self.lvalues[c]!=None else "n/a"
            value = Nodo("VALUE",valor,self.fila, self.colum)
            named.addHijo(value)
            c=c+1
            hijo2.addHijo(named)

        #validamos que exista la tabla y la base

        if not self.manipulador.exist_table(self.dbAplied,self.tb_name):
            print("No existe la base de datos o la tabla")
            return
        
        obj_insert = INSERT(self.dbAplied, self.tb_name,self.lcolumns,self.lvalues)

        self.manipulador.insert_ontbl(obj_insert)
    

    
    

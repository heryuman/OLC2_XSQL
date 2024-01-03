from Abstract.Instruccion import Instruccion
from Arbol.Nodo import Nodo
from Simbolo.Ambito import Ambito
from util.manipulador_xml import CREATE_XML
from util.generic import SELECT

class Select(Instruccion):

    def __init__(self, variastablas:bool,listaTablas:[str], listaColumns:[str],dbAplied:str,listaCondiciones:[],fila, colum):
        super().__init__(fila, colum)
        self.sonVariasTablas:bool = variastablas
        self.listaTablas:[str] = listaTablas
        self.columnas:[str] = listaColumns
        self.dbAplied:str = dbAplied
        self.condiciones:[] = listaCondiciones
        self.manipulador:CREATE_XML = CREATE_XML()
    

    def compilar(self, tree, tablaSim: Ambito, nodo: Nodo, output: []):
        
        if self.dbAplied == None:
            simbolo = tablaSim.getValueFromSimbolo(self.env.useDB)
            self.dbAplied = simbolo._valor

        if self.dbAplied == None or self.dbAplied =="":
            #print("No hay una BBDD previamente selecionada")
            output.append(self.env.dbNotFound)
            return
        
        nodo._token ="SELECT"
        nodo._lexema ="select"
        nodo._linea = self.fila
        nodo._columna = self.colum


        hijo = Nodo("COLUMNAS","columnas",self.fila,self.colum)
        nodo.addHijo(hijo)

        if len(self.columnas) == 0:
            col = Nodo("COLUMNA","*",self.fila, self.colum)
            hijo.addHijo(col)
        else:
            for col in self.columnas:
                col = Nodo("COLUMNA",col,self.fila,self.colum)
                hijo.addHijo(col)
        
        hijo2 = Nodo("TABLES","table(s)", self.fila, self.colum)

        nodo.addHijo(hijo2)
        for table in self.listaTablas:
            tab = Nodo("TABLE",table,self.fila, self.colum)
            hijo2.addHijo(tab)

        if len(self.condiciones)>0:
            hijo3 =Nodo("CONDICIONES","condiciones",self.fila,self.colum)
            nodo.addHijo(hijo3)
            for cond in self.condiciones:
                co = Nodo("CONDICION", cond, self.fila, self.colum)
                hijo3.addHijo(co)
        
        
        obj_select = SELECT(self.sonVariasTablas,self.columnas,self.listaTablas,self.dbAplied,self.condiciones)
        
        self.manipulador.select(obj_select,output)
from FuncionesDeSistema.Fun_Suma import Fun_Suma
from Arbol.Arbol import Arbol
from Arbol.Nodo import Nodo
from util.manipulador_xml import CREATE_XML
from util.table import TBL
from util.column import COLUM



def trySuma():
    funcion = Fun_Suma()

    salida = funcion.getSuma("base1","tabla1", "columna1")

    print(salida)

def validarArbol():
    nodo1= Nodo('suma','+',0,1)
    arbol = Arbol(nodo1)
    
    nodo1_1 = Nodo('num','1',1,0)
    nodo2 = Nodo('multi','*',1,1)
    nodo2_1 = Nodo('num','5',1,1)
    nodo2_2 = Nodo('num','6',1,1)
    
    nodo1.addHijo(nodo1_1)
    nodo1.addHijo(nodo2)
    nodo2.addHijo(nodo2_1)
    nodo2.addHijo(nodo2_2)
    
    

    arbol.graficarAST()

def main():
    #print("Hola mundo2")
    #trySuma()
    ##validarArbol()
    creator = CREATE_XML()

    table = TBL("BasePrueba","Mytabla2")
    column1 = COLUM("col1","varchar","no","n/a","15","false")
    column2 = COLUM("col2","varchar","no","n/a","15",False)
    
    table.insert_column(column1)
    table.insert_column(column2)
    
    creator.insert_table(table)







if __name__ == "__main__":
    main()
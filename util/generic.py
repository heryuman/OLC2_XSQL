class GENERIC:
    def __init__(self):
        self.algo=None
    
    def centrar_ventana(self,ventana,aplicacion_ancho,aplicacion_largo):
        pantall_ancho = ventana.winfo_screenwidth()
        pantall_largo = ventana.winfo_screenheight()
        x = int((pantall_ancho/2) - (aplicacion_ancho/2))
        y = int((pantall_largo/2) - (aplicacion_largo/2))
        return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")
    
class INSERT:
    def __init__(self,db_name,tb_name,l_into,lvalues):
        self._db_name=db_name #Nombre de la base de datos donde se insertara
        self._tb_name=tb_name #Nombre de la tabla a insertar
        self._lvalues=lvalues  #Lista de valores a insertar
        self._linto=l_into     # Lista de columnas de la tabla 
                              # INSERT INTO (col1,col2,col3)VALUES(val1,val2,val3)

#SelectAll es el parametro que indica si viene un SELECT * FROM TABLA, el parametro 
#deberá ser un True en caso sea el tipo de query, y la ListaColumnas debera ser vacío []
#ListaColumnas si no fuera el caso anterior, selectAll debera ser False
#l_tb_name la lista de en caso vengan mas de una tabla a consultar
#db_name, nombre de la BD a donde se va a consultar
#l_condiciones, lista de condiciones de la consulta la lista contendra objetos de tipo CONDICION
class SELECT:
    def __init__(self,selectAll,listaColumnas,l_tb_name,db_name,l_condiciones):
        self._SelectAll=selectAll
        self._lcolumns=listaColumnas
        self._l_tbname=l_tb_name
        self._db_name=db_name
        self._lcondiciones=l_condiciones

class CONDICION:
    #from util.generic import OPERADOR
    def __init__(self,exp1,operador,exp2):
        self._exp1=exp1
        self._exp2=exp2
        self._operador=operador

from enum import Enum
class OPERADOR(Enum):
    SUMA=0
    RESTA=1
    MULTIPLICACION=2
    DIVISION=3
    IGUALACION=4
    OP_AND=5
    OP_OR=6
    DIFERENTE=7
        
    
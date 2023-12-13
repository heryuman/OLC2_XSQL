from Analizador.lexico import tokens
from object.columna import COLUMNA
from object.reference import REFERENCE
from object.tamanio import TAMANIO
from util.table import TBL
#diccionario de nombres
lista=[]
listaErrores=[]


def  p_inicio(p):
    '''inicio : instrucciones'''
    p[0] = p[1]
    

def p_instrucciones(p):
    ''' instrucciones : instrucciones instruccion'''
    if p[2] != "":
        p[1].append(p[2])
    p[0] = p[1]

def p_instrucciones_instruccion(p):
    '''instrucciones : instruccion'''
    if p[1] == "":
        p[0] = []
    else:
        p[0] = [p[1]]

def p_instruccion(p):
    '''instruccion : comandocreate'''
    p[0] = (p[1])
    

def p_comandocreate(p):
    '''comandocreate : CREATE TABLE ID PARABRE datostable PARCIERRA PYC'''
    print("cmd creand",p[2])
    print("tb name ",p[3])
    tbl=TBL()
    print("datos: ", p[5])
    
    
def p_datostable(p):
    '''datostable : datostable datotable'''
    if p[2] != "":
        p[1].append(p[2])
    p[0] = p[1]

def p_datostable_datotable(p):
    '''datostable : datotable'''
    if p[1] == "":
        p[0] = []
    else:
        p[0] = [p[1]]

def p_datotable(p):
    '''datotable : columnas'''
    p[0] = p[1]
    
def p_columnas(p):
    '''columnas : columnas COMA columna
                | columna'''
    if len(p) == 4:
        p[0]=p[3]
    else:
        p[0] = p[1]
    
def p_columna(p):
    '''columna : ID tipo tamanios
              | ID tipo restriccion
              | ID tipo 
              | ID tipo tamanios restriccion'''
    columna=None
    listColum=[]
    if len(p) == 4:
        #se crearia el xml con la estructura de una restriccion
        if isinstance(p[3],TAMANIO):
            columna = COLUMNA(p[1],p[2],False,False,"",p[3].tamanio,p[3].presicion,None,None) #no es llave primaria, no es not nul y es tamanio       
            listColum.append(columna)
        elif isinstance(p[3],str):
            if p[3].lower()=="primary key":
                columna = COLUMNA(p[1],p[2],True,False,"",getTamxTipo(p[2]),0, None,None) #cuando es una llave primaria
                listColum.append(columna)
            elif p[3].lower() == "not null":
                columna = COLUMNA(p[1],p[2],False,True,"",getTamxTipo(p[2]),0,None,None) #no es llave primaria y lleva not null
                listColum.append(columna)
        else:
            columna = COLUMNA(p[1],p[2],False,False,"",getTamxTipo(p[2]),0,p[3].colreference,p[3].tablareference) #no es llave primaria, no lleva not null y si es reference
            listColum.append(columna)
    elif len(p) == 3:
        columna = COLUMNA(p[1],p[2],False,False,"", getTamxTipo(p[2]),0,None,None) #no es llave primaria, no es llave foranea y no llena not null
        listColum.append(columna)
    elif len(p)==5:
        columna = COLUMNA(p[1],p[2],False,False,"",p[3].tamanio,p[3].presicion,p[4].colreference, p[4].tablareference)
        listColum.append(columna)
    p[0]=listColum

def getTamxTipo(tipo):
    if tipo.lower() == "int":
        return 11
    elif tipo.lower() == "text":
        return 20
    elif tipo.lower() == "date":
        return 11
    elif tipo.lower() == "decimal":
        return 5
    elif tipo.lower() == "nvarchar":
        return 15

def p_tamanios(p):
    '''tamanios : PARABRE tamanios COMA tamanio PARCIERRA
                | PARABRE tamanio PARCIERRA'''
    if len(p) == 6:
        p[0] = TAMANIO(p[2],p[4])
    elif len(p) == 4:
        p[0] = TAMANIO(p[2],0)
    
def p_tamanio(p):
    '''tamanio : NUMEROS'''
    p[0] = p[1]
    
def p_restriccion(p):
    '''restriccion : PRIMARY KEY
                   | NOT NULL
                   | reference'''
    if len(p)==3:
        p[0] = p[1] + " " + p[2]
    else:
        p[0] = p[1]

def p_reference(p):
    '''reference : REFERENCE ID PARABRE ID PARCIERRA'''
    p[0] = REFERENCE(p[2],p[4])

def p_tipo(p):
    '''tipo : INT
            | TEXT
            | nvarchar
            | DATE
            | DECIMAL'''
    p[0] = p[1]
    
def p_nvarchar(p):
    '''nvarchar : NVARCHAR PARABRE NUMEROS PARCIERRA'''
    p[0] = p[3]

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")




import ply.yacc as yacc
parser=yacc.yacc()
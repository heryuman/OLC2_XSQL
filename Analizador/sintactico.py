from Analizador.lexico import tokens
from object.columna import COLUMNA

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
    print("create: ", p[1])
    print("table: ", p[2])
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
    '''columnas : columna COMA columna
                | columna'''
    
    
def p_columna(p):
    '''columna : ID tipo restriccion
              | ID tipo
              | ID tipo tamanios'''
    if p[3] != "":
        print(p[3]) #se crearia el xml con la estructura de una restriccion
        if p[3]=="PRIMARY KEY":
            columna = COLUMNA(p[1],p[2],True,False,"",None, None)
            
    else:
        print("d")

def p_tamanios(p):
    '''tamanios : PARABRE tamanios COMA tamanio PARCIERRA
                | PARABRE tamanio PARCIERRA'''

    
def p_tamanio(p):
    '''tamanio : NUMEROS'''
    p[0] = p[1]
    
def p_restriccion(p):
    '''restriccion : PRIMARY KEY
                   | NOT NULL
                   | references'''
    if len(p)==3:
        p[0] = p[1] + " " + p[2]
    else:
        p[0] = p[1]

def p_references(p):
    '''references : REFERENCES ID PARABRE ID PARCIERRA'''
    p[0]=[
        p[2],
        p[4]]

def p_tipo(p):
    '''tipo : INTEGER
            | TEXT
            | varchar
            | DATE
            | DECIMAL'''
    p[0] = p[1]
    
def p_varchar(p):
    '''varchar : VARCHAR PARABRE NUMEROS PARCIERRA'''
    p[0] = p[3]
import ply.yacc as yacc
parser=yacc.yacc()
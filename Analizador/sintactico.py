from Analizador.lexico import tokens
from object.columna import COLUMNA
from object.reference import REFERENCE
from object.tamanio import TAMANIO
#diccionario de nombres
lista=[]
listaErrores=[]

precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTI', 'DIV'),
    ('nonassoc', 'MAYORQ', 'MENORQ', 'MAYORIGUAL', 'MENORIGUAL', 'IGUAL')
)

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
    '''instruccion : comandocreate
                   | comandoalter
                   | comandotruncate
                   | comandodrop
                   | comandouse
                   | comandoselect
                   | comandoupdate
                   | comandoinsert'''
    p[0] = (p[1])
    

def p_comandocreate(p):
    '''comandocreate : CREATE TABLE exprecionides PARABRE datostable PARCIERRA PYC'''
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
    '''columnas : columnas COMA columna
                | columna'''
    if len(p) == 4:
        p[0]=p[3]
    else:
        p[0] = p[1]
    
def p_columna(p):
    '''columna : exprecionides tipo tamanios
              | exprecionides tipo restriccion
              | exprecionides tipo 
              | exprecionides tipo tamanios restriccion'''
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
    if tipo == "int":
        return 11
    elif tipo == "text":
        return 20
    elif tipo == "date":
        return 11
    elif tipo == "decimal":
        return 5
    elif tipo == "nvarchar":
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
    '''reference : REFERENCE exprecionides PARABRE exprecionides PARCIERRA'''
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


def p_comandoalter(p):
    '''comandoalter : ALTER TABLE exprecionides ADD COLUMN exprecionides tipo PYC
                    | ALTER TABLE exprecionides comandodrop'''
    print("alter " , p[3])


def p_comandotruncate(p):
    '''comandotruncate : TRUNCATE TABLE exprecionides PYC'''
    print("truncate " , p[3])


def p_comandodrop(p):
    '''comandodrop : DROP COLUMN exprecionides PYC
                   | DROP TABLE exprecionides PYC'''
    print("drop ", p[3])

def p_comandouse(p):
    '''comandouse : USE exprecionides PYC'''
    p[0] = p[2]


def p_comandoselect(p):
    '''comandoselect : SELECT valoresselected FROM datosselect PYC
                     | SELECT valoresselected FROM datosselect datoswhere PYC'''
    print("valoresselected " , p[2])
    print("datosselect " , p[4])
    p[0]=""
    
def p_valoresselected(p):
    '''valoresselected : MULTI
                       | datosselect'''
    p[0] = p[1]
    
def p_datosselect(p): #utilizar  isinstance para diferenciar si es una suma o un id
    '''datosselect : datosselect COMA datoselect
                   | datosselect COMA expresion
                   | datoselect
                   | expresion'''
    if len(p) == 4:
        p[0] = str(p[1]) + "," + str(p[3])
    else:
        p[0] = str(p[1])
        
def p_datoselect(p):
    '''datoselect : exprecionides'''
    p[0] = p[1]

def p_datoswhere(p): #oparitmeticas -> expresion
    '''datoswhere : WHERE exprecionides
                  | WHERE expresion
                  | WHERE expresion exprecionides
                  | WHERE exprecionides BETWEEN listasbitween
                  | WHERE exprecionides IGUAL expresion'''
    if len(p)==5:
        p[0] = p[4]
    elif len(p)==4:
        p[0]=p[3]
    else:
        p[0] = p[2]
    print(p[0])
def p_listasbitween(p):
    '''listasbitween : listasbitween listabitween'''
    if p[2] != "":
        p[1].append(p[2])
    p[0] = p[1]

def p_listasbitweenlistabitween(p):
    '''listasbitween : listabitween'''
    if p[1] == "":
        p[0] = []
    else:
        p[0] = [p[1]]

def p_listabitween(p):
    '''listabitween : CADENA
                    | AND
                    | OR
                    | exprecionides PARABRE PARCIERRA
                    | exprecionides IGUAL expresion'''
    if len(p) == 4:
        if p[2] == "(":
            print(p[1])
        elif p[2] =="=":
            print(p[1])
    print(p[1])
    
def p_oparitmeticas(p): #falta ver las producciones de las operaciones aritmeticas
    '''expresion : expresion SUMA termino 
                 | expresion RESTA termino 
                 | termino'''
    #por el momento esta de esta forma, es de enviar los datos y manipularlos desde la otra clase
    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]


def p_termino(p):
    '''termino : termino MULTI factor
               | termino DIV factor
               | factor'''
    if len(p) == 4:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : exprecionides
              | NUMEROS
              | PARABRE expresion PARCIERRA
              | expresion MAYORQ expresion'''
    if len(p) ==4:
        if p[2] == ">":
            p[0] = p[1] > p[2]
        elif p[2] == "<":
            p[0] = p[1] < p[2]
        elif p[2] == ">=":
            p[0] = p[1] >= p[2]
        elif p[2] == "<=":
            p[0] = p[1] <= p[2]
        else:
            p[0] = p[2]
    else:
        p[0] = p[1]

def p_signoscomparacion(p):
    '''signoscomparacion : MAYORQ
                         | MENORQ
                         | MAYORIGUAL
                         | MENORIGUAL'''
    p[0] = p[1]

def p_valordeoperacion(p):
    '''valordeoperacion : exprecionides
                        | NUMEROS
                        | CADENA'''
    p[0] = p[1]
    

def p_comandoupdate(p):
    '''comandoupdate : UPDATE exprecionides SET listaupdate PYC'''
    print("listaupdate " , p[4])

def p_listaupdate(p):
    '''listaupdate : listaupdate COMA valorupdate
                   | valorupdate'''
    if len(p) ==4:
        p[0]=p[3]        
    else:
        p[0] = p[1]

def p_valorupdate(p):
    '''valorupdate : exprecionides IGUAL valordeoperacion
                   | exprecionides IGUAL expresion
                   | exprecionides IGUAL valordeoperacion datoswhere'''
    if len(p) == 5:
        p[0] = p[4]


def p_listaIDES(p):
    '''exprecionides : exprecionides PUNTO ID
                     | ID'''
    if len(p) == 2:
        p[0] = [p[1]]  # Si es solo un ID, devuelve una lista con un elemento
    else:
        p[0] = p[1] + [p[3]]  # Si es una expresión seguida de un ID, concatena la lista con el nuevo ID

def p_comandoinsert(p):
    '''comandoinsert : INSERT INTO exprecionides PARABRE listacolumna PARCIERRA VALUES PARABRE listavalores PARCIERRA PYC'''
    print(p[3])
    print(p[5])
    print(p[9])

def p_listacolumna(p):
    '''listacolumna : exprecionides COMA exprecionides
                    | exprecionides'''
    if len(p) == 4:
        p[0] =p[1] + "," + p[3]
    else:
        p[0] = p[1]

def p_listavalores(p):
    '''listavalores : valordeoperacion COMA valordeoperacion
                    | valordeoperacion'''
    
    if len(p) == 4:
        p[0] =p[1] + "," + p[3]
    else:
        p[0] = p[1]
  
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")   


import ply.yacc as yacc
parser=yacc.yacc()
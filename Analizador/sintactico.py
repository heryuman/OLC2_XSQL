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
                   | comandoinsert
                   | comandodelete
                   | comandoif
                   | comandoset
                   | comandocase'''
    p[0] = p[1]
    

def p_comandocreate(p):
    '''comandocreate : CREATE TABLE exprecionides PARABRE datostable PARCIERRA PYC
                     | CREATE comandoproduce
                     | CREATE DATA BASE exprecionides PYC'''


    
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

    
def p_tamanio(p):
    '''tamanio : NUMEROS'''
    p[0] = p[1]
    
def p_restriccion(p):
    '''restriccion : PRIMARY KEY reference
                   | NOT NULL reference
                   | FOREING KEY reference
                   | PRIMARY KEY
                   | NOT NULL
                   | FOREING KEY
                   | reference'''
    if len(p)==3:
        p[0] = p[1] + " " + p[2]
    elif len(p)==4:
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
            | DATETIME
            | DECIMAL'''
    p[0] = p[1]
    
def p_nvarchar(p):
    '''nvarchar : NVARCHAR PARABRE NUMEROS PARCIERRA'''
    p[0] = p[3]


def p_comandoalter(p):
    '''comandoalter : ALTER TABLE exprecionides ADD COLUMN exprecionides tipo PYC
                    | ALTER TABLE exprecionides comandodrop'''



def p_comandotruncate(p):
    '''comandotruncate : TRUNCATE TABLE exprecionides PYC'''
    p[0] = p[3] #aca es donde se pone la logica del comando truncate


def p_comandodrop(p):
    '''comandodrop : DROP COLUMN exprecionides PYC
                   | DROP TABLE exprecionides PYC'''
    p[0] = p[3]

def p_comandouse(p):
    '''comandouse : USE exprecionides PYC'''
    p[0] = p[2]


def p_comandoselect(p):
    '''comandoselect : SELECT valoresselected FROM datosselect PYC
                     | SELECT valoresselected FROM datosselect  WHERE datoswhere PYC
                     | SELECT comandoif
                     | SELECT comandocase
                     | SELECT funcconcatenar
                     | SELECT SUBSTRAER funcsubstraer
                     | SELECT HOY PARABRE PARCIERRA PYC'''

def p_funcconcatenar(p):
    '''funcconcatenar : CONCATENA PARABRE expresiones_concatenar PARCIERRA PYC'''

def p_expresiones_concatenar(p):
    '''expresiones_concatenar : expresion_concatenar
                             | expresiones_concatenar COMA expresion_concatenar'''

def p_expresion_concatenar(p):
    '''expresion_concatenar : CADENA
                          | CONCATENA PARABRE expresiones_concatenar PARCIERRA'''

def p_funcsubstraer(p):
    '''funcsubstraer : PARABRE CADENA COMA NUMEROS COMA NUMEROS PARCIERRA PYC'''


    
def p_valoresselected(p):
    '''valoresselected : MULTI
                       | datosselect'''
    p[0] = p[1]
    
def p_datosselect(p):
    '''datosselect : datosselect COMA datosselect_item
                   | datosselect_item'''


def p_datosselect_item(p):
    '''datosselect_item : expresion
                       | exprecionides
                       | expresion AS exprecionides
                       | exprecionides AS exprecionides'''


def p_datoswhere(p): #oparitmeticas -> expresion
    '''datoswhere : expresion
                  | exprecionides
                  | exprecionides BETWEEN listasbitween
                  | exprecionides IGUAL expresion
                  | exprecionides IGUAL valordeoperacion
                  | exprecionides IGUAL exprecionides
                  | expresion andor datoswhere
                  | expresion datoswhere datoswhere '''

    
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
                    | andor
                    | exprecionides PARABRE PARCIERRA
                    | exprecionides IGUAL expresion'''
    p[0] = p[1]
    
def p_andor(p):
    '''andor : AND
             | OR
             | VALAND
             | VALOR'''
    p[0] = p[1]
    
    
def p_oparitmeticas(p): #falta ver las producciones de las operaciones aritmeticas
    '''expresion : expresion PLUS termino 
                 | expresion RESTA termino 
                 | termino'''
    #por el momento esta de esta forma, es de enviar los datos y manipularlos desde la otra clase



def p_termino(p):
    '''termino : termino MULTI factor
               | termino DIV factor
               | factor'''


def p_factor(p):
    '''factor : valordeoperacion
              | PARABRE expresion PARCIERRA
              | expresion signoscomparacion expresion'''


def p_signoscomparacion(p):
    '''signoscomparacion : MAYORQ
                         | MENORQ
                         | MAYORIGUAL
                         | MENORIGUAL'''
    p[0] = p[1]

def p_valordeoperacion(p):
    '''valordeoperacion : exprecionides
                        | NUMEROSDECIMALES
                        | NUMEROS
                        | CADENA'''
    p[0] = p[1]
    

def p_comandoupdate(p):
    '''comandoupdate : UPDATE exprecionides SET listaupdate PYC'''


def p_listaupdate(p):
    '''listaupdate : listaupdate COMA valorupdate
                   | valorupdate'''


def p_valorupdate(p):
    '''valorupdate : exprecionides IGUAL valordeoperacion
                   | exprecionides IGUAL expresion
                   | exprecionides IGUAL valordeoperacion WHERE datoswhere'''



def p_listaIDES(p):
    '''exprecionides : exprecionides PUNTO ID
                     | ARROBA ID
                     | ID'''


def p_comandoinsert(p):
    '''comandoinsert : INSERT INTO exprecionides PARABRE listacolumna PARCIERRA VALUES PARABRE listavalores PARCIERRA PYC'''


def p_listacolumna(p):
    '''listacolumna : listacolumna COMA exprecionides
                    | exprecionides'''


def p_listavalores(p):
    '''listavalores : listavalores COMA valordeoperacion
                    | valordeoperacion'''

  

def p_comandodelete(p):
    '''comandodelete : DELETE FROM exprecionides WHERE datoswhere PYC'''

  

def p_comandoif(p):
    '''comandoif : produccionesif comandoelse
                 | exprecionides COMA comandoif
                 | produccionesif
                 | exprecionides'''

def p_produccionesif(p):
    '''produccionesif : IF PARABRE listacentencias PARCIERRA PYC END IF PYC
                      | IF PARABRE listacentencias PARCIERRA AS valordeoperacion FROM exprecionides PYC END IF PYC
                      | IF listacentencia comandothen comandoelse END IF PYC
                      | IF PARABRE listacentencias PARCIERRA PYC 
                      | IF PARABRE listacentencias PARCIERRA AS valordeoperacion FROM exprecionides PYC 
                      | IF listacentencia comandothen'''
                      
def p_comandoelse(p):
    '''comandoelse : ELSE comandothen
                   | ELSE instrucciones
                   | empty'''

def p_empty(p):
    'empty :'
    pass
                   
def p_comandothen (p):
    '''comandothen : THEN instrucciones
                   | THEN valordeoperacion'''
    p[0] = p[2]
    
def p_listacentencias(p):
    '''listacentencias : listacentencias COMA listacentencia
                       | listacentencia'''

def p_listacentencia(p):
    '''listacentencia : valordeoperacion
                      | expresion'''
    p[0] = p[1]
    
    
def p_comandocase(p):
    '''comandocase : produccionescase
                   | exprecionides COMA comandocase
                   | exprecionides'''

def p_produccionescase(p):
    '''produccionescase : CASE listacases FROM exprecionides PYC'''
    
def p_listacases(p):
    '''listacases : listacases listacase'''
    if p[2] != "":
        p[1].append(p[2])
    p[0] = p[1]
    
def p_listacaseslistacase(p):
    '''listacases : listacase'''
    if p[1] == "":
        p[0] = []
    else:
        p[0] = [p[1]]
        
def p_listacase(p):
    '''listacase : WHEN expresion andor expresion comandothen
                 | comandoelse
                 | END expresion'''


def p_comandoproduce(p):
    '''comandoproduce : PROCEDURE parametrosprocedure PARABRE parametrosprocedure PARCIERRA comandoasbegin
                      | PROCEDURE parametrosprocedure comandoasbegin'''

def p_comandoasbegin(p):
    '''comandoasbegin : AS BEGIN listabegin END PYC'''

def p_parametrosprocedure(p):
    '''parametrosprocedure : parametrosprocedure COMA parametroproduce
                           | parametroproduce'''
                           
def p_parametroproduce(p):
    '''parametroproduce : exprecionides AS tipo
                        | exprecionides tipo
                        | exprecionides'''

def p_listabegin(p):
    '''listabegin : listabegin DECLARE parametroproduce PYC
                  | listabegin comandoset
                  | listabegin instrucciones
                  | DECLARE parametroproduce PYC
                  | comandoset
                  | instrucciones'''

def p_comandoset(p):
    '''comandoset : SET listaupdate PYC'''
    
    
def p_error(p):
    if p:
        error_message = f"Error de sintaxis en línea {p.lineno}, posición {p.lexpos}: '{p.value}'"
        print(error_message)

        # Imprimir la línea completa con un indicador de la posición del error
        line_with_error = obtener_linea_con_error(p.lexer.lexdata, p.lineno, p.lexpos)
        print(line_with_error)

def obtener_linea_con_error(lexdata, lineno, lexpos):
    lines = lexdata.split("\n")
    error_line = lines[lineno - 1]
    return f"{error_line}\n{' ' * (lexpos - 1)}^"

import ply.yacc as yacc
parser=yacc.yacc()
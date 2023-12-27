from Analizador.lexico import tokens
from Analizador.lexico import find_column
from object.columna import COLUMNA
from object.reference import REFERENCE
from object.tamanio import TAMANIO
from Instrucciones.CreateTable import CreateTable
from Instrucciones.CreateDB import CreateDB
from Instrucciones.Column import column
from Instrucciones.Reference import Reference
from Instrucciones.Use import Use
from Instrucciones.Insert import Insert
from Instrucciones.Select import Select
#diccionario de nombres
lista=[]
listaErrores=[]
useDB=[]

precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIV'),
    ('left','ANDPERSON','AND_TK','ORPIPE','OR_TK'),
    ('nonassoc', 'MAYQ', 'MENORQ', 'MAYORIGUAL', 'MENORIGUAL', 'IGUAL')
)

def  p_inicio(p):
    '''inicio : instrucciones '''
    p[0] = p[1]
    #for instruccion in p[0]:
     #   if isinstance(instruccion,CreateTable):
           #print("desde inicio create table--->",instruccion.id)
    return p[0]

def p_instrucciones(p):
    '''instrucciones : instrucciones instruccion
                     | instruccion
    '''
    if len(p) ==2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]
        

def p_instrucciones_instruccion(p):
    '''instruccion : cmduse
                     | ddl
                     | dml
                     | declaracion
                     | asignacion_local
                     | asignacion_global
                     | sentencia_if
                     | sentencia_while
                     | sent_return
                     | sentencia_case 
                     | comandoexec
    '''
    
    p[0]=p[1]

def p_cmduse(p):
    '''cmduse : USE ID PYC
    '''
    useDB.append(p[2])
    print("la base ",useDB[0])
    #validar dentro del xml, si la base existe#
    p[0] = Use(p[2], p.lineno(2),1)

def p_ddl(p):
    '''ddl : createdb
           | createtbl
           | createpc
           | createfn
           | alterdb
           | truncatedb
           | doptable
           
    '''
    
    p[0] = p[1]

        #print("**********Estamos imprimiendo el id de tbl*************",p[1])

    
#comando create
def p_createdb(p):
    '''createdb : CREATE DATABASE ID PYC
                | CREATE DATA BASE ID PYC
    '''
    if len(p)== 6:
        p[0]= CreateDB(p[4],p.lineno(2),1)
    else:
        p[0] = CreateDB(p[3],p.lineno(2),1)
    
def p_createtbl(p):
    '''createtbl : CREATE TABLE ID PARA lcolumnas PARC PYC
                 | CREATE TABLE ID PUNTO ID PARA lcolumnas PARC PYC
    '''
    if len(p)==8:
        p[0] = CreateTable(p[3],None,p[5],p.lineno(2),1,False)
        #print("se crea tabla->",p[3])
        #print("con ",len(p[5]),"columnas")
        #for columnas in p[5]:
            #print("colname->",columnas.id," restricciones->",columnas.restriccion)
            
    else:
        p[0] = CreateTable(p[5],p[3],p[7],p.lineno(2),1,False)

    

def p_lcolumnas(p):
    '''lcolumnas : lcolumnas COMA columna atributos_col
                 | lcolumnas COMA columna
                 | columna atributos_col
                 | columna
    '''
    if len(p) == 2:
        p[0] = [p[1]]
        #p[0].append(p[1])
    elif len(p) == 3:
        #col.setAtri(p[2])
        p[1].restriccion =p[2] 
        p[0] = [p[1]]
    elif len(p)==4:
        p[1].append(p[3])
        p[0] = p[1]
    elif len(p) == 5:
        p[3].restriccion = p[4]
        p[1].append(p[3])
        p[0] = p[1]
        ##print("columna ",p[3].id,"restriciones ",p[4])




def p_columna(p):
    '''columna : ID tipo
               | ID tipo PARA expresion PARC
               | ID tipo PARA expresion COMA expresion PARC
    '''
    if len(p) ==3:
        p[0]= column(p[1],p[2],None,"",None,p.lineno(2),3)
    elif len(p) == 6:
        p[0]= column(p[1],p[2],p[4],"",None,p.lineno(2),1)
    else:
        p[0]= column(p[1],p[2],p[4],p[6],None,p.lineno(2),1)


def p_tipo(p):
    '''tipo : INT
            | TEXT
            | NVARCHAR
            | DATE 
            | DATETIME
            | DECIMAL
    '''
    if len(p)==2:
        p[0] = p[1]

def p_atributos_col(p):
    '''atributos_col : atributos_col restriccion
                     | atributos_col reference
                     | restriccion
                     | reference
    '''
    if len(p)==3:
        p[1].append(p[2])
        p[0] = p[1]
    elif len(p)==2:
        p[0] = [p[1]]

def p_restriccion(p):
    '''restriccion : PRIMARY KEY 
                   | FOREING KEY
                   | NOT NULL
                   | NULL
    '''
    if p[1].lower() == "primary":
        p[0] = "PRIMARY KEY"
    elif p[1].lower() == "foreing":
        p[0] = "FOREING KEY"
    elif p[1].lower() == "not":
        p[0] = "NOT NULL"
    elif p[1].lower() == "null":
        p[0] = "NULL"
    
    

def p_reference(p):
    '''reference : REFERENCE ID PARA ID PARC
    '''
    p[0] = Reference(p[2], p[4],p.lineno(2),1)
#declarar una variable 
def p_variable(p):
    '''variable :  ARROBA ID
    '''
def p_declaravar(p):
   ''' declaracion : DECLARE variable tipo PYC
                    | DECLARE ID tipo PYC 
                    | DECLARE variable tipo 
                    | DECLARE ID tipo
                    | DECLARE variable AS tipo 
                    | DECLARE ID AS tipo    
                    | DECLARE variable AS tipo PYC
                    | DECLARE ID AS tipo PYC 
                    
                          
    '''
#asignacion variable 
def p_asigna_local(p):
    '''asignacion_local :  SET variable IGUAL expresion PYC
    '''
def p_asigna_global(p):
    '''asignacion_global : SET expresion PYC
    '''


def p_cmdcreatepc(p):    
    '''
    createpc : CREATE PROCEDURE ID PARA lparams_pc_fn PARC AS BEGIN instrucciones END
             | CREATE PROCEDURE ID PARA lparams_pc_fn PARC AS BEGIN instrucciones END PYC
    '''

def p_cmdcreatefn(p):
    ''' createfn : CREATE FUNCTION  ID PARA lparams_pc_fn PARC RETURNS tipo tamanios AS BEGIN instrucciones END PYC
                 | CREATE FUNCTION  ID PARA lparams_pc_fn PARC RETURNS tipo AS BEGIN instrucciones END PYC
                 | CREATE FUNCTION  ID PARA lparams_pc_fn PARC RETURNS tipo tamanios AS BEGIN instrucciones END
                 | CREATE FUNCTION  ID PARA lparams_pc_fn PARC RETURNS tipo AS BEGIN instrucciones END 
    '''
def p_params_fn_pc(p):
    '''
    lparams_pc_fn : lparams_pc_fn COMA variable tipo
              | lparams_pc_fn COMA variable 
              | lparams_pc_fn COMA variable AS tipo
              | variable AS tipo
              | variable tipo
              | variable
    '''

def p_tamanio(p):
    ''' tamanios : PARA NUMEROS COMA NUMEROS PARC
                 | PARA NUMEROS PARC
    '''
#COMANDOS DML

def p_dml(p):
    '''
     dml : insert
         | select
         | update
         | delete
    '''
    p[0] = p[1]

def p_insert(p):
    '''
    insert : INSERT INTO ID  PARA linsert PARC VALUES PARA linsert PARC PYC
    '''
    p[0] = Insert(p[3],p[5],p[9],p.lineno(2),1)


def p_linsert(p):
    '''
      linsert : linsert COMA expresion
              | expresion
        '''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p)==4:
        p[1].append(p[3])
        p[0] = p[1]

def p_select(p):
    '''
    select : SELECT POR FROM lselect PYC
        | SELECT POR FROM lselect condicion PYC
        | SELECT lselect FROM lselect PYC
        | SELECT lselect FROM lselect condicion PYC
        | SELECT lselect 
        | SELECT lselect PYC
    '''
def p_funciones_procedure(p):
    '''
        funciones_procedure : ID PARA lexpresion PARC
    '''

def p_lids(p):
    '''
    lselect : lselect COMA ID
        | ID
        | lselect COMA ID PUNTO ID
        | ID PUNTO ID
        | lselect variable
        | variable
        | lselect COMA  variable IGUAL expresion
        | variable IGUAL expresion
        | lselect COMA expresion
        | expresion
    '''
    #agregamos estas produccioens lselect COMA expresion
    #    | expresion para esta cadena de entrada
    # SELECT tbcliente.codigocliente,CONCATENA(tbcliente.primer_nombre,tbcliente.primer_apellido)

def p_update(p):
    '''update : UPDATE ID SET lupdate condicion PYC

    '''

def p_lupdate(p):
    '''lupdate : lupdate  COMA expresion  
               | expresion 
    '''

def p_condicion(p):
    '''condicion : WHERE lexpresion
    '''
def p_lexpresion(p):
    '''lexpresion : lexpresion expresion
                  | lexpresion COMA expresion
                  | expresion
                 
                  
    '''
def p_sentencia_if(p):
    '''
    sentencia_if : IF PARA expresion PARC BEGIN instrucciones END PYC
                 | IF PARA expresion PARC BEGIN instrucciones END
                 | IF PARA expresion PARC BEGIN instrucciones END ELSE BEGIN instrucciones END
                 | IF PARA expresion PARC BEGIN instrucciones END PYC ELSE BEGIN instrucciones END PYC
    '''
def p_sentencia_while(p):
    '''
        sentencia_while : WHILE PARA expresion PARC BEGIN instrucciones END PYC
                        | WHILE  expresion BEGIN instrucciones END PYC
                        | WHILE PARA expresion PARC BEGIN instrucciones END 
                        | WHILE  expresion  BEGIN instrucciones END
    '''

def p_sentencia_case(p):
    '''
        sentencia_case : CASE lwhen END PYC
                        | CASE lwhen END
                        | CASE lwhen ELSE THEN instrucciones END PYC
                        | CASE lwhen ELSE THEN instrucciones END
    '''

def p_lwhen(p):
    '''
        lwhen : lwhen WHEN expresion THEN instrucciones 
               | lwhen WHEN PARA expresion PARC THEN instrucciones 
               | WHEN expresion THEN instrucciones 
               | WHEN PARA expresion PARC THEN instrucciones  
    '''

def p_expresion(p):
    '''
     expresion : PARA expresion PARC
              | expresion POR expresion
              | expresion MAS expresion
              | expresion MENOS expresion
              | expresion DIV expresion
              | expresion MENORQ expresion
              | expresion MAYQ expresion
              | expresion MENORIGUAL expresion
              | expresion MAYORIGUAL expresion
              | expresion IGUAL IGUAL expresion
              | expresion AND_TK expresion
              | expresion ANDPERSON expresion
              | expresion OR_TK expresion
              | expresion ORPIPE expresion
              | expresion DIFERENTE expresion
              | NOT_TK expresion
              | TK_FECHA
              | ID
              | NUMEROSDECIMALES
              | NUMEROS
              | CADENA             
              | expresion IGUAL expresion
              | expresion IGUAL variable
              | variable IGUAL expresion
              | operadoressql
              | nativas
              | variable
              | ID PUNTO ID 
              | funciones_procedure
    '''
    if len(p)==2:
        p[0]= p[1]

def p_operadoressql(p):
    '''operadoressql : between
    '''

def p_between(p):
    '''between : BETWEEN expresion 
        '''

def p_nativas(p):
    ''' nativas : sumar
                | concatenar
                | substraer
                | today
                | count
                | cas
    '''

def p_sumar(p):
    ''' sumar : SUMAR PARA expresion PARC
    '''
def p_concatenar(p):
    ''' concatenar : CONCATENA PARA lexpresion PARC
    '''
def p_sustraer(p):
    ''' substraer : SUBSTRAER PARA expresion COMA expresion COMA expresion PARC
    '''
def p_contar(p):
    ''' count : CONTAR PARA POR PARC
              | CONTAR PARA NUMEROS PARC
    '''

def p_hoy(p):
    '''
       today : HOY PARA PARC
    '''
def p_cas (p):
    '''cas : CAS PARA ARROBA ID AS tipo PARC
    '''

def p_return (p):
    '''
        sent_return : RETURNS expresion PYC
                    | RETURNS expresion 
    '''
def p_exec(p):
    '''
        comandoexec : EXEC ID lexpresion
                    | EXEC ID PARA lexpresion PARC
                    | EXEC ID lexpresion PYC
                    | EXEC ID PARA lexpresion PARC PYC
    '''

def p_alterdb(p):
    '''
        alterdb : ALTER TABLE ID addtable
                | ALTER TABLE ID DROP COLUMN ID PYC
    '''
def p_addtable(p):
    '''
        addtable : ADD ID tipo PYC
                 | ADD COLUMN ID tipo PYC
                 | ALTER COLUMN ID ID PYC
    '''

def p_droptable(p):
    '''
        doptable : DROP TABLE ID PYC
    '''

def p_truncatedb(p):
    '''
        truncatedb : TRUNCATE TABLE ID PYC
    '''

def p_delete(p):
    '''
        delete : DELETE FROM ID PYC
               | DELETE FROM ID WHERE expresion PYC
    '''

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")   


import ply.yacc as yacc
parser=yacc.yacc()
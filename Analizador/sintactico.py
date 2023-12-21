from Analizador.lexico import tokens
from object.columna import COLUMNA
from object.reference import REFERENCE
from object.tamanio import TAMANIO
#diccionario de nombres
lista=[]
listaErrores=[]

precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIV'),
    ('left','ANDPERSON','AND_TK','ORPIPE','OR_TK'),
    ('nonassoc', 'MAYQ', 'MENORQ', 'MAYORIGUAL', 'MENORIGUAL', 'IGUAL')
)

def  p_inicio(p):
    '''inicio : instrucciones '''

def p_instrucciones(p):
    '''instrucciones : instrucciones instruccion
                     | instruccion
    '''

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
    '''
    if p[1] == "":
        p[0] = []
    else:
        p[0] = [p[1]]

def p_cmduse(p):
    '''cmduse : USE ID PYC
    '''

def p_ddl(p):
    '''ddl : ddl createdb 
           | ddl createtbl
           | ddl createpc
           | ddl createfn
           | createdb
           | createtbl
           | createpc
           | createfn
    '''
#comando create
def p_createdb(p):
    '''createdb : CREATE DATABASE ID PYC 
    '''
def p_createtbl(p):
    '''createtbl : CREATE TABLE ID PARA lcolumnas PARC PYC
                 | CREATE TABLE ID PUNTO ID PARA lcolumnas PARC PYC
    '''

def p_lcolumnas(p):
    '''lcolumnas : lcolumnas COMA columna atributos_col
                 | lcolumnas COMA columna
                 | columna atributos_col
                 | columna
    '''
def p_columna(p):
    '''columna : ID tipo
               | ID tipo PARA expresion PARC
               | ID tipo PARA expresion COMA expresion PARC
    '''

def p_tipo(p):
    '''tipo : INT
            | TEXT
            | NVARCHAR
            | NVARCHAR tamanios
            | DATE 
            | DATETIME
            | DECIMAL
    '''

def p_atributos_col(p):
    '''atributos_col : atributos_col restriccion
                     | restriccion
                     | reference
    '''

def p_restriccion(p):
    '''restriccion : PRIMARY KEY 
                   | FOREING KEY
                   | NOT NULL
                   | NULL
    '''

def p_reference(p):
    '''reference : REFERENCE ID PARA ID PARC
    '''

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
     dml : dml insert
         | dml select
         | dml update
         | insert
         | select
         | update
    '''

def p_insert(p):
    '''
    insert : INSERT INTO ID  PARA linsert PARC VALUES PARA linsert PARC PYC
    '''
def p_linsert(p):
    '''
      linsert : linsert COMA expresion
              | expresion
        '''

def p_select(p):
    '''
    select : SELECT POR FROM lselect PYC
        | SELECT POR FROM lselect condicion PYC
        | SELECT lselect FROM lselect PYC
        | SELECT lselect FROM lselect condicion PYC
        | SELECT nativas PYC
        | SELECT nativas
        | SELECT expresion 
        | SELECT expresion PYC
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
    '''
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
    '''

def p_lwhen(p):
    '''
        lwhen : lwhen WHEN expresion BEGIN instrucciones 
               | lwhen WHEN PARA expresion PARC BEGIN instrucciones 
               | WHEN expresion BEGIN instrucciones 
               | WHEN PARA expresion PARC BEGIN instrucciones 
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
              | ID
              | NUMEROSDECIMALES
              | NUMEROS
              | CADENA
              | expresion IGUAL expresion
              | expresion IGUAL ARROBA expresion
              | operadoressql
              | nativas
              | ARROBA ID
              | ID PUNTO ID 
    '''
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
    ''' substraer : SUBSTRAER PARA CADENA COMA NUMEROS COMA NUMEROS PARC
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

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")   


import ply.yacc as yacc
parser=yacc.yacc()
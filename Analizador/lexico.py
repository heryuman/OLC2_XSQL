from Arbol.Errores import Errores
ListaErrores=[]
reservadas={

        'create':'CREATE',
        'table':'TABLE',
        'use' : 'USE',
        'primary': 'PRIMARY',
        'key' : 'KEY',
        'foreing':'FOREING',
        'datetime':'DATETIME',
        'nvarchar' : 'NVARCHAR',
        'date': 'DATE',
        'database':'DATABASE',
        'data':'DATA',
        'base': 'BASE',
        'null':'NULL',
        'not':'NOT',
        'reference' : 'REFERENCE',
        'int' : 'INT',
        'text' : 'TEXT',
        'decimal' : 'DECIMAL',
        
        'alter' : 'ALTER',
        'add' : 'ADD',
        'column' : 'COLUMN',
        
        'truncate' : 'TRUNCATE',
        
        'drop' : 'DROP',
        #comienzo la parte de manipulacion de datos
        'select' : 'SELECT',
        'from' : 'FROM',
        'where' : 'WHERE',
        'between':'BETWEEN',
        'and' : 'AND_TK',
        'or' : 'OR_TK',
        
        'update' : 'UPDATE',
        'set' : 'SET',
        
        'insert' : 'INSERT',
        'into' : 'INTO',
        'values' : 'VALUES',  
        'delete' : 'DELETE', 
        'if' : 'IF',
        'as' : 'AS',
        
        'case' : 'CASE',
        'when' : 'WHEN',
        'then' : 'THEN',
        'else' : 'ELSE',
        'end' : 'END',
        'procedure' : 'PROCEDURE',
        'begin' : 'BEGIN',
        'declare' : 'DECLARE',
        'return' : 'RETURNS',
        'concatena' : 'CONCATENA',
        'concat' : 'CONCATENA',
        'concatenar' : 'CONCATENA',
        'substraer' : 'SUBSTRAER',
        'hoy' : 'HOY',
        'contar' : 'CONTAR',
        'sumar' : 'SUMAR',
        'suma' : 'SUMAR',
        'cas' : 'CAS',
        'cast': 'CAS',
        'function': 'FUNCTION',
        'returns': 'RETURNS',
        'while':'WHILE',
        'exec' : 'EXEC'
}


tokens=[
        'ID',
        'NUMEROS',
        'NUMEROSDECIMALES',
        'PARA',
        'PARC',
        'PYC',
        'COMA',
        'MAS',
        'MENOS',
        'POR',
        'DIV',
        'MAYQ',
        'MENORQ',
        'MAYORIGUAL',
        'MENORIGUAL',
        'PUNTO',
        'ANDPERSON',
        'ORPIPE',
        'IGUAL',
        'ARROBA',
        'CADENA',
        'DIFERENTE',
        'TK_FECHA',
        'NOT_TK'
]+list(reservadas.values())

t_ignore=' \t \n \r'

t_PARA = r'\('
t_PARC = r'\)'
t_PYC = r'\;'
t_COMA = r'\,'
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIV = r'/'
t_MAYQ = r'\>'
t_MENORQ = r'\<'
t_MAYORIGUAL = r'\>='
t_MENORIGUAL = r'\<='
t_PUNTO = r'\.'
t_IGUAL = r'='
t_ARROBA = r'\@'
t_ANDPERSON = r'&&'
t_ORPIPE = r'\|\|'
t_NOT_TK= r'\!'
t_DIFERENTE=r'\!\='
def t_NUMEROSDECIMALES(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor flotante demasiado grande: %s" % t.value)
        t.value = 0
    return t

def t_NUMEROS(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero demasiado grande %d", t.value)
        t.value = 0
    return t
#esto es para la parte de los decimales
def t_TK_FECHA(t):
    r'(\'\d{4}-\d{2}-\d{2}\')'
    t.value = t.value[1:-1]
    return t

def t_ID(t):
    r'[a-zA-Z_0-9][a-zA-Z_0-9]*'
    t.type=reservadas.get(t.value.lower(),'ID')
    return t

def t_nuevalinea(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_CADENA(t):
    r'(\'[^\']*\'|\"[^\"]*\")'
    t.value = t.value[1:-1]
    return t




def t_error(t):
    print(f"Error Lexico {t.value!r} en linea : {t.lineno} y columna {t.lexpos+1} ")
    error= Errores(f"Error Lexcico con : {t.value!r} ",1,t.lineno,t.lexpos+1)
    ListaErrores.append(error)
    t.lexer.skip(1)

def find_column(inp, tk):
    line_start = inp.rfind('\n', 0, tk.lexpos) + 1
    return (tk.lexpos - line_start) + 1

import ply.lex as lex
lexer = lex.lex()
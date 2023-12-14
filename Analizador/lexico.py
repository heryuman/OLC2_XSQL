reservadas={

        'create':'CREATE',
        'table':'TABLE',
        'use' : 'USE',
        'primary': 'PRIMARY',
        'key' : 'KEY',
        'nvarchar' : 'NVARCHAR',
        'date': 'DATE',
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
        'and' : 'AND',
        'or' : 'OR',
        
        'update' : 'UPDATE',
        'set' : 'SET',
        
        'insert' : 'INSERT',
        'into' : 'INTO',
        'values' : 'VALUES'
}


tokens=[
        'ID',
        'NUMEROS',
        'NUMEROSDECIMALES',
        'PARABRE',
        'PARCIERRA',
        'PYC',
        'COMA',
        'SUMA',
        'RESTA',
        'MULTI',
        'DIV',
        'MAYORQ',
        'MENORQ',
        'MAYORIGUAL',
        'MENORIGUAL',
        'PUNTO',
        'COMILLASIMPRE',
        'COMILLADOBLE',
        'IGUAL',
        'CADENA'
]+list(reservadas.values())

t_ignore=' \t \n \r'

t_PARABRE = r'\('
t_PARCIERRA = r'\)'
t_PYC = r'\;'
t_COMA = r'\,'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTI = r'\*'
t_DIV = r'/'
t_MAYORQ = r'\>'
t_MENORQ = r'\<'
t_MAYORIGUAL = r'\>='
t_MENORIGUAL = r'\<='
t_PUNTO = r'\.'
t_COMILLASIMPRE = r'\''
t_COMILLADOBLE = r'\"'
t_IGUAL = r'='


def t_NUMEROS(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero demasiado grande %d", t.value)
        t.value = 0
    return t
#esto es para la parte de los decimales
def t_NUMEROSDECIMALES(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor flotante demasiado grande: %s" % t.value)
        t.value = 0
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
    print(f"Error Lexico {t.value!r}")
    t.lexer.skip(1)


import ply.lex as lex
lexer = lex.lex()
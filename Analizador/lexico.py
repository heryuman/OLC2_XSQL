reservadas={

        'create':'CREATE',
        'data' : 'DATA',
        'base' : 'BASE',
        'table':'TABLE',
        'use' : 'USE',
        'primary': 'PRIMARY',
        'foreing' : 'FOREING',
        'key' : 'KEY',
        'nvarchar' : 'NVARCHAR',
        'date': 'DATE',
        'datetime' : 'DATETIME',
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
        
        'return' : 'RETURN',
        'concatena' : 'CONCATENA',
        'substraer' : 'SUBSTRAER',
        'hoy' : 'HOY',
        'contar' : 'CONTAR',
        'suma' : 'SUMA',
        'cas' : 'CAS'
}


tokens=[
        'ID',
        'NUMEROS',
        'NUMEROSDECIMALES',
        'PARABRE',
        'PARCIERRA',
        'PYC',
        'COMA',
        'PLUS',
        'RESTA',
        'MULTI',
        'DIV',
        'MAYORQ',
        'MENORQ',
        'MAYORIGUAL',
        'MENORIGUAL',
        'PUNTO',
        'VALAND',
        'VALOR',
        'IGUAL',
        'DIFEREMTE',
        'IGUALIGUAL',
        'ARROBA',
        'CADENA'
]+list(reservadas.values())

t_ignore=' \t \n \r'

t_PARABRE = r'\('
t_PARCIERRA = r'\)'
t_PYC = r'\;'
t_COMA = r'\,'
t_PLUS = r'\+'
t_RESTA = r'-'
t_MULTI = r'\*'
t_DIV = r'/'
t_MAYORQ = r'\>'
t_MENORQ = r'\<'
t_MAYORIGUAL = r'\>='
t_MENORIGUAL = r'\<='
t_PUNTO = r'\.'
t_IGUAL = r'='
t_ARROBA = r'\@'
t_VALAND = r'&&'
t_VALOR = r'\|\|'
t_IGUALIGUAL = r'=='
t_DIFEREMTE = r'!='
def t_NUMEROSDECIMALES(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError as e:
        print(f"Error: {e} en {t.value}")
        t.value = 0.0
    return t

def t_NUMEROS(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError as e:
        print(f"Error: {e} en {t.value}")
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
    r'(\'[^\']*\')|(\"[^\"]*\")'
    t.value = t.value[1:-1]
    return t




def t_error(t):
    print(f"Error léxico en línea {t.lineno}, posición {t.lexpos}: Carácter inesperado '{t.value[0]}'")
    t.lexer.skip(1)


import ply.lex as lex
lexer = lex.lex()
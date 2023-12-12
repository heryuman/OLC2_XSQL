reservadas={

        'create':'CREATE',
        'table':'TABLE',
        'primary': 'PRIMARY',
        'key' : 'KEY',
        'varchar' : 'VARCHAR',
        'date': 'DATE',
        'null':'NULL',
        'not':'NOT',
        'references' : 'REFERENCES',
        'integer' : 'INTEGER',
        'text' : 'TEXT',
        'decimal' : 'DECIMAL'

}


tokens=[
        'ID',
        'NUMEROS',
        'PARABRE',
        'PARCIERRA',
        'PYC',
        'COMA'
]+list(reservadas.values())

t_ignore=' \t \n \r'

t_PARABRE = r'\('
t_PARCIERRA = r'\)'
t_PYC = r'\;'
t_COMA = r'\,'

def t_NUMEROS(t):
    r"-?\d+"
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type=reservadas.get(t.value.lower(),'ID')
    return t

def t_nuevalinea(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")






def t_error(t):
    print(f"Error Lexico {t.value!r}")
    t.lexer.skip(1)


import ply.lex as lex
lexer = lex.lex()
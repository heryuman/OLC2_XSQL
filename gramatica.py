import ply.yacc as sintactico
import ply.lex as lexico

palabrasReservadas ={"select" : "SELECT",
                     "from": "FROM",
                     "where": "WHERE",
                     "begin": "BEGIN",
                     "end": "END",
                     "declare": "DECLARE",
                     "default":"DEFAULT",
                     "set":"SET",
                     "create": "CREATE",
                     "table": "TABLE",
                     "alter": "ALTER",
                     "add": "ADD",
                     "drop": "DROP",
                     "colum":'COLUMN',
                     "to":'TO', 
                     "insert":'INSERT', 
                     "into":'INTO', 
                     "values":'VALUES', 
                     "update":'UPDATE', 
                     "truncate":'TRUNCATE', 
                     "delate":'DELATE', 
                     "cast":'CAST', 
                     "if":'IF',
                     "else":'ELSE', 
                     "int":'INT', 
                     "then":'THEN', 
                     "print":'PRINT', 
                     "case":'CASE', 
                     "as":'AS', 
                     "break":'BREAK', 
                     "continue":'CONTINUE',
                     "returns":'RETURNS', 
                     "return":'RETURN',
                     "substraer":"SUBSTRAER",
                     "contar":"CONTAR",
                     "foreing":"FOREING",
                     "reference":"REFERENCE",
                     "primary":"PRIMARY",
                     "constrait":"CONSTRAIT",
                     "concatenar":"CONCATENAR"}

tokens = ["IDENTIFICADOR",
          "COMILLAS",
          "STRING",
          "NUMEROS",
          "COMENTARIOS",
          "GUIONMENOR",
          "IGUAL",
          "SUMA",
          "RESTA",
          "MULTIP",
          "DIVISION"]+list(palabrasReservadas.values())

# Definir las expresiones regulares para cada token
t_GUIONBAJO = r"_"   #como solo es un caracter se hace de esta forma
t_IGUAL = r'='
t_COMA = r','
t_ARROBA = r'@'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_PYC = r';'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIP = r'\*'
t_DIVISION = r'/'
t_DIFERENTE = r'!='
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_MENOR = r'<'
t_MAYOR = r'>'
t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'




def t_COMILLAS(t):
    r'\"'
    return t


def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

def t_IDENTIFICADOR(t):
    r"([0-9])*[a-zA-Z_][a-zA-Z0-9_]*"
    #aca se deben de reconocer las palabras reservadas
    return t

#ahora numeros 
def t_NUMEROS(t):
    r"-?\d+"
    return t

t_ignore = " \t\r"

def t_nuevalinea(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print(f'Error Lexico:'+t.value[0]+' en la linea: '+str(t.lineno) +' en la columna: '+str(find_column(input, t)))
    t.lexer.skip(1)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos)+1
    return (token.lexpos - line_start) + 1


#COMIENZA LO SINTACTICO

def p_inicio(t):
    '''inicio : instrucciones'''
    t[0] = t[1]

def p_instrucciones(t):
    '''instrucciones : instrucciones instruccion'''
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]
    
def p_instrucciones_instruccion(t):
    '''instrucciones : instruccion'''
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]
        
def p_instruccion(t):
    '''instruccion : comandocreate'''
    t[0] = t[1]
    
def p_comandocreate(t):
    '''comandocreate : CREATE TABLE IDENTIFICADOR PARIZQ datostabla PARDER PYC'''
    t[0]=""
    
def p_datostabla(t):
    '''datostabla : datostabla datotabla '''
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_datostabla_datotabla(t):
    '''datostabla : datotabla '''
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_datotabla(t):
    '''datotabla : IDENTIFICADOR tipo  '''
    t[0]=""
    

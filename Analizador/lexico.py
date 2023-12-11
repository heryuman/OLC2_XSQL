reservadas={

        'create':'CREATE',
        'type':'TYPE',
        'path':'PATH',
        'name':'NAME',
        'body':'BODY',
        'server':'SERVER',
        'bucket':'BUCKET',
        'delete':'DELETE',
        'copy':'COPY',
        'transfer':'TRANSFER',
        'rename':'RENAME',
        'modify':'MODIFY',
        'backup':'BACKUP',
        'recovery':'RECOVERY',
        'delete_all':'DELETE_ALL',
        'open':'OPEN',
        'from':'FROM',
        'to': 'TO',
        'type_from':'TYPEFROM',
        'type_to':'TYPETO',
        'ip':'IP',
        'port':'PORT'
        

}


tokens=[
        'NOMBRE_ARCHIVO',
        'ID',
        'CHAIN',
        'GUION',
        'MAYQ',
        'DIAG',
        'PUERTONUM',
        'IPNUM'
]+list(reservadas.values())

t_ignore=' \t \n \r'
t_GUION= r'-'
t_MAYQ =r'>'
t_DIAG='/'
t_PUERTONUM = r'\b(?:[1-9]|[1-9][0-9]{1,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])\b'



def t_NOMBRE_ARCHIVO(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z0-9_]+'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type=reservadas.get(t.value.lower(),'ID')
    return t
def t_IPNUM(t):
    r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    return t


'''
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

'''
def t_CHAIN(t):
    r'\".*?\"'
    t.value=t.value[1:-1]
   # print("la cadena es en chain: ",t.value)
    return t




def t_error(t):
    from Operaciones.ManipuladorDeOperaciones import ManipuladorDeOperaciones
    from Operaciones.Log import Log
    print(f"Error Lexico {t.value!r}")
    ahora = ManipuladorDeOperaciones().getDate()
    fecha = ahora.date()
    hora = ahora.time().isoformat()
    log = Log(fecha.day, fecha.month, fecha.year, hora, f"ERROR","Error Lexico en : {t.value}","Sintaxis incorrecta en   "+t.value)
    ManipuladorDeOperaciones().crearLog(log)
    t.lexer.skip(1)


import ply.lex as lex
lexer = lex.lex()
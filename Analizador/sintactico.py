from Analizador.lexico import tokens


#diccionario de nombres
lista=[]
listaErrores=[]
precedence = (
 
    ('right', 'DIAG'),
)


def  p_statement_group(p):
    'INICIO : operaciones'
    #print("ok")
    
def p_operaciones(p):
    ''' operaciones : CREATE mods_create
                    | DELETE mods_delete
                    | COPY mods_copy
                    | TRANSFER mods_copy
                    | RENAME mods_rename
                    | MODIFY mods_modify
                    | BACKUP mods_backup
                    | RECOVERY mods_recovery
                    | DELETE_ALL mods_delete_all
                    | OPEN mods_open
    '''
    
    
    
def p_mods_create(p):
    '''
    mods_create : mod_name 
                | mod_body
                | mod_path
                | mod_type
                | mods_create mod_name 
                | mods_create mod_body
                | mods_create mod_path
                | mods_create mod_type
    '''
    p[0]=p[1]
def p_opciones_nombre(p):
    '''
     opciones_nombre : NOMBRE_ARCHIVO
                    | CHAIN 
    
    '''
    p[0]=p[1]
    
def p_opciones_type(p):
    '''
    opciones_type : SERVER
                  | BUCKET
    '''
    p[0]=p[1]
    
def p_listaMods(p):
    '''
    mod_name : GUION NAME GUION MAYQ opciones_nombre
    
    mod_body : GUION BODY GUION MAYQ CHAIN
    
    mod_path      : GUION PATH      GUION MAYQ opciones_path
                  | GUION PATH      GUION MAYQ path_rename
             
    mod_type      : GUION TYPE      GUION MAYQ opciones_type
    
    mod_from      : GUION FROM      GUION MAYQ opciones_path opciones_nombre
                  | GUION FROM      GUION MAYQ opciones_path
             
    mod_to        : GUION TO        GUION MAYQ opciones_path 
    
    mod_type_to   : GUION TYPETO    GUION MAYQ opciones_type 
    
    mod_type_from : GUION TYPEFROM  GUION MAYQ opciones_type 
    
    mod_ip        : GUION IP        GUION MAYQ IPNUM 
    
    mod_port      : GUION PORT      GUION MAYQ PUERTONUM 
    '''
    if len(p)== 7:
        modif=modificador()
        modif.nombreMod=p[2]
        modif.valorMod=p[5]+p[6]
    else:
        modif=modificador()
        modif.nombreMod=p[2]
        modif.valorMod=p[5]
    #comando.modificadores.append(modif)
    #print(p[2],p[5])
        

def p_mods_delete(p):
    '''
    mods_delete : mod_path
                | mod_name
                | mod_type
                | mods_delete mod_path
                | mods_delete mod_name
                | mods_delete mod_type
    '''
def p_opciones_path(p):
    '''opciones_path : DIAG ID DIAG
                  | DIAG CHAIN DIAG
                  | ID DIAG
                  | CHAIN DIAG
                  | opciones_path  ID DIAG
                  | opciones_path  CHAIN DIAG          
    '''
    if len(p) == 4:
        # Regla: DIAG ID DIAG o DIAG CHAIN DIAG
        p[0] = p[1] +p[2] +p[3]
    elif len(p) == 3:
        # Regla: ID DIAG o CHAIN DIAG
        p[0] = p[1]+p[2]
    else:
        # Regla: opciones_path ID DIAG o opciones_path CHAIN DIAG
        p[0] = p[1]+p[2]+p[3]

def p_path_rename(p):
    '''
     path_rename :  opciones_path opciones_nombre  
    '''
    p[0]=p[1]+p[2]

def p_mods_copy(p):
    '''
    mods_copy : mod_from
             |  mod_to
             |  mod_type_to
             |  mod_type_from
             |  mods_copy mod_from
             |  mods_copy mod_to
             |  mods_copy mod_type_to
             |  mods_copy mod_type_from
    '''
    p[0]=p[1]

def p_mods_rename(p):
    '''
    mods_rename : mod_path
                | mod_name
                | mod_type
                | mods_rename mod_path
                | mods_rename mod_name
                | mods_rename mod_type
    '''
    p[0]=p[1]

def p_mods_modify(p):
    '''
    mods_modify : mod_path
                | mod_body
                | mod_type
                | mods_modify mod_path
                | mods_modify mod_body
                | mods_modify mod_type
    '''

def p_mods_backup(p):
    '''
    mods_backup : mod_type_to
                | mod_type_from
                | mod_ip
                | mod_port
                | mod_name
                | mods_backup mod_type_to
                | mods_backup mod_type_from
                | mods_backup mod_ip
                | mods_backup mod_port
                | mods_backup mod_name
    '''
    p[0]=p[1]

def p_mods_recovery(p):
    '''
    mods_recovery : mod_type_to
                  | mod_type_from
                  | mod_ip
                  | mod_port
                  | mod_name
                  | mods_recovery mod_type_to
                  | mods_recovery mod_type_from
                  | mods_recovery mod_ip
                  | mods_recovery mod_port
                  | mods_recovery mod_name
    '''
    p[0]=p[1]

def p_mods_delete_all(p):
    
    '''
    mods_delete_all : mod_type 
    '''
    p[0]=p[1]

def p_mods_open(p):
    '''
    mods_open : mod_type
              | mod_ip
              | mod_port
              | mod_name
              | mods_open mod_type
              | mods_open mod_ip
              | mods_open mod_port
              | mods_open mod_name
    '''
    p[0]=p[1]

def p_error(p):
    
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    """
        ahora = ManipuladorDeOperaciones().getDate()
        fecha = ahora.date()
        hora = ahora.time().isoformat()
        log = Log(fecha.day, fecha.month, fecha.year, hora, "ERROR","Error al intentar ejecutar el comando: "+comando.nombre_cmd.upper(),"Sintaxis incorrecta en   "+p.value)
        ManipuladorDeOperaciones().crearLog(log)
        pass
    else:
        print("Error de sintaxis al finalizar la entrada")
        ahora = ManipuladorDeOperaciones().getDate()
        fecha = ahora.date()
        hora = ahora.time().isoformat()
        log = Log(fecha.day, fecha.month, fecha.year, hora, "ERROR","Error al intentar ejecutar el comando","Error de sintaxis al finalizar la entrada")
        ManipuladorDeOperaciones().crearLog(log)
        pass
"""
import ply.yacc as yacc
parser=yacc.yacc()
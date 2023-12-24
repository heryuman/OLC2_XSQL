class GENERIC:
    def __init__(self):
        self.algo=None
    
    def centrar_ventana(self,ventana,aplicacion_ancho,aplicacion_largo):
        pantall_ancho = ventana.winfo_screenwidth()
        pantall_largo = ventana.winfo_screenheight()
        x = int((pantall_ancho/2) - (aplicacion_ancho/2))
        y = int((pantall_largo/2) - (aplicacion_largo/2))
        return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")
    
class INSERT:
    def __init__(self,db_name,tb_name,l_into,lvalues):
        self._db_name=db_name #Nombre de la base de datos donde se insertara
        self._tb_name=tb_name #Nombre de la tabla a insertar
        self._lvalues=lvalues  #Lista de valores a insertar
        self._linto=l_into     # Lista de columnas de la tabla 
                              # INSERT INTO (col1,col2,col3)VALUES(val1,val2,val3)
    
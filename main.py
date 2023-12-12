from Front.gui_p import GUI_P
from util.manipulador_xml import CREATE_XML
from util.table import TBL
from util.column import COLUM

creardb=CREATE_XML()
#creardb.create_db("db_test4")

tabla1=TBL("db_test3","my_tab1")
columna1=COLUM("ID","INT",True,None,11)
tabla1.insert_column(columna1)
creardb.insert_table(tabla1)


#GUI_P()
import xml.etree.ElementTree as ET
from xml.dom import minidom

import os
class CREATE_XML:
    
    
    def __init__(self) :
        self._db_name=None
        self._tb_name=None
        self.root=None
        self._colums=[]
    
    """def insert_columns(self,columna:COLUM):
        self._colums.append(columna)
    """
    def create_db(self,db_name):
        #validamos si existe el archivo
        try:
            if  os.path.isfile("dbfile.xml"):
                
                with open("dbfile.xml","r") as f:
                    
                    tree=ET.parse(f)
                root=tree.getroot()
                db=root.findall(".//DATABASE")
                base=root.find("BASES_DE_DATOS")

                if db is not None:
                    for base in db :
                        print("nombre db ",base.get("name_db"))
                        if db_name == base.get("name_db"):
                            print("ERROR!!, la base ya existe, no se puede agregar")
                            return
                self.insert_db(db_name)
        
            else:
                self.root=ET.Element("BASE_DE_DATOS")
                
                #se agrega el nombre de la nueva BD
                new_bd=ET.SubElement(self.root,"BASES")
                new_bd_name=ET.SubElement(new_bd,"DATABASE")
                new_bd_name.attrib["name_db"]=db_name
                new_bd_eschema=ET.SubElement(new_bd_name,"TABLAS")
                new_bd_tables_space=ET.SubElement(new_bd_eschema,"CREATE")
                new_bd_tables_space_I=ET.SubElement(new_bd_eschema,"INSERT")
                new_bd_tables_space.text=" "
                new_bd_tables_space_I.text=" "

                #guardamos el xml
                cadena_xml = ET.tostring(self.root, encoding="utf-8").decode("utf-8")
                xml_con_formato = minidom.parseString(cadena_xml).toprettyxml(indent="  ")

                # Guardar el XML en un archivo
                with open("dbfile.xml", "w", encoding="utf-8") as archivo:
                    archivo.write(xml_con_formato)
        except Exception as e:
            print(e)   


    def insert_db(self,db_name):
        
        if  os.path.isfile("dbfile.xml"):
                
                with open("dbfile.xml","r") as f:
                    
                    tree=ET.parse(f)
                root=tree.getroot()
               
                base=root.find("BASES")
                print("+-+-> ",base)
                new_bd_name=ET.SubElement(base,"DATABASE")
                new_bd_name.attrib["name_db"]=db_name
                new_bd_eschema=ET.SubElement(new_bd_name,"TABLAS")
                new_bd_tables_space=ET.SubElement(new_bd_eschema,"CREATE")
                new_bd_tables_space_I=ET.SubElement(new_bd_eschema,"INSERT")
                new_bd_tables_space.text=" "
                new_bd_tables_space_I.text=" "
                #guardamos el xml
                cadena_xml = ET.tostring(root, encoding="utf-8").decode("utf-8")
                xml_con_formato = minidom.parseString(cadena_xml).toprettyxml(indent="  ")

                # Guardar el XML en un archivo
                with open("dbfile.xml", "w", encoding="utf-8") as archivo:
                    archivo.write(xml_con_formato)
    
    def insert_table(self,table):
        db_name=table.get_db_name()
        tb_name=table.get_tb_name()
        with open("dbfile.xml","r") as f:        
                tree=ET.parse(f)
        root=tree.getroot()
        n_db=root.find(".//DATABASE[@name_db='"+db_name+"']")
        if n_db is not None:
              
            n_create=n_db.find("./TABLAS/CREATE")
            n_tb= ET.SubElement(n_create,"TABLA")
            n_tb.attrib["tab_name"]=tb_name
            colums=ET.SubElement(n_tb,"COLUMNAS")
            for col in table._columns:
                nc=col._column_name
                nt=col._type
                #cz=col._col_size
                n_col=ET.SubElement(colums,"COLUMNA")
                n_col.attrib["nombrecol"]=nc
                n_col.attrib["tipo"]=nt
                #n_col.attrib["col_size"]=str(cz)
            cadena_xml = ET.tostring(root, encoding="utf-8").decode("utf-8")
            xml_con_formato = minidom.parseString(cadena_xml).toprettyxml(indent="  ")
            # Guardar el XML en un archivo
            with open("dbfile.xml", "w", encoding="utf-8") as archivo:
                    archivo.write(xml_con_formato)
        else:
            print("no existe la BD"+ db_name)
                # Guardar el XML en un archivo
            with open("dbfile.xml", "w", encoding="utf-8") as archivo:
                archivo.write(xml_con_formato)
#METODOS QUE VALIDAN SI EXISTE LA TABLA O LA BD
    def exist_table(self,db_name,tb_name):
        with open("dbfile.xml","r") as f:        
                tree=ET.parse(f)
        root=tree.getroot()
        db=root.find(".//DATABASE[@name_db='"+db_name+"']")
        
        if db is not None:
            print("existe la BD",db.get("name_db"))
            tb=root.find(".//DATABASE//TABLAS//CREATE//TABLA[@tab_name='"+tb_name+"']")
            if tb is not None:
                 print("Existe la tb ",tb.get("tab_name"))
                 return True
            return False
        return False
    
    def exist_db(self,db_name):
         with open("dbfile.xml","r") as f:        
                tree=ET.parse(f)
         root=tree.getroot()
         db=root.find(".//DATABASE[@name_db='"+db_name+"']")
        
         if db is not None:
            print("existe la BD",db.get("name_db"))
            return True
         return False
#FINALIZAN METODOS QUE VALIDAN SI EXISTE LA TABLA O LA BD

                    




    

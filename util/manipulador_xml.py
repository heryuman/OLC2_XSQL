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
                #base=root.find("BASES_DE_DATOS")

                if db is not None:
                    for base in db :
                        print("nombre db ",base.get("name_db"))
                        if db_name.lower() == base.get("name_db").lower():
                            print("ERROR!!, la base ya existe, no se puede agregar")
                            return
                self.insert_db(db_name)
        
            else:
                self.root=ET.Element("BASE_DE_DATOS")
                
                #se agrega el nombre de la nueva BD
                new_bd=ET.SubElement(self.root,"BASES")
                new_bd_name=ET.SubElement(new_bd,"DATABASE")
                new_bd_name.attrib["name_db"]=db_name.lower()
                new_bd_eschema=ET.SubElement(new_bd_name,"TABLAS")
                #new_bd_tables_space=ET.SubElement(new_bd_eschema,"CREATE")
                #new_bd_tables_space_I=ET.SubElement(new_bd_eschema,"INSERT")
                #new_bd_tables_space.text=" "
                #new_bd_tables_space_I.text=" "

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
                new_bd_name.attrib["name_db"]=db_name.lower()
                new_bd_eschema=ET.SubElement(new_bd_name,"TABLAS")
                #new_bd_tables_space=ET.SubElement(new_bd_eschema,"CREATE")
                #new_bd_tables_space_I=ET.SubElement(new_bd_eschema,"INSERT")
                #new_bd_tables_space.text=" "
                #new_bd_tables_space_I.text=" "
                #guardamos el xml
                cadena_xml = ET.tostring(root, encoding="utf-8").decode("utf-8")
                xml_con_formato = minidom.parseString(cadena_xml).toprettyxml(indent="  ")

                # Guardar el XML en un archivo
                with open("dbfile.xml", "w", encoding="utf-8") as archivo:
                    archivo.write(xml_con_formato)
    
    def insert_table(self,table):
        db_name=table.get_db_name().lower()
        tb_name=table.get_tb_name().lower()
        with open("dbfile.xml","r") as f:        
                tree=ET.parse(f)
        root=tree.getroot()
        n_db=root.find(".//DATABASE[@name_db='"+db_name+"']")
        if n_db is not None:
              
            n_create=n_db.find("./TABLAS")
            n_tb= ET.SubElement(n_create,"TABLA")
            n_tb.attrib["tab_name"]=tb_name
            tab_space_create=ET.SubElement(n_tb,"CREATE")
            tab_space_insert=ET.SubElement(n_tb,"INSERT")

            colums=ET.SubElement(tab_space_create,"COLUMNAS")
            cols_i=ET.SubElement(tab_space_insert,"COLUMNAS")
            for col in table._columns:
                nc=col._column_name
                nt=col._type
                cpk=col._pk
                cisnull=col._isNull
                cval=col._valor
                cz=col._col_size
                cpresicion=col._presicion
                crefer=col._col_fer
                tbrefe=col._tab_refernce

                n_col=ET.SubElement(colums,"COLUMNA")
                n_col.attrib["nombrecol"]=nc
                n_col.attrib["tipo"]=nt
                n_col.attrib["pk"]=str(cpk)
                n_col.attrib["isNull"]=str(cisnull)
                n_col.attrib["valor"]=str(cval)
                n_col.attrib["col_size"]=str(cz)
                n_col.attrib["presicion"]=str(cpresicion)
                n_col.attrib["col_ref"]=crefer
                n_col.attrib["tab_ref"]=tbrefe
            cadena_xml = ET.tostring(root, encoding="utf-8").decode("utf-8")
            xml_con_formato = minidom.parseString(cadena_xml).toprettyxml(indent="")
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
        db=root.find(".//DATABASE[@name_db='"+db_name.lower()+"']")
        
        if db is not None:
            print("existe la BD",db.get("name_db"))
            tb=root.find(".//DATABASE//TABLAS//TABLA[@tab_name='"+tb_name.lower()+"']")
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

#Area Selvin
#Metodo insert
    def insert_ontbl(self,obj_insert):
        l_into=obj_insert._linto
        l_values=obj_insert._lvalues
        db_name=obj_insert._db_name
        tb_name=obj_insert._tb_name
        with open("dbfile.xml","r")as f:
              tree=ET.parse(f)
        root=tree.getroot()

        db=root.find(".//DATABASE[@name_db='"+db_name.lower()+"']")
        
        if db is not None:
            print("existe la BD",db.get("name_db"))
            tb=root.find(".//DATABASE//TABLAS//TABLA[@tab_name='"+tb_name.lower()+"']")
            if tb is not None:
                cols_into=tb.findall(".//CREATE//COLUMNAS//COLUMNA")
                #for columna in cols_into:
                #     print("columna : ",columna.get("nombrecol"))
                #print("linto",len(l_into),l_into)
                #print("cols_into",len(cols_into),cols_into)
                tab_insert=tb.find(".//INSERT//COLUMNAS")
                cols_insert=ET.SubElement(tab_insert,"COLUMNAS")
                
                atri=[]
                for atr in cols_into:
                    atri.append(atr.attrib) 
                if len(l_into)==len(cols_into):
                    for i in range(0,len(l_into)):
                       if atri[i]["nombrecol"].lower()==l_into[i].lower():
                            if self.compare_type(l_values[i],atri[i]["tipo"].lower()):
                                 print(l_values[i])
                                 col_insert=ET.SubElement(cols_insert,"COLUMNA")
                                 col_insert.attrib["nombrecol"]=atri[i]["nombrecol"]
                                 col_insert.attrib["tipo"]=atri[i]["tipo"]
                                 col_insert.attrib["pk"]=atri[i]["pk"]
                                 col_insert.attrib["isNull"]=atri[i]["isNull"]
                                 col_insert.attrib["valor"]=str(l_values[i])
                                 col_insert.attrib["col_size"]=atri[i]["col_size"]
                                 col_insert.attrib["presicion"]=atri[i]["presicion"]
                                 col_insert.attrib["col_ref"]=atri[i]["col_ref"]
                                 col_insert.attrib["tab_ref"]=atri[i]["tab_ref"]
                                 cadena_xml = ET.tostring(root, encoding="utf-8").decode("utf-8")
                                 xml_con_formato = minidom.parseString(cadena_xml).toprettyxml(indent="")
                                 # Guardar el XML en un archivo
                                 with open("dbfile.xml", "w", encoding="utf-8") as archivo:
                                        archivo.write(xml_con_formato)
                            else:
                                 print("ERROR!!,tipo de datos Incorrecto")
                else:
                     print("Error!!,no coinciden la lista de parametros de la tabla")
            else:
                 print("ERROR!!,La tabla ",tb_name," no existe")
        else:
            print("ERROR!!,La Base ",db_name," no existe")
                
    def compare_type(self,valor,tipo):
         if type(valor)==int:
              if tipo =="int":
                   return True
              elif tipo=="nvarchar":
                   return True
              else:
                   False
         elif type(valor)==str:
              if tipo =="cadena":
                return True
              elif tipo =="nvarchar":
                   return True
              elif tipo == "date":
                  return True
              elif tipo =="datetime":
                  return True
              else:
                   False
         elif type(valor)== float:
              if tipo =="decimal":
                   return True
              else:
                   False
         else:
              False 
    
    def select(self):
        print("")
       
               
#Area Cutzal



    

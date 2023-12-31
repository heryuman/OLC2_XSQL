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
    def create_db(self,db_name,output):
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
                            output.append("ERROR!!, la base ya existe, no se puede agregar")
                            return
                self.insert_db(db_name,output)
        
            else:
                self.root=ET.Element("BASE_DE_DATOS")
                
                #se agrega el nombre de la nueva BD
                new_bd=ET.SubElement(self.root,"BASES")
                new_bd_name=ET.SubElement(new_bd,"DATABASE")
                new_bd_name.attrib["name_db"]=db_name
                new_bd_eschema=ET.SubElement(new_bd_name,"TABLAS")

                #guardamos el xml
                cadena_xml = ET.tostring(self.root, encoding="utf-8").decode("utf-8")
                xml_con_formato = minidom.parseString(cadena_xml).toprettyxml(indent="  ")

                # Guardar el XML en un archivo
                with open("dbfile.xml", "w", encoding="utf-8") as archivo:
                    archivo.write(xml_con_formato)
        except Exception as e:
            print(e)   
            output.append(f"Error con: {e}")


    def insert_db(self,db_name,output):
        
        if  os.path.isfile("dbfile.xml"):
                
                with open("dbfile.xml","r") as f:
                    
                    tree=ET.parse(f)
                root=tree.getroot()
               
                base=root.find("BASES")
                print("+-+-> ",base)
                new_bd_name=ET.SubElement(base,"DATABASE")
                new_bd_name.attrib["name_db"]=db_name
                new_bd_eschema=ET.SubElement(new_bd_name,"TABLAS")
                #guardamos el xml
                cadena_xml = ET.tostring(root, encoding="utf-8").decode("utf-8")
                xml_con_formato = minidom.parseString(cadena_xml).toprettyxml(indent="  ")

                # Guardar el XML en un archivo
                with open("dbfile.xml", "w", encoding="utf-8") as archivo:
                    archivo.write(xml_con_formato)
        else:
            output.append("ERROR!!,no existe un archivo de BD")
    
    def insert_table(self,table,output):
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
            create=ET.SubElement(n_tb,"CREATE")
            insert=ET.SubElement(n_tb,"INSERT")
            colums=ET.SubElement(create,"COLUMNAS")
            col_i=ET.SubElement(insert,"COLUMNAS")
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
            xml_con_formato = minidom.parseString(cadena_xml).toprettyxml(indent="  ")
            # Guardar el XML en un archivo
            with open("dbfile.xml", "w", encoding="utf-8") as archivo:
                    archivo.write(xml_con_formato)
        else:
            print("no existe la BD"+ db_name)
            output.append(f"Error, no existe la BD: {db_name}")
                # Guardar el XML en un archivo
            #with open("dbfile.xml", "w", encoding="utf-8") as archivo:
            #    archivo.write(xml_con_formato)
#METODOS QUE VALIDAN SI EXISTE LA TABLA O LA BD
    def exist_table(self,db_name,tb_name):
        with open("dbfile.xml","r") as f:        
                tree=ET.parse(f)
        root=tree.getroot()
        db=root.find(".//DATABASE[@name_db='"+db_name+"']")
        
        if db is not None:
            print("existe la BD",db.get("name_db"))
            tb=root.find(".//DATABASE//TABLAS//TABLA[@tab_name='"+tb_name+"']")
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
    def insert_ontbl(self,obj_insert,output):
        l_into=obj_insert._linto
        l_values=obj_insert._lvalues
        db_name=obj_insert._db_name
        tb_name=obj_insert._tb_name
        with open("dbfile.xml","r")as f:
              tree=ET.parse(f)
        root=tree.getroot()

        db=root.find(".//DATABASE[@name_db='"+db_name.lower()+"']")
        
        if db is not None:
            print("-->existe la BD",db.get("name_db"))
            tb=root.find(".//DATABASE//TABLAS//TABLA[@tab_name='"+tb_name.lower()+"']")
            if tb is not None:
                cols_into=tb.findall(".//CREATE//COLUMNAS//COLUMNA")
                #for columna in cols_into:
                #     print("columna : ",columna.get("nombrecol"))
                #print("linto",len(l_into),l_into)
                #print("cols_into",len(cols_into),cols_into)
                tab_insert=tb.find(".//INSERT//COLUMNAS")
                #cols_insert=ET.SubElement(tab_insert,"COLUMNA")
                
                atri=[]
                colNulls=[]
                for atr in cols_into:
                    atri.append(atr.attrib) 
                print("tamaño inicial de atri", len(atri))
                for colum in atri:
                    if colum["nombrecol"] in l_into:
                        print("existe la colummna",colum["nombrecol"])
                    else:
                        print("No existe la colummna",colum["nombrecol"])
                        print("Pero es Null ",colum["isNull"])
                        colNulls.append(colum)
                        atri.remove(colum)
                print("el nuevo tamañao de atri", len(atri))
                
                
                if len(l_into)==len(atri):
                    for i in range(0,len(l_into)):
                       if atri[i]["nombrecol"].lower()==l_into[i].lower():
                            if self.compare_type(l_values[i],atri[i]["tipo"].lower()):
                                 print(l_values[i])
                                 col_insert=ET.SubElement(tab_insert,"COLUMNA")
                                 col_insert.attrib["nombrecol"]=atri[i]["nombrecol"]
                                 col_insert.attrib["tipo"]=atri[i]["tipo"]
                                 col_insert.attrib["pk"]=atri[i]["pk"]
                                 col_insert.attrib["isNull"]=atri[i]["isNull"]
                                 col_insert.attrib["valor"]=str(l_values[i])
                                 col_insert.attrib["col_size"]=atri[i]["col_size"]
                                 col_insert.attrib["presicion"]=atri[i]["presicion"]
                                 col_insert.attrib["col_ref"]=atri[i]["col_ref"]
                                 col_insert.attrib["tab_ref"]=atri[i]["tab_ref"]
                                 
                            else:
                                 print("ERROR!!,tipo de datos Incorrecto")
                                 output.append("ERROR!!,tipo de datos Incorrecto")
                    if len(colNulls)>0:
                        for colnull in colNulls:
                            col_insert=ET.SubElement(tab_insert,"COLUMNA")
                            col_insert.attrib["nombrecol"]=colnull["nombrecol"]
                            col_insert.attrib["tipo"]=colnull["tipo"]
                            col_insert.attrib["pk"]=colnull["pk"]
                            col_insert.attrib["isNull"]=colnull["isNull"]
                            col_insert.attrib["valor"]="null"
                            col_insert.attrib["col_size"]=colnull["col_size"]
                            col_insert.attrib["presicion"]=colnull["presicion"]
                            col_insert.attrib["col_ref"]=colnull["col_ref"]
                            col_insert.attrib["tab_ref"]=colnull["tab_ref"]
                    cadena_xml = ET.tostring(root, encoding="utf-8").decode("utf-8")
                    xml_con_formato = minidom.parseString(cadena_xml).toprettyxml(indent="")
                                 # Guardar el XML en un archivo
                    with open("dbfile.xml", "w", encoding="utf-8") as archivo:
                                        archivo.write(xml_con_formato)        
                        
                else:
                     print("Error!!,no coinciden la lista de parametros de la tabla")
                     output.append("Error!!,no coinciden la lista de parametros de la tabla")
            else:
                 print("ERROR!!,La tabla ",tb_name," no existe")
                 output.append("ERROR!!,La tabla ",tb_name," no existe")
        else:
            print("ERROR!!,La Base ",db_name," no existe")
            output.append("ERROR!!,La Base ",db_name," no existe")
                
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
    
    def select(self,obj_select):
        select_all=obj_select._SelectAll
        db_name=obj_select._db_name
        ltb=obj_select._l_tbname
        lcond=obj_select._lcondiciones
        
        if select_all:
            self.select_all(db_name,ltb)
    
    
    def select_all(self,db_name,ltb,output):
        
        if self.exist_db(db_name):
            with open("dbfile.xml","r")as f:
              tree=ET.parse(f)
            root=tree.getroot()

            db=root.find(".//DATABASE[@name_db='"+db_name.lower()+"']")
            if db is not None:
                for tabla in ltb:
                    tb=root.find(".//DATABASE//TABLAS//TABLA[@tab_name='"+tabla.lower()+"']")
                    if tb is not None:
                        colselect=tb.findall(".//INSERT//COLUMNAS//COLUMNA")
                        for i in range(0,len(colselect)):
                            print(colselect[i].get("nombrecol")," : ", colselect[i].get("valor"))
                            
                        #print(colselect["nombrecol"]," -- ")
                    
            else:
                print(f'Error, la DB {db_name} no existe')
                output.append(f'Error, la DB {db_name} no existe')
            
        
        
        
       
               
#Area Cutzal
                   



    def xml_gui(nombre_archivo): #esta funcion es para mostrar el xml como un arbol en la parte del GUI
        #nombre_archivo = 'dbfile.xml' #nombre del archivo
        if os.path.exists(nombre_archivo): #verificamos si el archivo existe
            tree = ET.parse(nombre_archivo)
            root = tree.getroot()
            #utilizamos variables para guardar los valores que vienen del archivo
            databases = []
            
            #reconocemos los valores del xml
            #aun no reconoce lo de procedimientos y funciones
            for database in root.findall('.//DATABASE'):
                database_name = database.get('name_db')
                tabla_names = []
                for tabla in database.findall('.//TABLA'):
                    tabla_name = tabla.get('tab_name')
                    tabla_names.append(tabla_name)
                databases.append((database_name, tabla_names))
            return databases
        else:
            return []
            
    
    def delete_db(self, db_name):
        try:
            if os.path.isfile("dbfile.xml"):
                with open("dbfile.xml", "r") as f:
                    tree = ET.parse(f)
                root = tree.getroot()
                bases = root.find(".//BASES")
                if bases is not None:
                    elements_to_remove = []
                    for base_elem in bases.findall("DATABASE"):
                        if db_name == base_elem.get("name_db"):
                            elements_to_remove.append(base_elem)
                    if not elements_to_remove:
                        self.mensajeError("Error", "La base no existe, no se puede eliminar")
                        return
                    for elem in elements_to_remove:
                        bases.remove(elem)
                    #se guarda el xml actualizado
                    cadena_xml = ET.tostring(root, encoding="utf-8").decode("utf-8")
                    xml_con_formato = minidom.parseString(cadena_xml).toprettyxml(indent="  ")
                    with open("dbfile.xml", "w", encoding="utf-8") as archivo:
                        archivo.write(xml_con_formato)
                else:
                    self.mensajeError("Error", "No hay bases de datos para eliminar")
                    return
            else:
                self.mensajeError("Error", "El archivo de base de datos no existe")
        except Exception as e:
            print(e)

    
    #def mensajeError(self, tituloVentana, mensaje):
        #root = tk.Tk()
        #root.withdraw()
        #messagebox.showerror(tituloVentana, mensaje)
        #root.destroy()
        
    def createDump(self,db_name):
        try:
            if  os.path.isfile(db_name+".xml"):
                with open(db_name+".xml","r") as f:
                    tree=ET.parse(f)
                root=tree.getroot()
                db=root.findall(".//DATABASE")
                base=root.find("BASES_DE_DATOS")
                if db is not None:
                    for base in db :
                        print("nombre db ",base.get("name_db"))
                        if db_name == base.get("name_db"):
                            self.mensajeError("ERROR!!, la base ya existe, no se puede agregar")
                            return
                self.insert_db2(db_name)
            else:
                self.root=ET.Element("BASE_DE_DATOS")
                #se agrega el nombre de la nueva BD
                new_bd=ET.SubElement(self.root,"BASES")
                new_bd_name=ET.SubElement(new_bd,"DATABASE")
                new_bd_name.attrib["name_db"]=db_name
                new_bd_eschema=ET.SubElement(new_bd_name,"TABLAS")
                new_bd_eschema=ET.SubElement(new_bd_name,"FUNCIONES")
                new_bd_eschema=ET.SubElement(new_bd_name,"PROCEDIMIENTOS")
                new_bd_eschema.text=" "
                #guardamos el xml
                cadena_xml = ET.tostring(self.root, encoding="utf-8").decode("utf-8")
                xml_con_formato = minidom.parseString(cadena_xml).toprettyxml(indent="  ")
                with open(db_name+".xml", "w", encoding="utf-8") as archivo:
                    archivo.write(xml_con_formato)
        except Exception as e:
            print(e)
    
    
    def insert_db2(self,db_name):
        if  os.path.isfile(db_name+".xml"):
                with open(db_name+".xml","r") as f:
                    tree=ET.parse(f)
                root=tree.getroot()
                base=root.find("BASES")
                print("+-+-> ",base)
                new_bd_name=ET.SubElement(base,"DATABASE")
                new_bd_name.attrib["name_db"]=db_name
                new_bd_eschema=ET.SubElement(new_bd_name,"TABLAS")
                new_bd_eschema=ET.SubElement(new_bd_name,"FUNCIONES")
                new_bd_eschema=ET.SubElement(new_bd_name,"PROCEDIMIENTOS")
                new_bd_eschema.text=" "
                cadena_xml = ET.tostring(root, encoding="utf-8").decode("utf-8")
                xml_con_formato = minidom.parseString(cadena_xml).toprettyxml(indent="  ")
                with open(db_name+".xml", "w", encoding="utf-8") as archivo:
                    archivo.write(xml_con_formato)
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
import tkinter as tk
from tkinter import messagebox
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
                            self.mensajeError("ERROR!!, la base ya existe, no se puede agregar")
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

#Area Selvin

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

    
    def mensajeError(self, tituloVentana, mensaje):
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(tituloVentana, mensaje)
        root.destroy()
        
    def createDump(self, db_name):
        try:
            dbfile_path = "dbfile.xml"

            if not os.path.isfile(dbfile_path):
                self.mensajeError("ERROR!!, el archivo 'dbfile.xml' no existe")
                return

            tree = ET.parse(dbfile_path)
            root = tree.getroot()
            databases = root.findall(".//DATABASE")
            if databases is not None:
                for database in databases:
                    if db_name == database.get("name_db"):
                        self.insert_db2(db_name, root)
                        return

                self.mensajeError(f"ERROR!!, la base '{db_name}' no existe en 'dbfile.xml'")
            else:
                self.mensajeError("ERROR!!, no hay bases de datos en 'dbfile.xml'")
        except Exception as e:
            print(e)

    def insert_db2(self, db_name, root):
        original_database = root.find(f".//DATABASE[@name_db='{db_name}']")
        if original_database is None:
            self.mensajeError(f"ERROR!!, la base '{db_name}' no existe")
            return

        existing_database = root.find(f".//DATABASE[@name_db='{db_name}_DUMP']")
        if existing_database is not None:
            self.mensajeError(f"ERROR!!, la base '{db_name}_DUMP' ya existe")
            return

        new_base_datos = ET.Element("BASE_DE_DATOS")
        new_bases = ET.SubElement(new_base_datos, "BASES")

        new_database = ET.SubElement(new_bases, "DATABASE")
        new_database.attrib["name_db"] = f"{db_name}_DUMP"

        # Copiar estructura de tablas
        original_tables = original_database.find("TABLAS")
        if original_tables is not None:
            new_tables = ET.SubElement(new_database, "TABLAS")
            for original_table in original_tables.findall("TABLA"):
                new_table = ET.SubElement(new_tables, "TABLA", attrib={"tab_name": original_table.get("tab_name")})
                create_element = original_table.find("CREATE")
                if create_element is not None:
                    new_create = ET.SubElement(new_table, "CREATE")
                    self.copy_element(create_element, new_create)

        # Copiar FUNCIONES
        original_functions = original_database.find("FUNCIONES")
        if original_functions is not None:
            new_functions = ET.SubElement(new_database, "FUNCIONES")
            for original_function in original_functions.findall("FUNCION"):
                new_function = ET.SubElement(new_functions, "FUNCION", attrib=original_function.attrib)
                create_element = original_function.find("CREATE")
                if create_element is not None:
                    new_create = ET.SubElement(new_function, "CREATE")
                    self.copy_element(create_element, new_create)

        # Copiar PROCEDIMIENTOS
        original_procedures = original_database.find("PROCEDIMIENTOS")
        if original_procedures is not None:
            new_procedures = ET.SubElement(new_database, "PROCEDIMIENTOS")
            for original_procedure in original_procedures.findall("PROCEDIMIENTO"):
                new_procedure = ET.SubElement(new_procedures, "PROCEDIMIENTO", attrib=original_procedure.attrib)
                create_element = original_procedure.find("CREATE")
                if create_element is not None:
                    new_create = ET.SubElement(new_procedure, "CREATE")
                    self.copy_element(create_element, new_create)

        cadena_xml = ET.tostring(new_base_datos, encoding="utf-8").decode("utf-8")
        xml_con_formato = minidom.parseString(cadena_xml).toprettyxml(indent="  ")
        with open(f"{db_name}_DUMP.xml", "w", encoding="utf-8") as archivo:
            archivo.write(xml_con_formato)

    def copy_element(self, original, new_element):
        for original_column in original.findall("*"):
            new_create_column = ET.SubElement(new_element, original_column.tag, attrib=original_column.attrib)
            for inner_column in original_column.findall("*"):
                new_inner_column = ET.SubElement(new_create_column, inner_column.tag, attrib=inner_column.attrib)
                if inner_column.text:
                    new_inner_column.text = inner_column.text

    def mensajeError(self, mensaje):
        print("Error:", mensaje)
import tkinter as tk
from tkinter import ttk
from util.generic import GENERIC
from Analizador.sintactico import parse as Analizar
from Analizador.sintactico import useDB
from Simbolo.Ambito import Ambito
from Simbolo.Simbolo import Simbolo
from Abstract.Instruccion import Instruccion
from Arbol.AST import AST
from util.manipulador_xml import CREATE_XML
from tkinter import filedialog
from tkinter import messagebox
import subprocess
from tkinter import simpledialog
import os
from enviroment import enviroment
from Arbol.Arbol import Arbol
from Arbol.Nodo import Nodo

class GUI_P:
    _instances = [] #esta instancia permite hacer lo de cerrar una pestaña y luego poder abrir y que si se carge el contenido del archivo
    def __init__(self) :
        self.contador_pestanas = 0

        self.tablaSimbolos = Ambito(None)
        self.tablaSimbolos.addSimbolo(self.getFirstSimbolo())

        self.notebook=None
        self.mat_text=[]
        self.mat_consola = []
        utl= GENERIC()
        self.ventana=tk.Tk()
        self.archivo_guardado = None  # Variable para almacenar la ruta del archivo guardado
        self.ventana.title('SQLX')
        self.ventana.config(bg='#ffffff')
        #self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,800,500)
        #frame treeview
        frame_treeview= tk.Frame(self.ventana, bd=0, width=15, relief=tk.SOLID, padx=10, pady=10, bg='#3a7fff')
        frame_treeview.pack(side='left', fill=tk.BOTH)
        self.tree = ttk.Treeview(frame_treeview, height=100)
        #self.tree.pack(side="left")
        
        
        self.ventana.after(20000, self.reload_data)       
        
       # tree.place(x=0,y=0,relwidth=1,relheight=1)
        self.tree.pack(side="left")

        #frame_menus
        frame_menus = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#3a7fff',padx=10,pady=10)
        frame_menus.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        
        #frame_botones
        frame_botones = tk.Frame(frame_menus,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_botones.pack(side="top",fill=tk.X)
        #botones
        btn_archivo= tk.Menubutton(frame_botones,text="Archivo")
        archivo_ops=tk.Menu(btn_archivo)
        archivo_ops.add_command(label="Abrir", command=self.abrir_archivo)
        archivo_ops.add_command(label="Guardar")
        archivo_ops.add_command(label="Guardar Como" , command=self.guardar_como_archivo)
        archivo_ops.add_command(label="Cerrar", command=self.cerrar_pestana_actual)
        archivo_ops.add_command(label="Salir", command=self.salir_programa)
        btn_archivo.config(menu=archivo_ops)
        btn_archivo.pack(side="left",padx=10,pady=10)

        btn_tools=tk.Menubutton(frame_botones,text="Herramientas")
        tools_ops=tk.Menu(btn_tools)
        bases_datos_submenu = tk.Menu(tools_ops)
        bases_datos_submenu.add_command(label="Crear nueva BD", command = self.CrearBDNueva) #crea una nueva BD
        bases_datos_submenu.add_command(label="Eliminar BD", command= self.EliminarDB) #elimina una BD
        bases_datos_submenu.add_command(label="Crear DUMP", command=self.CrearDUMP) #crear un script de la base de datos crea un archivo con la creación de tablas, funciones y procedimientos. Solamente Estructura
        bases_datos_submenu.add_command(label="Seleccionar BD") #Muestra un listado de las bases de datos en el sevidor
        tools_ops.add_cascade(label="Bases de Datos", menu=bases_datos_submenu)
        
        sql_submenu = tk.Menu(tools_ops)
        sql_submenu.add_command(label="Nuevo Query", command=self.tools_sql)
        sql_submenu.add_command(label="Ejecutar Query", command=self.run_script)
        tools_ops.add_cascade(label="SQL", menu = sql_submenu)
        
        tools_ops.add_command(label="Exportar") # exportar el contenido de una tabla o varias tablas
        tools_ops.add_command(label="Importar") #importar los datos de una o varias tablas a otra base de datos, ya debe existir la estructura
        btn_tools.config(menu=tools_ops)
        btn_tools.pack(side="left",padx=10,pady=10)

        """btn_runscript=tk.Button(frame_botones,text="Run Script",command=self.run_script)
        btn_runscript.pack(side="left",padx=10,pady=10)

        btn_run_sql=tk.Button(frame_botones,text="Run SQL",command=self.run_sql)
        btn_run_sql.pack(side="left",padx=10,pady=10)"""
        
        btn_run_sql=tk.Button(frame_botones,text="Abrir AST",command=self.mostrar_ventana_imagen)
        btn_run_sql.pack(side="left",padx=10,pady=10)

        #frame_form_fill
        self.frame_form_fill = tk.Frame(frame_menus,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        self.frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        #title = tk.Label(frame_botones, text="Inicio de sesion",font=('Times', 30), fg="#666a88",bg='#fcfcfc',pady=50)
        #title.pack(expand=tk.YES,fill=tk.BOTH)
        self.notebook = ttk.Notebook(frame_menus)
        self.notebook.pack(expand=tk.YES, fill=tk.BOTH)
        #ttk.Button(self.ventana, text="Abrir AST", command=self.mostrar_ventana_imagen).pack(padx=10, pady=10)
        self.tools_sql()
        self.consola()
        self.ventana.mainloop()
        GUI_P._instances.append(self) #son instancias del GUI ya que no funcionaba al momento de eliminar una pestaña y volver a cargar un archivo

    @classmethod
    def get_instances(cls):
        return cls._instances

    def tools_sql(self):
        if self.notebook is None:
            self.notebook = ttk.Notebook(self.frame_form_fill)
            self.notebook.pack()
        self.contador_pestanas += 1
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=f"Query{self.contador_pestanas}")
        print("size note:", self.contador_pestanas)
        texto = tk.Text(tab)
        texto.pack()
        self.mat_text.append(texto)
        tab.bind("<Button-2>", lambda event: self.cerrar_pestana_actual())
        
    def cerrar_pestana_actual(self):
        if not self.notebook.tabs():
            messagebox.showerror("Error", "No hay scripts por cerrar")            
            return
        index = self.notebook.index("current")
        self.mat_text.pop(index)  # Elimina el Text asociado a la pestaña cerrada
        self.notebook.forget(index)
        

    def run_script(self):
        self.mat_consola[0].config(state="normal")
        self.mat_consola[0].delete("1.0", tk.END)
        index = self.notebook.index("current")
        text_widget = self.mat_text[index]
        entrada = text_widget.get("1.0", "end-1c")
        instruccion = Analizar(entrada)
        ast = AST(instruccion)
        arbol = Arbol(self.getInitNodo())
        salidaConsola:[str]=[]
        c:int = 0
        try:
            padre = Nodo("","",0,0)
            for inst in ast.getInstrucciones():
                print("el objeto es de tipo ",type(inst))
                hijo2 = Nodo("","",0,0)
                if isinstance(inst,Instruccion):
                    if padre._token !="":
                        hijo2._token = padre._token
                        hijo2._lexema = padre._lexema
                        hijo2._linea = padre._linea
                        hijo2._columna = padre._columna
                        hijo2._hijos = padre._hijos
                    hijo = Nodo("","",0,0)
                    inst.compilar(ast,self.tablaSimbolos,hijo,salidaConsola)
                    padre = Nodo("INSTRUCCION","inst",0,0)
                    if hijo2._token != "" and hijo._token!="":
                        padre.addHijo(hijo2)
                    if not hijo._token=="":
                        padre.addHijo(hijo)
            arbol._raiz.addHijo(padre)
            ##MANDAMOS A GRAFICAR
            arbol.graficarAST()
            print("el objeto es de tipo ", type(inst))
            if isinstance(inst, Instruccion):
                inst.compilar(ast, None)
            # Muestra el resultado en la consola
            resultado = "Instrucciones ejecutadas en la pestaña Query{}.".format(index + 1)
            self.mat_consola[0].config(state="normal")
            self.mat_consola[0].insert(tk.END, resultado + "\n")
        except Exception as e:
            # Muestra el error en la consola
            error_msg = "Error al ejecutar las instrucciones en la pestaña Query{}: {}".format(index + 1, e)
            self.mat_consola[0].config(state="normal")
            self.mat_consola[0].insert(tk.END, error_msg + "\n")
            salidaConsola.append(f"Error encontrado de tipo Exception: {e}")
        # Después de ejecutar la pestaña actual, deshabilita la edición en la consola
        self.mat_consola[0].config(state="disabled")
        print(salidaConsola)

    def run_sql(self):
        index=self.notebook.index("current")
        cursor_posicion=self.mat_text[index].index(tk.INSERT)
        fila=cursor_posicion.split(".")[0]
        linea_actual=self.mat_text[index].get(f"{fila}.0", f"{fila}.end-1c")
        print("Texto en la línea actual:", linea_actual)
        #parser.parse(linea_actual)

    def getFirstSimbolo(self)->Simbolo:

        simbolo = Simbolo()
        simbolo._identificador = enviroment().useDB
        simbolo._valor=""

        return simbolo
    def getInitNodo(self)->Nodo:

        return Nodo('INICIO','i',0,0)
        

    def reload_data(self):
        resultados = CREATE_XML.xml_gui('dbfile.xml')
        self.update_gui(resultados)
        self.ventana.after(20000, self.reload_data)

    def update_gui(self, resultados):
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Agregar los nuevos datos al Treeview
        root = self.tree.insert("", "end", text="BASES DE DATOS")
        for database_name, tabla_names in resultados:
            h2 = self.tree.insert(root, "end", text=database_name)
            if tabla_names:
                rs = self.tree.insert(h2, "end", text="TABLAS")
                for tabla_name in tabla_names:
                    self.tree.insert(rs, "end", text=tabla_name)
        """
        for database_name, tabla_names, funciones, procedimientos in resultado:
            print(database_name)
            h2=tree.insert(root,"end",text=database_name)
            if tabla_names:
                rs=tree.insert(h2,"end",text="TABLAS")
                for tabla_name in tabla_names:
                    print(tabla_name)
                    tree.insert(rs,"end",text=tabla_name)
            if funciones:
                rs=tree.insert(h2,"end",text="FUNCIONES")
                for funcion in funciones:
                    print(funcion)
                    tree.insert(rs,"end",text=funcion)
            if procedimientos:
                rs=tree.insert(h2,"end",text="PROCEDIMIENTOS")
                for procedimiento in procedimientos:
                    print(procedimiento)
                    tree.insert(rs,"end",text=procedimiento)
        """
                    
                    
    def salir_programa(self):
        self.ventana.destroy()
    
    def guardar_como_archivo(self):
        ruta_archivo = filedialog.asksaveasfilename(defaultextension=".sql", filetypes=[("Archivos SQL", "*.sql"), ("Todos los archivos", "*.*")])
        if ruta_archivo:
            self.archivo_guardado = ruta_archivo
            index = self.notebook.index("current")
            contenido_actual = self.mat_text[index].get("1.0", tk.END)
            with open(ruta_archivo, "w") as archivo:
                archivo.write(contenido_actual)
    
    def abrir_archivo(self):
        if not self.notebook.tabs():
            messagebox.showerror("Error", "No hay scripts para cargar/abrir un archivo.")
            return
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.sql"), ("Todos los archivos", "*.*")])
        if ruta_archivo:
            self.archivo_abierto = ruta_archivo
            index = self.notebook.index("current")
            contenido_archivo = ""
            try:
                with open(ruta_archivo, "r") as archivo:
                    contenido_archivo = archivo.read()
            except FileNotFoundError:
                messagebox.showerror("Error", f"No se pudo encontrar el archivo: {ruta_archivo}")
                return
            self.mat_text[index].delete("1.0", tk.END)
            self.mat_text[index].insert("1.0", contenido_archivo)
            
    def mostrar_ventana_imagen(self):
        try:
            # Obtén el directorio del script actual (front)
            directorio_script = os.path.dirname(__file__)
            # Construye la ruta relativa al directorio raíz
            ruta_imagen = os.path.join(directorio_script, '..', 'AST.png')
            # Normaliza la ruta para manejar barras inclinadas y barras invertidas
            ruta_imagen = os.path.normpath(ruta_imagen)
            # Verifica si el archivo de imagen existe
            if os.path.exists(ruta_imagen):
                # Intenta abrir la imagen con el visor de imágenes del sistema operativo
                subprocess.Popen(['start', ruta_imagen], shell=True)
            else:
                print("La imagen 'AST.png' no existe en la ubicación especificada.")

        except Exception as e:
            # Maneja cualquier excepción que pueda ocurrir al intentar abrir la imagen
            print(f"Error al abrir la imagen: {e}")
    
    
    
    def CrearBDNueva(self):
        creardb=CREATE_XML()
        nombre_bd = simpledialog.askstring("Crear Base de Datos", "Inserte el nombre de la base de datos:")
        #print(nombre_bd)
        creardb.create_db(nombre_bd)
        """
        tabla1=TBL("db_test4","my_tab1")
        columna1=COLUM("otra col","INT",False,None,11,False)
        tabla1.insert_column(columna1)
        creardb.insert_table(tabla1)
        """
        
    def EliminarDB(self):
        elimDB = CREATE_XML()
        nombre_db = simpledialog.askstring("Eliminar Base de Datos", "Ingres el nombre de la base de datos:")
        #print(f"La base de datos: {nombre_db} fue eliminada con exito")
        elimDB.delete_db(nombre_db)
        
    def CrearDUMP(self):
        #print("dump")
        crear= CREATE_XML()
        nombre = simpledialog.askstring("Crear DUMP", "Ingrese el nombre de la Base de datos:")
        crear.createDump(nombre)
    
    def exportarDB(self):
        print("exportar")
        
    def importarDB(self):
        print("importar")
        nombre = simpledialog.askstring("Crear DUMP", "Ingrese el nombre de la Base de datos:")
        
        
    def consola(self):
        frame_consola = tk.Frame(self.frame_form_fill)
        frame_consola.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        notebook_consola = ttk.Notebook(frame_consola)
        notebook_consola.pack(expand=tk.YES, fill=tk.BOTH)
        tab_consola = ttk.Frame(notebook_consola)
        notebook_consola.add(tab_consola, text="Consola")
        consola_texto = tk.Text(tab_consola, wrap=tk.WORD, width=80, height=15, state="disabled") #para que no se pueda modificar la consola
        consola_texto.pack(expand=True, fill=tk.BOTH)
        self.mat_consola.append(consola_texto)

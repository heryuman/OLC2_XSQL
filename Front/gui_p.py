import tkinter as tk
from tkinter import ttk
from util.generic import GENERIC
from Analizador.sintactico import parser
from Analizador.sintactico import useDB
from Abstract.Instruccion import Instruccion
from Arbol.AST import AST
from util.manipulador_xml import CREATE_XML
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import simpledialog

from util.table import TBL
from util.column import COLUM
import os
class GUI_P:
    _instances = [] #esta instancia permite hacer lo de cerrar una pestaña y luego poder abrir y que si se carge el contenido del archivo
    def __init__(self) :
        self.contador_pestanas = 0
        self.notebook=None
        self.mat_text=[]
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
        
        
        self.ventana.after(2000, self.reload_data)       
        
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
        bases_datos_submenu.add_command(label="Eliminar BD") #elimina una BD
        bases_datos_submenu.add_command(label="Crear DUMP") #crear un script de la base de datos crea un archivo con la creación de tablas, funciones y procedimientos. Solamente Estructura
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
        index = self.notebook.index("current")
        entrada = self.mat_text[index].get("1.0", "end-1c")
        instruccion = parser.parse(entrada)
        ast = AST(instruccion)

        try:
            for inst in ast.getInstrucciones():
                print("el objeto es de tipo ",type(inst))
                if isinstance(inst,Instruccion):
                    inst.compilar(ast,None)
        
        except Exception as e:
            print(f"Error al ejecutar las instrucciones: {e} ")

    def run_sql(self):
        index=self.notebook.index("current")
        cursor_posicion=self.mat_text[index].index(tk.INSERT)
        fila=cursor_posicion.split(".")[0]
        linea_actual=self.mat_text[index].get(f"{fila}.0", f"{fila}.end-1c")
        print("Texto en la línea actual:", linea_actual)
        parser.parse(linea_actual)

    def reload_data(self):
        resultados = CREATE_XML.xml_gui('dbfile.xml')
        self.update_gui(resultados)
        self.ventana.after(2000, self.reload_data)

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
        ventana_imagen = tk.Toplevel(self.ventana)
        ventana_imagen.title('Reporte AST')
        #para obtener dimenciones de la pantalla
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        #print("valorx " , ancho_pantalla)
        #print("valory " , alto_pantalla)
        ventana_imagen.geometry(f"{ancho_pantalla}x{alto_pantalla}") #tamaño de la ventana al tamaño de la pantalla
        ruta_imagen = "AST.png"
        if os.path.exists(ruta_imagen):
            imagen = Image.open(ruta_imagen)
            #la imagen debe de ocupar toda la ventana para verse completa
            cambiarDimencion = imagen.resize((ancho_pantalla, alto_pantalla))
            imagen_tk = ImageTk.PhotoImage(cambiarDimencion)
            imagen = ttk.Label(ventana_imagen, image=imagen_tk) #para la nueva ventana
            imagen.image = imagen_tk  #para que se muestre la imagen en la ventana
            imagen.pack(fill="both", expand=True) #dimenciones de la imagen dentro de la pantalla
        else:
            ttk.Label(ventana_imagen, text="El AST aun no se genera.").pack(padx=10, pady=10)
    
    
    
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
import tkinter as tk
from tkinter import ttk
from util.generic import GENERIC
from Analizador.sintactico import parser
class GUI_P:
    def __init__(self) :
        self.notebook=None
        self.mat_text=[]
        utl= GENERIC()
        self.ventana=tk.Tk()
        self.ventana.title('SQLX')
        self.ventana.config(bg='#ffffff')
        #self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,800,500)
        #frame treeview
        frame_treeview= tk.Frame(self.ventana,bd=0,width=15,relief=tk.SOLID,padx=10,pady=10,bg='#3a7fff')
        frame_treeview.pack(side='left',fill=tk.BOTH)
        tree= ttk.Treeview(frame_treeview,height=100)
        root=tree.insert("","end",text="Raiz")
        tree.insert(root,"end",text="Hoja1")
        h2=tree.insert(root,"end",text="Hoja2")
        rs=tree.insert(h2,"end",text="Rama Secundaria")
        tree.insert(rs,"end",text="Hoja3")
       # tree.place(x=0,y=0,relwidth=1,relheight=1)
        tree.pack(side="left")

        #frame_menus
        frame_menus = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#3a7fff',padx=10,pady=10)
        frame_menus.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #frame_botones
        frame_botones = tk.Frame(frame_menus,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_botones.pack(side="top",fill=tk.X)
        #botones
        btn_archivo= tk.Menubutton(frame_botones,text="Archivo")
        archivo_ops=tk.Menu(btn_archivo)
        archivo_ops.add_command(label="Abrir")
        archivo_ops.add_command(label="Guardar")
        archivo_ops.add_command(label="Guardar como")
        archivo_ops.add_command(label="Cerrar")
        archivo_ops.add_command(label="Salir")
        btn_archivo.config(menu=archivo_ops)
        btn_archivo.pack(side="left",padx=10,pady=10)

        btn_tools=tk.Menubutton(frame_botones,text="Herramientas")
        tools_ops=tk.Menu(btn_tools)
        tools_ops.add_command(label="Bases de Datos")
        tools_ops.add_command(label="SQL",command=self.tools_sql)
        tools_ops.add_command(label="Exportar")
        tools_ops.add_command(label="Importar")
        btn_tools.config(menu=tools_ops)
        btn_tools.pack(side="left",padx=10,pady=10)

        btn_runscript=tk.Button(frame_botones,text="Run Script",command=self.run_script)
        btn_runscript.pack(side="left",padx=10,pady=10)

        btn_run_sql=tk.Button(frame_botones,text="Run SQL",command=self.run_sql)
        btn_run_sql.pack(side="left",padx=10,pady=10)

        #frame_form_fill
        self.frame_form_fill = tk.Frame(frame_menus,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        self.frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        #title = tk.Label(frame_botones, text="Inicio de sesion",font=('Times', 30), fg="#666a88",bg='#fcfcfc',pady=50)
        #title.pack(expand=tk.YES,fill=tk.BOTH)
        self.ventana.mainloop()


    def tools_sql(self):
        if self.notebook is None:
            self.notebook=ttk.Notebook(self.frame_form_fill)
            self.notebook.pack()
        tab=ttk.Frame(self.notebook)
        self.notebook.add(tab,text="Query"+str(len(self.notebook.tabs())+1))
        print("size note: "+str(len(self.notebook.tabs())))
        texto=tk.Text(tab)
        texto.pack()
        self.mat_text.append(texto)

    def run_script(self):
        index = self.notebook.index("current")
        entrada = self.mat_text[index].get("1.0", "end-1c")
        #print("index: ", index, "- size mat_text: ", len(self.mat_text), entrada)
        
        # Suponiendo que 'parser' es una instancia de LRParser
        parser.parse(entrada)

    def run_sql(self):
        index=self.notebook.index("current")
        cursor_posicion=self.mat_text[index].index(tk.INSERT)
        fila=cursor_posicion.split(".")[0]
        linea_actual=self.mat_text[index].get(f"{fila}.0", f"{fila}.end-1c")
        print("Texto en la línea actual:", linea_actual)
        parser.parse(linea_actual)


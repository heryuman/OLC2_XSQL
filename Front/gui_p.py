import tkinter as tk
from tkinter import ttk
from util.generic import GENERIC
class GUI_P:
    def __init__(self) :
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
        tools_ops.add_command(label="SQL")
        tools_ops.add_command(label="Exportar")
        tools_ops.add_command(label="Importar")
        btn_tools.config(menu=tools_ops)
        btn_tools.pack(side="left",padx=10,pady=10)
        

        #title = tk.Label(frame_botones, text="Inicio de sesion",font=('Times', 30), fg="#666a88",bg='#fcfcfc',pady=50)
        #title.pack(expand=tk.YES,fill=tk.BOTH)
        self.ventana.mainloop()


        


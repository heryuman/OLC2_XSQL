import tkinter as tk

root = tk.Tk()

# Creamos un panel
panel = tk.Frame(root)

# Colocamos el panel en la derecha
panel.pack(side="right")

# Agregamos una etiqueta al panel
label = tk.Label(panel, text="Etiqueta")
label.pack()

# Agregamos un cuadro de texto al panel
entry = tk.Entry(panel)
entry.pack()

# Agregamos una lista al panel
listbox = tk.Listbox(panel)
listbox.pack()

root.mainloop()

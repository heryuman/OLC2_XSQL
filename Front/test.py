import tkinter as tk

def obtener_linea_actual():
    # Obtener la posición del cursor
    cursor_posicion = text_widget.index(tk.INSERT)

    # Extraer la parte de la fila de la posición
    fila = cursor_posicion.split(".")[0]

    # Obtener el texto de la línea actual
    linea_actual = text_widget.get(f"{fila}.0", f"{fila}.end-1c")
    print("Texto en la línea actual:", linea_actual)

# Crear la aplicación principal
app = tk.Tk()
app.title("Ejemplo de Texto - Línea Actual")

# Crear un widget Text
text_widget = tk.Text(app, height=5, width=30)
text_widget.pack(padx=10, pady=10)

# Botón para obtener la línea actual
boton_obtener_linea = tk.Button(app, text="Obtener Línea Actual", command=obtener_linea_actual)
boton_obtener_linea.pack(pady=10)

# Iniciar el bucle principal de la aplicación
app.mainloop()

import tkinter as tk
from tkinter import ttk

def agregar_dato():
    dato = entrada.get()
    if dato:
        lista.insert('', 'end', values=(dato,))
        entrada.delete(0, tk.END)

def limpiar_datos():
    for item in lista.get_children():
        lista.delete(item)

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación GUI con Tkinter")
root.geometry("400x300")

# Crear y colocar los componentes GUI
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Ingrese un dato:").grid(row=0, column=0, padx=5, pady=5)
entrada = tk.Entry(frame)
entrada.grid(row=0, column=1, padx=5, pady=5)

btn_agregar = tk.Button(frame, text="Agregar", command=agregar_dato)
btn_agregar.grid(row=0, column=2, padx=5, pady=5)

lista = ttk.Treeview(root, columns=("Dato",), show='headings')
lista.heading("Dato", text="Dato")
lista.pack(pady=10)

btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_datos)
btn_limpiar.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()


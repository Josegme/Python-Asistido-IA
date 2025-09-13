"""
Editor y Catálogo de Productos con Tkinter
------------------------------------------

Esta aplicación carga automáticamente un archivo 'productos.json' y muestra los productos en una tabla interactiva.

Características implementadas:
- Carga de productos desde JSON al iniciar.
- Tabla visual con columnas: ID, Nombre, Descripción, Precio.
- Colores alternados en filas para mejor lectura (Zebra stripes).
- Subventana de detalles al hacer doble clic en un producto.
- Búsqueda de productos por nombre.
- Exportar lista de productos a CSV.
- Feedback visual con mensajes y botones para cerrar subventanas.

Requisitos:
- Python 3.x
- Tkinter (incluido en Python)
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import csv

# Función para cargar productos desde JSON
def cargar_productos():
    try:
        with open("productos.json", "r", encoding="utf-8") as archivo:
            productos = json.load(archivo)
            return productos
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo 'productos.json'.")
        return []
    except json.JSONDecodeError:
        messagebox.showerror("Error", "El archivo 'productos.json' no es válido.")
        return []

# Función para mostrar detalles de un producto en una subventana
def mostrar_detalles(event):
    item_seleccionado = tabla.focus()  # Obtener el item seleccionado
    if not item_seleccionado:
        return
    datos = tabla.item(item_seleccionado, "values")

    subventana = tk.Toplevel(ventana)
    subventana.title(f"Detalles de {datos[1]}")
    subventana.geometry("400x250")
    subventana.configure(bg="#f0f0f0")

    tk.Label(subventana, text=f"ID: {datos[0]}", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5, anchor="w", padx=10)
    tk.Label(subventana, text=f"Nombre: {datos[1]}", font=("Arial", 12), bg="#f0f0f0").pack(pady=5, anchor="w", padx=10)
    tk.Label(subventana, text=f"Descripción: {datos[2]}", font=("Arial", 12), wraplength=380, justify="left", bg="#f0f0f0").pack(pady=5, anchor="w", padx=10)
    tk.Label(subventana, text=f"Precio: {datos[3]}", font=("Arial", 12), bg="#f0f0f0").pack(pady=5, anchor="w", padx=10)

    tk.Button(subventana, text="Cerrar", command=subventana.destroy).pack(pady=10)

# Función para buscar productos por nombre
def buscar_producto():
    filtro = entrada_buscar.get().lower()
    for i in tabla.get_children():
        tabla.delete(i)
    for producto in productos:
        if filtro in producto["NOMBRE"].lower():
            tabla.insert("", tk.END, values=(
                producto.get("ID", ""),
                producto.get("NOMBRE", ""),
                producto.get("DESCRIPCION", ""),
                f"${producto.get('PRECIO', 0):.2f}"
            ))

# Función para exportar productos a CSV
def exportar_csv():
    ruta = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if ruta:
        try:
            with open(ruta, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["ID", "Nombre", "Descripción", "Precio"])
                for producto in productos:
                    writer.writerow([producto.get("ID"), producto.get("NOMBRE"), producto.get("DESCRIPCION"), producto.get("PRECIO")])
            messagebox.showinfo("Exportado", f"Productos exportados a {ruta} correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar el archivo:\n{e}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Catálogo de Productos")
ventana.geometry("800x500")
ventana.configure(bg="#f0f0f0")

# Frame para búsqueda
frame_buscar = tk.Frame(ventana, bg="#f0f0f0")
frame_buscar.pack(fill=tk.X, padx=10, pady=5)
tk.Label(frame_buscar, text="Buscar producto:", bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
entrada_buscar = tk.Entry(frame_buscar)
entrada_buscar.pack(side=tk.LEFT, padx=5)
tk.Button(frame_buscar, text="Buscar", command=buscar_producto).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buscar, text="Exportar CSV", command=exportar_csv).pack(side=tk.RIGHT, padx=5)

# Frame para la tabla
frame_tabla = ttk.Frame(ventana)
frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Crear la tabla con columnas
columnas = ("ID", "Nombre", "Descripción", "Precio")
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

# Configurar encabezados
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, anchor=tk.W, width=150)
tabla.column("Descripción", width=300)  # Dar más ancho a la descripción
tabla.pack(fill=tk.BOTH, expand=True)

# Agregar scrollbar vertical
scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Cargar productos y agregarlos a la tabla
productos = cargar_productos()
for index, producto in enumerate(productos):
    tabla.insert("", tk.END, values=(
        producto.get("ID", ""),
        producto.get("NOMBRE", ""),
        producto.get("DESCRIPCION", ""),
        f"${producto.get('PRECIO', 0):.2f}"
    ), tags=('evenrow' if index % 2 == 0 else 'oddrow',))

# Estilo visual con colores alternados
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
                background="#e1f5fe",
                foreground="black",
                rowheight=25,
                fieldbackground="#e1f5fe")
style.map("Treeview", background=[("selected", "#0288d1")])
tabla.tag_configure('evenrow', background="#e1f5fe")
tabla.tag_configure('oddrow', background="#b3e5fc")

# Evento de doble clic para abrir subventana
tabla.bind("<Double-1>", mostrar_detalles)

ventana.mainloop()

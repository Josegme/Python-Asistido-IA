import tkinter as tk
from tkinter import filedialog, messagebox

# Función para abrir un archivo
def abrir_archivo():
    ruta_archivo = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if ruta_archivo:
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                text_area.delete(1.0, tk.END)  # Limpiar área de texto
                text_area.insert(tk.END, contenido)  # Insertar contenido
            ventana.title(f"Editor de Texto - {ruta_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{e}")

# Función para guardar un archivo
def guardar_archivo():
    ruta_archivo = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if ruta_archivo:
        try:
            contenido = text_area.get(1.0, tk.END)  # Obtener todo el contenido
            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                archivo.write(contenido)
            ventana.title(f"Editor de Texto - {ruta_archivo}")
            messagebox.showinfo("Guardado", "Archivo guardado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")

# Funciones de copiar y pegar
def copiar_texto():
    try:
        texto = text_area.get(tk.SEL_FIRST, tk.SEL_LAST)  # Obtener texto seleccionado
        ventana.clipboard_clear()
        ventana.clipboard_append(texto)
    except tk.TclError:
        messagebox.showwarning("Advertencia", "No hay texto seleccionado para copiar.")

def pegar_texto():
    try:
        texto = ventana.clipboard_get()
        text_area.insert(tk.INSERT, texto)
    except tk.TclError:
        messagebox.showwarning("Advertencia", "El portapapeles está vacío.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Editor de Texto")
ventana.geometry("600x400")

# Crear un área de texto
text_area = tk.Text(ventana, wrap=tk.WORD, undo=True)
text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Crear un menú
menu_principal = tk.Menu(ventana)
ventana.config(menu=menu_principal)

# Menú Archivo
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)

# Menú Editar
menu_editar = tk.Menu(menu_principal, tearoff=0)
menu_editar.add_command(label="Copiar", command=copiar_texto)
menu_editar.add_command(label="Pegar", command=pegar_texto)
menu_principal.add_cascade(label="Editar", menu=menu_editar)

ventana.mainloop()

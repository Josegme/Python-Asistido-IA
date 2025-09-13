import tkinter as tk
from tkinter import messagebox, filedialog
import random
import string

def generar_password():
    try:
        longitud = int(entry_longitud.get())  # obtiene la longitud escrita por el usuario
        if longitud < 4:
            messagebox.showwarning("Advertencia", "La longitud mínima debe ser 4")
            return

        # Definimos los caracteres que se pueden usar
        caracteres = string.ascii_lowercase + string.digits + string.punctuation

        # Generar la contraseña
        password = "".join(random.choice(caracteres) for _ in range(longitud))

        # Mostrar en la caja de texto
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido")

def copiar_password():
    password = entry_resultado.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copiado", "La contraseña se copió al portapapeles")
    else:
        messagebox.showwarning("Advertencia", "No hay contraseña generada para copiar")

def guardar_password():
    password = entry_resultado.get()
    if password:
        try:
            archivo = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Archivo de texto", "*.txt")],
                title="Guardar contraseña"
            )
            if archivo:
                with open(archivo, "w") as f:
                    f.write(password)
                messagebox.showinfo("Guardado", f"Contraseña guardada en:\n{archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar la contraseña:\n{e}")
    else:
        messagebox.showwarning("Advertencia", "No hay contraseña para guardar")

# Crear ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas")
root.geometry("400x250")
root.resizable(False, False)

# Etiqueta y entrada para longitud
label_longitud = tk.Label(root, text="Longitud de la contraseña:", font=("Arial", 12))
label_longitud.pack(pady=5)

entry_longitud = tk.Entry(root, font=("Arial", 12), justify="center")
entry_longitud.pack(pady=5)

# Botón para generar
btn_generar = tk.Button(root, text="Generar Contraseña", font=("Arial", 12), command=generar_password)
btn_generar.pack(pady=10)

# Resultado
entry_resultado = tk.Entry(root, font=("Arial", 12), justify="center")
entry_resultado.pack(pady=5)

# Botón para copiar
btn_copiar = tk.Button(root, text="Copiar Contraseña", font=("Arial", 12), command=copiar_password)
btn_copiar.pack(pady=5)

# Botón para guardar
btn_guardar = tk.Button(root, text="Guardar en TXT", font=("Arial", 12), command=guardar_password)
btn_guardar.pack(pady=5)

# Loop principal
root.mainloop()

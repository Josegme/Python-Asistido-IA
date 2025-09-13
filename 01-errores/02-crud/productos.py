from main import (
    crear_producto,
    leer_producto,
    actualizar_producto,
    borrar_producto,
    mostrar_productos
)

# --- Crear productos ---
print("\n👉 Creando productos...")
crear_producto("Camisa", "Camisa de algodón", 20.0)
crear_producto("Pantalón", "Pantalón de mezclilla", 30.0)
crear_producto("Zapatillas", "Zapatillas deportivas", 50.0, "Nike")
mostrar_productos()

# --- Leer producto ---
print("\n👉 Leyendo un producto específico (Camisa):")
producto = leer_producto("Camisa")
if producto:
    print(f"Encontrado: {producto.nombre} - {producto.descripcion} - ${producto.precio}")
else:
    print("Producto no encontrado.")

# --- Actualizar producto ---
print("\n👉 Actualizando producto (Pantalón)...")
actualizar_producto("Pantalón", precio=35.0, descripcion="Pantalón de mezclilla azul")
mostrar_productos()

# --- Intentar actualizar con marca un Producto normal ---
print("\n👉 Probando actualizar marca de un producto sin marca (Camisa)...")
actualizar_producto("Camisa", marca="Adidas")  # Debería dar advertencia

# --- Borrar producto ---
print("\n👉 Borrando producto (Zapatillas)...")
borrar_producto("Zapatillas")
mostrar_productos()

# --- Intentar borrar algo que no existe ---
print("\n👉 Intentando borrar un producto inexistente (Zapatos)...")
try:
    borrar_producto("Zapatos")
except ValueError as e:
    print(f"Error: {e}")

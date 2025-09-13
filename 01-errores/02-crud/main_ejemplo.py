class Producto:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

class Subproducto(Producto):
    def __init__(self, nombre, descripcion, precio, marca):
        super().__init__(nombre, descripcion, precio)
        self.marca = marca


# Crear una lista de productos de prueba
productos = [
    Producto('Camisa', 'Camisa de algodón', 20.0),
    Producto('Pantalón', 'Pantalón de mezclilla', 30.0),
    Subproducto('Zapatillas', 'Zapatillas deportivas', 50.0, 'Nike')
]

# Funciones CRUD
def crear_producto(nombre, descripcion, precio, marca=None):
    if marca:
        producto = Subproducto(nombre, descripcion, precio, marca)
    else:
        producto = Producto(nombre, descripcion, precio)
    productos.append(producto)

def leer_producto(nombre):
    for producto in productos:
        if producto.nombre == nombre:
            return producto
    return None

def actualizar_producto(nombre, descripcion=None, precio=None, marca=None):
    producto = leer_producto(nombre)
    if producto:
        if descripcion:
            producto.descripcion = descripcion
        if precio:
            producto.precio = precio
        if marca:
            producto.marca = marca
    else:
        raise ValueError("Producto no encontrado")

def borrar_producto(nombre):
    producto = leer_producto(nombre)
    if producto:
        productos.remove(producto)
    else:
        raise ValueError("Producto no encontrado")
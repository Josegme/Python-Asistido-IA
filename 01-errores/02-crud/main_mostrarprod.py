class Producto:
    """
    Clase que representa un producto básico.

    Atributos:
        nombre (str): Nombre del producto.
        descripcion (str): Descripción del producto.
        precio (float): Precio del producto.
    """
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio


class Subproducto(Producto):
    """
    Clase que representa un subproducto que hereda de Producto y añade marca.

    Atributos:
        marca (str): Marca del subproducto.
    """
    def __init__(self, nombre, descripcion, precio, marca):
        super().__init__(nombre, descripcion, precio)
        self.marca = marca


# Lista de productos inicial
productos = [
    Producto('Camisa', 'Camisa de algodón', 20.0),
    Producto('Pantalón', 'Pantalón de mezclilla', 30.0),
    Subproducto('Zapatillas', 'Zapatillas deportivas', 50.0, 'Nike')
]


# Funciones CRUD

def crear_producto(nombre, descripcion, precio, marca=None):
    """
    Crea un producto o subproducto y lo agrega a la lista de productos.
    """
    if marca:
        producto = Subproducto(nombre, descripcion, precio, marca)
    else:
        producto = Producto(nombre, descripcion, precio)
    productos.append(producto)


def leer_producto(nombre):
    """
    Busca un producto por su nombre.
    """
    for producto in productos:
        if producto.nombre == nombre:
            return producto
    return None


def actualizar_producto(nombre, descripcion=None, precio=None, marca=None):
    """
    Actualiza los atributos de un producto existente.
    """
    producto = leer_producto(nombre)
    if producto:
        if descripcion is not None:
            producto.descripcion = descripcion
        if precio is not None:
            producto.precio = precio
        if marca is not None:
            if isinstance(producto, Subproducto):
                producto.marca = marca
            else:
                print("Advertencia: Este producto no tiene atributo 'marca'")
    else:
        raise ValueError("Producto no encontrado")


def borrar_producto(nombre):
    """
    Elimina un producto de la lista por su nombre.
    """
    producto = leer_producto(nombre)
    if producto:
        productos.remove(producto)
    else:
        raise ValueError("Producto no encontrado")


def mostrar_productos():
    """
    Muestra todos los productos disponibles en la lista.

    Retorna:
        None: Imprime en consola los productos y sus detalles.
    """
    if not productos:
        print("No hay productos disponibles.")
        return

    print("\n📦 Lista de productos disponibles:")
    for producto in productos:
        if isinstance(producto, Subproducto):
            print(f"- {producto.nombre} | {producto.descripcion} | ${producto.precio:.2f} | Marca: {producto.marca}")
        else:
            print(f"- {producto.nombre} | {producto.descripcion} | ${producto.precio:.2f}")

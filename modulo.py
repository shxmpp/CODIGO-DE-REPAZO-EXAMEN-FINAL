def stock_categoria(categoria, productos, inventario):
    total = 0

    for codigo in productos:
        if productos[codigo][1].lowe() == categoria.lowe():

            total += inventario[codigo][0]

        print("Stock total", total)


def buscar_precio(precio_min, precio_max, productos, inventario):

    lista = []

    for codigo in productos:
        precio = productos[codigo][2]
        stock = inventario[codigo][0]

        if precio_min <= precio <= precio_max and stock > 0:
            lista.append((productos[codigo][0], codigo))
    lista.sort()

    for nombre, codigo in lista:
        print(nombre, "--", codigo)


def actualizar_precio(codigo, nuevo_precio, productos):

    if codigo in productos:
        productos[codigo.upper()][2] = nuevo_precio

        return True

    return False


def agregar_productos(
    codigo,
    nombre,
    categoria,
    precio,
    disponible,
    stock,
    vendidos,
    productos,
    inventario,
):
    if codigo in productos:
        return False

    productos[codigo] = [nombre, categoria, precio, disponible]
    inventario[codigo] = [stock, vendidos]
    return True


def eliminar_produscto(codigo, producto, inventario):
    if codigo in producto:
        del producto[codigo]
        del inventario[codigo]

        return True

    return False


def mostrar_producto(producto, inventario):

    for codigo in producto:
        print("--------------------------------------------------")
        print("Codigo", codigo)
        print("Nombre", producto[codigo][0])
        print("Categoria", producto[codigo][1])
        print("Precio", producto[codigo][2])
        print("Disponible", producto[codigo][3])
        print("Stock", inventario[codigo][0])
        print("Vendidos", inventario[codigo][1])
        print("-------------------------------------------------")


# Definimos los validadores


def validamo_codigo(codigo, productos):

    codigo = codigo.strip().upper()

    if codigo == " ":
        return False

    if codigo in productos:
        return False

    return True


def validamos_nombre(nombre):
    return nombre.strip() != " "


def validamos_categoria(categoria):
    return categoria.strip() != " "


def validamos_precio(precio):
    return precio > 0


def validamos_stock(stock):
    return stock > 0


def validamos_vendidos(vendidos):
    return vendidos > 0


def validamos_disponibles(opcion):
    return opcion.strip().lower() in ["s", "n"]

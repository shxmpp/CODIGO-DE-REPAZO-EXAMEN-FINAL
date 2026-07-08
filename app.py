import modulo
import os


def main():
    productos = {
        "P101": ["Cuaernos", "Papeleria", 2490, True],
        "P102": ["Lapiz", "Papeleria", 590, True],
        "P103": ["Botella", "Accesorios", 6990, True],
        "P104": ["Mochila", "Accesorios", 24990, True],
    }
    inventario = {
        "P101": [30, 15],
        "P102": [120, 50],
        "P103": [0, 10],
        "P104": [8, 25],
    }
    while True:
        os.system("cls")
        opcion = print(f"""
            ========== MENÚ PRINCIPAL ==========
            1. Stock por categoría
            2. Buscar productos por rango de precio
            3. Actualizar precio
            4. Agregar producto
            5. Eliminar producto
            6. Mostrar productos
            7. Salir
            ===================================
            """)
        match opcion:
            case "1":
                os.system("cls")
                categoria = input("Ingrese categoria: ")
                modulo.stock_categoria(categoria, productos, inventario)
                os.system("pause")

            case "2":
                os.system("cls")
                try:
                    minimo = int(input("Precio minimo: "))
                    maximo = int(input("Ingrese maximo: "))

                    modulo.buscar_precio(minimo, maximo, productos, inventario)
                except:
                    print("Debe ingresar numero")
                os.system("pause")

            case "3":
                os.system("cls")
                try:
                    codigo = input("Codigo: ")

                    precio = int(input("Nuevo precio: "))

                    if modulo.actualizar_precio(codigo, precio, productos):
                        print("Precio Actualizado")
                    else:
                        print("El codigo no existe")
                except:
                    print("Debe ingresar un numero")

                os.system("pause")
            case "4":
                os.system("cls")
                while True:

                    codigo = input("Igrese el codigo: ").upper()

                    if modulo.validamo_codigo(codigo, productos):
                        break
                    print("Codigo invalido")

                while True:

                    nombre = input("Ingrese el nombre: ")

                    if modulo.validamos_nombre(nombre):
                        break
                    print("El nombre es invalido")

                while True:

                    categoria = input("Ingrese la categria: ")

                    if modulo.validamos_categoria(categoria):
                        break
                    print("La categoria es invalida")

                while True:
                    precio = int(input("Ingrese el precio: "))

                    if modulo.validamos_precio(precio):
                        break
                    print("El precio es invalido")

                while True:

                    disponible = print("Diposnible (S/N): ").lower()

                    if modulo.validamos_disponibles(disponible):
                        disponible == "s" or disponible == "n"
                        break

                while True:
                    try:
                        stock = int(input("Ingrese el stock: "))

                        if modulo.validamos_stock(stock):
                            break
                        print("Stock invalido")
                    except ValueError:
                        print("Debe ingresar un numero")

                while True:
                    try:
                        vendidos = int(input("Ingrese la cantidad de vendidos: "))

                        if modulo.validamos_vendidos(vendidos):
                            break
                        print("Cantidad de vendido invalida")
                    except ValueError:
                        print("Debe ingresar un numero")

                if modulo.agregar_productos(
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
                    print("Productos agregados correctamente.")
                else:
                    print("El codigo ya existe")

                os.system("pause")

            case "5":
                os.system("cls")
                codigo = input("Ingrese el codigo del producto a eliminar: ").upper()

                if modulo.eliminar_produscto(codigo, productos, inventario):
                    print("Productos eliminados correctamente")
                else:
                    print("codigo inexitente")

                os.system("pause")

            case "6":
                os.system("cls")
                modulo.mostrar_producto(productos, inventario)
                input("\n Presione ENTER para volver al menú")
                os.system("pause")

            case "7":
                os.system("cls")
                print("Saliendo de la app...")
                break


if __name__ == "___main__":
    main()

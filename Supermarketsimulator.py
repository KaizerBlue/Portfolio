from colorama import Fore, Back, Style
import os

productos = [
    {"nombre": "manzanas", "precio": 2.5, "cantidad": 32},
    {"nombre": "bananas", "precio": 1.75, "cantidad": 17},
    {"nombre": "leche", "precio": 3.0, "cantidad": 8},
    {"nombre": "pañuelos", "precio": 2.0, "cantidad": 27},
    {"nombre": "harina", "precio": 4.9, "cantidad": 9},
    {"nombre": "yerba", "precio": 3.0, "cantidad": 25},
    {"nombre": "choclo", "precio": 1.49, "cantidad": 19},
    {"nombre": "aceitunas", "precio": 2.49, "cantidad": 23},
    {"nombre": "te", "precio": 2.99, "cantidad": 65},
    {"nombre": "coca-cola", "precio": 4.99, "cantidad": 55},
]

ventas = [
    {"nombre": "manzanas", "cantidad": 22},
    {"nombre": "bananas", "cantidad": 13},
    {"nombre": "leche", "cantidad": 12},
    {"nombre": "pañuelos", "cantidad": 23},
    {"nombre": "harina", "cantidad": 19},
    {"nombre": "yerba", "cantidad": 15},
    {"nombre": "choclo", "cantidad": 13},
    {"nombre": "aceitunas", "cantidad": 13},
    {"nombre": "te", "cantidad": 35},
    {"nombre": "coca-cola", "cantidad": 5},
]

################################################################################################## PRODUCTOS

def lista_productos(): # Sirve para ver el listado de los productos.
    limpiar_consola()
    print("\n--- Productos Disponibles ---")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto['nombre']}: ${producto['precio']} - Disponibles: {producto['cantidad']}")

def agregar_producto(): # El usuario podrá agregar un producto a la lista.
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad disponible: "))
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"Producto '{nombre}' agregado correctamente.")
    frenar_flujo()

def eliminar_producto(): # El usuario podrá eliminar un producto de la lista.
    lista_productos()
    if productos:
        try:
            opcion = int(input("Ingrese el numero del producto a eliminar (0 para cancelar): "))
            if 1 <= opcion <= len(productos):
                producto_eliminado = productos.pop(opcion - 1)
                print(f"Producto '{producto_eliminado['nombre']}' eliminado correctamente.")
                frenar_flujo()
            elif opcion == 0:
                return
            
            else:
                print("¡OPCIÓN INVALIDA!")
                frenar_flujo()
        except ValueError as e:
            print(Fore.LIGHTRED_EX + "¡ERROR: ",e,"!")
            frenar_flujo()
    else:
        print(Fore.LIGHTRED_EX+"No hay productos para eliminar")
        frenar_flujo()

def editar_producto(): # El usuario podrá editar un producto de la lista.
    lista_productos()
    if productos:
        try:
            opcion = int(input("Ingrese el numero del producto a editar (0 para cancelar): "))
            if 1 <= opcion <= len(productos):
                producto = productos[opcion -1]
                print(f"Editando producto... '{producto['nombre']}")
                nombre = input("Ingrese un nuevo nombre(Dejar vacio para mantener): ")
                if nombre.strip():
                    producto['nombre'] = nombre
                precio = input("Ingrese un nuevo precio(Dejar vacio para mantener): ")
                if precio.strip():
                    producto['precio'] = float(precio)
                cantidad = input("Ingrese nueva cantidad de stock(Dejar vacio para mantener): ")
                if cantidad.strip():
                    producto['cantidad'] = int(cantidad)
                print(f"Producto '{producto['nombre']}' editado correctamente ;)")
                frenar_flujo()
            elif opcion == 0:
                return
            else:
                print("¡OPCIÓN INVALIDA!")
                frenar_flujo()
        except ValueError as e:
            print(Fore.LIGHTRED_EX + "¡ERROR: ",e,"!")
            frenar_flujo()

################################################################################################## VENTAS

def lista_ventas(): # Sirve para ver el listado de los productos vendidos y a su vez el total de ingresos.
    limpiar_consola()
    print("\n--- Productos Vendidos ---")
    for i, venta in enumerate(ventas, start=1):
        nombre_producto = venta['nombre']
        cantidad_vendida = venta['cantidad']
        
        # Obtener el precio del producto desde la lista de productos
        precio_unitario = obtener_precio_unitario(nombre_producto)
        
        if precio_unitario is not None:
            # Imprimir el nombre del producto, su precio y la cantidad vendida
            print(f"{i}. {nombre_producto}: ${precio_unitario:.2f} - Cantidad vendidos: {cantidad_vendida}")
        else:
            print(f"{i}. {nombre_producto}: Precio no encontrado - Cantidad vendidos: {cantidad_vendida}")

def calcular_total_vendidos():
    total = 0.0
    for venta in ventas:
        nombre_producto = venta['nombre']
        cantidad_vendida = venta['cantidad']
        for producto in productos:
            if producto['nombre'] == nombre_producto:
                precio_unitario = producto['precio']
                total += precio_unitario * cantidad_vendida
                break
    print(f"Total ingresos por ventas: ${total:.2f}")

def obtener_precio_unitario(nombre_producto):
    for producto in productos:
        if producto['nombre'] == nombre_producto:
            return producto['precio']
    return None  # Retornar None si no se encuentra el producto

def agregar_venta():
    print("\n--- Agregar Nueva Venta ---")
    nombre = input("Ingrese el nombre del producto: ").lower()
    cantidad = int(input("Cantidad vendida: "))
    precio_unitario = obtener_precio_unitario(nombre)
    if precio_unitario is None:
        print(f"No se encontró el producto '{nombre}' en la lista de productos.")
        frenar_flujo()
    else:
        ventas.append({"nombre": nombre, "precio": precio_unitario, "cantidad": cantidad})
        print(f"Venta de '{nombre}' agregada correctamente.")
        frenar_flujo()

def eliminar_venta(): # El usuario podrá eliminar una venta de la lista.
    lista_ventas()
    if ventas:
        try:
            opcion = int(input("Ingrese el numero del producto a eliminar (0 para cancelar): "))
            if 1 <= opcion <= len(ventas):
                venta_eliminada = ventas.pop(opcion - 1)
                print(f"Venta de '{venta_eliminada['nombre']}' eliminada correctamente.")
                frenar_flujo()
            elif opcion == 0:
                return
            else:
                print("¡OPCIÓN INVALIDA!")
                frenar_flujo()
        except ValueError as e:
            print(Fore.LIGHTRED_EX + "¡ERROR: ",e,"!")
            frenar_flujo()
    else:
        print(Fore.LIGHTRED_EX+"No hay ventas para eliminar")
        frenar_flujo()

def editar_venta(): # El usuario podrá editar una venta de la lista.
    lista_ventas()
    if ventas:
        try:
            opcion = int(input("Ingrese el numero de la venta a editar (0 para cancelar): "))
            if 1 <= opcion <= len(ventas):
                venta = ventas[opcion -1]
                print(f"Editando venta... {venta['nombre']}")
                nombre = input("Ingrese un nuevo nombre(Dejar vacio para mantener): ").lower()
                if nombre.strip():
                    venta['nombre'] = nombre
                cantidad = input("Ingrese nueva cantidad vendida(Dejar vacio para mantener): ")
                if cantidad.strip():
                    venta['cantidad'] = int(cantidad)
                print(f"Venta de '{venta['nombre']}' editada correctamente ;)")
                frenar_flujo()
            elif opcion == 0:
                return
            else:
                print("¡OPCIÓN INVALIDA!")
                frenar_flujo()
        except ValueError as e:
            print(Fore.LIGHTRED_EX + "¡ERROR: ",e,"!")
            frenar_flujo()

################################################################################################## PRINCIPAL

def frenar_flujo(): # Funcion para detener el flujo del programa, habilita que el usuario pueda ver los mensajes de errores o si las operaciones fueron exitosas.
    input(Fore.YELLOW+"\nPresiona Enter para continuar..."+Fore.RESET)

def limpiar_consola(): # Comando para limpiar la consola
    os.system("cls")

def logo(): # Logo de menu principal (UN INTENTO DE FLOR)
    limpiar_consola()
    print(Fore.LIGHTMAGENTA_EX+" ▄▀▀▀▀▀▀▀▄  ")
    print(Fore.LIGHTMAGENTA_EX+"▐",Fore.LIGHTRED_EX+"▄█▀▀▀█▄",Fore.LIGHTMAGENTA_EX+"▌")
    print("▐",Fore.LIGHTRED_EX+"██   ██",Fore.LIGHTMAGENTA_EX+"▌")
    print("▐",Fore.LIGHTRED_EX+"▀█▄▄▄█▀",Fore.LIGHTMAGENTA_EX+"▌")
    print(" ▀▄▄▄▄▄▄▄▀  ")
    print(Fore.GREEN+"   █████    ")
    print("    ▐█▌▄▄▀▌ ")
    print("▐▀▄▄▐█▌█▄▄▀ ")
    print(" ▀▄▄███     ")
    print("    ▐█▌     ")

def despedida(): # Logo de despedida.
    print("      ▄▀▀▀▀▀▀▀▄       ")
    print("     ▐ ▄█▀▀▀█▄ ▌      ")
    print("     ▐ ▀█▄▄▄█▀ ▌      ")
    print("      ▀▄▄▄▄▄▄▄▀       ")
    print("     ▐▀▄▄▐█▌▄▄▀▌      ")
    print("      ▀▄▄███▄▄▀       ")
    print("-GRACIAS POR PASARTE-")

def Menu_principal(): # Interfaz en consola del programa.
    limpiar_consola()
    logo()
    print("" + Fore.LIGHTGREEN_EX)
    print("1| Ver productos")
    print("")
    print("2| Agregar un producto")
    print("3| Eliminar productos")
    print("4| Editar productos")
    print("")
    print("5| Ver ventas")
    print("")
    print("6| Agregar venta")
    print("7| Eliminar una venta")
    print("8| Editar ventas")
    print("")
    print("9| Salir")

def main(): # Función principal del programa, un "Supermercado" donde se podra ver lista de los productos, agregar, eliminar y editar.
    while True:
        try:
            Menu_principal()
            eleccion = int(input("ELIJA UNA OPCION: "))
            if eleccion <= 0 or eleccion >= 10:
                print(Fore.LIGHTRED_EX + "¡ERROR! ESCOGE UN NUMERO VALIDO")
                frenar_flujo()
            elif eleccion == 1:
                lista_productos()
                frenar_flujo()
            elif eleccion == 2:
                agregar_producto()
            elif eleccion == 3:
                eliminar_producto()
            elif eleccion == 4:
                editar_producto()
            elif eleccion == 5:
                lista_ventas()
                calcular_total_vendidos()
                frenar_flujo()
            elif eleccion == 6:
                agregar_venta()
            elif eleccion == 7:
                eliminar_venta()
            elif eleccion == 8:
                editar_venta()
            elif eleccion == 9:
                despedida()
                return False
            else:
                print("¡ERROR! ESCOGE UN NUMERO VALIDO")
        except ValueError as e:
            print("ERROR:", e)
            frenar_flujo()
main()
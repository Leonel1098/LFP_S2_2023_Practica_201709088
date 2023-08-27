def cargar_inv():
    global inventario
    print("Carga del inventario inicial")
    archivo = input("Ingrese la ruta del archivo: ")

    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()
        
        inventario = []

        for linea in lineas:
            instruccion, datos = linea.strip().split(' ', 1)
            if instruccion == 'crear_producto':
                nombre, cantidad, precio_unitario, ubicacion = datos.split(';')
                producto = {
                    'nombre': nombre,
                    'cantidad': float(cantidad),
                    'precio unitario': float(precio_unitario),
                    'ubicacion': ubicacion
                }
                inventario.append(producto)
        
        print("\nInventario cargado con éxito!")
        print("")
        
        for producto in inventario:
            print(f"Producto:  {producto['nombre']}")
            print(f"Cantidad:  {producto['cantidad']}")
            print(f"Precio Unitario : {producto['precio unitario']}")
            print(f"Ubicacion: {producto['ubicacion']}\n")
    except FileNotFoundError:
        print("El archivo especificado no existe ")
    except FileExistsError as e:
        print("Ocurrió un error al cargar el inventario ", str(e))


def cargar_instrucciones():
    global inventario
    print("Carga las instrucciones de movimiento")
    archivo = input("Ingrese la ruta del archivo: ")

    errores = False

    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()

        for linea in lineas:
            instruccion, datos = linea.strip().split(' ', 1)
            if instruccion == 'agregar_stock':
                nombre, cantidad, ubicacion = datos.split(';')
                
                producto_encontrado = False
                for producto in inventario:
                    if producto['nombre'] == nombre and producto['ubicacion'] == ubicacion:
                        producto_encontrado = True
                        producto['cantidad'] += float(cantidad)
                        break
                
                if not producto_encontrado:
                    print("")
                    print(f"Error: El producto '{nombre}' no se encuentra en la ubicación '{ubicacion}'")
                    errores = True

            elif instruccion == 'vender_producto':
                nombre, cantidad, ubicacion = datos.split(';')
                producto_encontrado = False
                for producto in inventario:
                    if producto['nombre'] == nombre and producto['ubicacion'] == ubicacion:
                        producto_encontrado = True
                        if producto['cantidad'] >= float(cantidad):
                            producto['cantidad'] -= float(cantidad)
                        else:
                            print("")
                            print(f"Error: No hay suficiente cantidad del producto '{nombre}' en la ubicación '{ubicacion}'")
                            errores = True
                        break
                
                if not producto_encontrado:
                    print("")
                    print(f"Error: El producto '{nombre}' no se encuentra en la ubicación '{ubicacion}'")
                    errores = True
                    
        if not errores:
            print("\n Archivo de Movimientos Cargado Correctamente")
            
    except FileNotFoundError:
        print("El archivo especificado no existe")
    except Exception as e:
        print("Ocurrió un error al cargar las instrucciones:", str(e))

def generar_informe():
    with open("informe.txt", "w") as informe_file:
        informe_file.write("Informe de Inventario:\n")
        informe_file.write("Producto\tCantidad\tPrecio Unitario\tValor Total\tUbicación\n")
        informe_file.write("-" * 70 + "\n")

        for producto in inventario:
            cantidad = producto['cantidad']
            precio_unitario = producto['precio unitario']
            valor_total = cantidad * precio_unitario
            ubicacion = producto['ubicacion']
            
            informe_line = "{:<15} {:<10} ${:<14.2f} ${:<9.2f} {}".format(producto['nombre'], cantidad, precio_unitario, valor_total, ubicacion)
            informe_file.write(informe_line + "\n")

        print("\n¡Informe generado y guardado en 'informe.txt'!")


def menu():
    while True:
        print("")
        print("-------------------------------------------------")
        print("Practica 1 - Lenguajes formales y de programacion")
        print("-------------------------------------------------")
        print("# Sistema de inventario:")
        print("")
        print("1. Cargar Inventario Inicial")
        print("2. Cargar Instrucciones de movimientos")
        print("3. Crear informe de inventario")
        print("4. Salir")
        opcion = input("Ingrese una opcion: ")
   
        if opcion == "1":
            cargar_inv()
        elif opcion == "2":
            cargar_instrucciones()
        elif opcion == "3":
            generar_informe()
        elif opcion == "4":
            print("Saliendo del programa, vuelve pronto")
            break
        else:
            print("Indique una opción válida")

menu()
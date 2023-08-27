from tkinter import Tk
from tkinter import filedialog
from Producto_Data import Producto_Data

manejar_productos = Producto_Data()



root = Tk()
root.withdraw()

def CargarInstrucciones():
    root.attributes("-topmost", True)
    #Abre Ventana para Buscar el archivo
    archivo = filedialog.askopenfilename()
    
    
    if archivo:
        print("Archivo seleccionado:", archivo)
        print("")
        global array_chars
        array_chars = []
        archivo_texto = open(archivo, "r+", encoding = "utf8")
        

        for line in archivo_texto.readlines():
            instruccion, datos = line.strip().split(' ', 1)
            if instruccion == 'crear_producto':
                nombre, cantidad, precio_unitario, ubicacion = datos.split(';')
                producto = {
                    'nombre': nombre,
                    'cantidad': float(cantidad),
                    'precio unitario': float(precio_unitario),
                    'ubicacion': ubicacion}
                array_chars.append(producto)

        for producto in array_chars:
            print(f"Producto:  {producto['nombre']}")
            print(f"Cantidad:  {producto['cantidad']}")
            print(f"Precio Unitario : {producto['precio unitario']}")
            print(f"Ubicacion: {producto['ubicacion']}\n")
       
       
        
    else:
        print("")
        print("No se seleccionó ningún archivo.")


def CargarMovimientos():
    global array_chars
    array_chars = []
    root.attributes("-topmost", True)
    #Abre Ventana para Buscar el archivo
    
    errores = False

    try:
        archivo = filedialog.askopenfilename()
        print("Archivo seleccionado:", archivo)
        print("")
        archivo_texto = open(archivo, "r+", encoding = "utf8")
        lineas = archivo_texto.readlines()

        #global array_chars
        #array_chars = []

        for line in lineas:
            instruccion, datos = line.strip().split(' ', 1)
            if instruccion == 'agregar_stock':
                nombre, cantidad, ubicacion = datos.split(';')
                producto_encontrado = False
                for producto in array_chars:
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
                for producto in array_chars:
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
            print("\nArchivo de Movimientos Cargado Correctamente")
            
    except FileNotFoundError:
        print("El archivo especificado no existe")
    except Exception as e:
        print("Ocurrió un error al cargar las instrucciones:", str(e))
     


def Abrir_Txt():
    with open("Resultado.txt","w", encoding= "utf8") as archivo_txt:
        archivo_txt.write("Informe de Inventario: \n"
                        "Producto       " "  Cantidad         "  
                        "Precio Unitario          "  "Valor Toral          "  "Ubicación \n")
        
        for producto in array_chars:
            cantidad = producto['cantidad']
            precio_unitario = producto['precio unitario']
            valor_total = cantidad * precio_unitario
            ubicacion = producto['ubicacion']
            
            archivo_data = "{:<15} {:<10} ${:<14.2f} ${:<9.2f} {}".format(producto['nombre'], cantidad, precio_unitario, valor_total, ubicacion)
            archivo_txt.write(archivo_data + "\n")

        print("Archivo Resultado.txt Creado Correctamente")

def Menu(): 
    while True:
        print("")
        print("------------------------------------------------------")
        print("Practica 1 Lenguajes Formales y de Programación")
        print("------------------------------------------------------")
        print("")
        print(">->->->->->->->SISTEMA DE INVENTARIO<-<-<-<-<-<-<-<")
        print("")
        print(" 1. Cargar Inventario Inicial")
        print(" 2. Cargar Instrucciones de Movimietos")
        print(" 3. Crear informe de Inventario")
        print(" 4. Salir")
        print("")
        print("-------------------------------------------------------")
        # Solicituamos una opción al usuario
        opcionMenu = input(" Por favor seleccione una opcion >> ")
        
        if opcionMenu =="1":
           print("---->Cargar Inventario Inicial")
           print("")
           CargarInstrucciones()
           print("")
          
           

        elif opcionMenu =="2":
            print("---->Cargar Instrucciones de Movimientos")
            print("")
            CargarMovimientos()
            print("")
            
            
            
        elif opcionMenu =="3":
            print("----->Crear Informe de Inventario")
            print("")
            Abrir_Txt()
            print("")
            
        elif opcionMenu =="4":
            print("")
            print(" Adiós :)")
            break

        else:
                print ("")
                input("No has pulsado ninguna opción correcta...\n Pulsa una tecla para continuar")





#RecorrerArchivo()
Menu()

"""""   
        global Data
        Data = array_chars
        #print(Data)
        print("")
        print("Carga Exitosa")
        print("")"""
   
"""""   
def NuevoProducto():
        for productos in Data:
            instruccion = productos[0]
            nombre = productos[1]
            cantidad = productos[2]
            precio_unitario = productos[3]
            ubicacion = productos[4]
            manejar_productos.Nuevo_Producto(instruccion,nombre,cantidad,precio_unitario,ubicacion)
    
def VisualizarProducto():
    manejar_productos.Ver_Productos()
  
"""
###def load_file():
"""""
    try:
        Tk().withdraw()
        filename = filedialog.askopenfilename()
        input_file = open(filename, 'r+', encoding='utf-8')
    except:
        print('Error al cargar el archivo')
    else:
        array_chars = []

        for line in input_file.readlines():
            for char in line.strip():
                array_chars.append(char)
                

        print(array_chars)###
        

#def RecorrerArchivo():
    #nombre_archivo = Data
    #for linea in Data.readlines():
            # Procesa cada línea aquí
            #linea = linea.strip()  # Elimina los caracteres de nueva línea al final de la línea
            #print(linea)  # Por ejemplo, puedes imprimir la línea o realizar otra operación
            """
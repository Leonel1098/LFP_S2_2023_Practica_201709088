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
        archivo_texto = open(archivo, "r+", encoding = "utf8")
        array_chars = []
        for line in archivo_texto.readlines():
            
            for char in line.replace(" ",";").split(";"):
                array_chars.append(char) 
        print(array_chars)

        global Data
        Data = array_chars
        #print(Data)
        print("")
        print("Carga Exitosa")
        print("")
        
    else:
        print("")
        print("No se seleccionó ningún archivo.")

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

def Abrir_Txt():
    with open("Resultado.txt","w", encoding= "utf8") as archivo_txt:
        archivo_txt.write("Informe de Inventario: \n"
                        "Producto       " "  Cantidad         "  
                        "Precio Unitario          "  "Valor Toral          "  "Ubicación \n")
        for item in Data:
                archivo_txt.write(str(item))
    print("Archivo Creado Correctamente")

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
            CargarInstrucciones()
            print("")
            
            
            
        elif opcionMenu =="3":
            print("----->Crear Informe de Inventario")
            print("*********************")
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

    
   
    
    
  
"""
###def load_file():
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
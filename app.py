import tkinter as tk
from tkinter import Tk
from tkinter import filedialog

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
           CargarInventario()
           

        elif opcionMenu =="2":
            print("---->Cargar Instrucciones de Movimientos")
            CargarInstrucciones()
            print("")
            
            
        elif opcionMenu =="3":
            print("----->Crear Informe de Inventario")
           
            print("")
            
        elif opcionMenu =="4":
            print("Adiós Goku ")
            break

        else:
                    print ("")
                    input("No has pulsado ninguna opción correcta...\n Pulsa una tecla para continuar")


root = Tk()
root.withdraw()
def CargarInventario():
    root.attributes("-topmost", True)
    #Abre Ventana para Buscar el archivo
    archivo = filedialog.askopenfilename()
    
    
    if archivo:
        print("Archivo seleccionado:", archivo)
        print("")
        archivo_texto = open(archivo, "r", encoding = "utf8")
        texto = archivo_texto.read()
        archivo_texto.close()
        
        global Data
        Data = texto
        print(Data)
        print("Carga Exitosa")
    else:
        print("")
        print("No se seleccionó ningún archivo.")

def CargarInstrucciones():
     CargarInventario()

Menu()

    
   
    
    
  

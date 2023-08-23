from    Producto import Producto

class Producto_Data:
    
    def __init__(self):
        self.productos = []
        self.contador_productos = 0
    
    def Nuevo_Producto(self,instruccion,nombre,cantidad,precio_unitario,ubicacion):
        for producto in self.productos:
            if producto.nombre == nombre:
                print("Error, nombre existente")
                return False
        nuevo_product = Producto(instruccion,nombre,cantidad,precio_unitario,ubicacion)
        self.productos.append(nuevo_product)
        self.contador_productos +=1 
        print(nuevo_product)
        print("Se agregó un nuevo Producto")
        return True
    
    def Ver_Productos(self):
        print("")
        print("******************")
        print("")
        for producto in self.productos:
            print("Instrucción ", producto.instruccion, "Nombre:", producto.nombre,"Cantidad:", producto.cantidad, 
                  "precio_unitario:", producto.precio_unitario, "Ubicación:" ,producto.ubicacion)
            print("********************")
    
    """def Devolver_Cantidad_Producto(self,nombre):
        #Recorrer la lista
        for producto in self.productos:
            # Encontrar una coincidencia
            if producto.nombre == nombre:
                #Devolver el paciente encontrado
                return producto.cantidad
       """ 






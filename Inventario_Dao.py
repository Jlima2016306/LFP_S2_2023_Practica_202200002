from Inventario import Inventario

class Inventario_Dao:
    def __init__(self):
        self.invetarios=[]
        self.contador_Productos=0

    def crear_producto(self,nombre,cantidad,precioUnitario,ubicacion):
        for producto in self.invetarios:
            if producto.nombre == nombre and producto.ubicacion == ubicacion:
                print("Error, producto repetido")
                return False
        nuevo_producto = Inventario(nombre,float(cantidad),precioUnitario,ubicacion)
        self.invetarios.append(nuevo_producto)
        print("Se agrego un nuevo producto")
        return  True    
    
    def agregar_stock(self,nombre,cantidad,ubicacion):
        for inventory in self.invetarios:
            if inventory.ubicacion == ubicacion:
                if inventory.nombre == nombre:
                    
                    inventory.cantidad += int(cantidad)
                    print("Se agrego con exito")
                    return True
                else:
                    print("No se encontro ese producto en esa bodega")
                    
                    return False
    
    def vender_stock(self,nombre,cantidad,ubicacion):
        for inventory in self.invetarios:
            if inventory.ubicacion == ubicacion:
                if inventory.nombre == nombre:
                    
                    if inventory.cantidad > int(cantidad):
                    
                        inventory.cantidad -= int(cantidad)
                        print("Se Vendio con exito")
                        return True
                    elif inventory.cantidad < int(cantidad):
                        print("No hay suficiente en stock")
                        return False

                else:
                    print("No se encontro ese producto en esa bodega")
                    
                    return False
                

    def guardar_inventario_en_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'w') as archivo:
                archivo.write("Informe de Inventario:\n")
                archivo.write("{:<15} {:<10} {:<15} {:<15} {}\n".format(
                    "Producto", "Cantidad", "Precio Unitario", "Valor Total", "Ubicacion"))
                archivo.write("-" * 70 + "\n")
                
                for producto in self.invetarios:
                    valor_total = float(producto.cantidad) * float(producto.precioUnitario)
                    linea = "{:<15} {:<10} ${:<15} ${:<15} {}\n".format(
                        producto.nombre, str(producto.cantidad), str(producto.precioUnitario), str(valor_total), producto.ubicacion)
                    archivo.write(linea)
            print("Inventario guardado exitosamente en el archivo.")
        except Exception as e:
           
            print("Ocurrió un error al guardar el inventario:", str(e))

    def visualizar_stock(self):
        print("")
        print("")
        print("=============================")
        for Stock in self.invetarios:
            print("Nombre:",Stock.nombre,"Precio:",Stock.precioUnitario,"Cantidad:",Stock.cantidad ,"Ubicación:",Stock.ubicacion)
        print("=============================")
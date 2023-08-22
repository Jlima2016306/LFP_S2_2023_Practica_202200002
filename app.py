from Inventario_Dao import Inventario_Dao
import tkinter as tk
from cargador import cargador




manejador_Inventario = Inventario_Dao()

def registrar_Producto():

    



    def cargar_inventario(archivo):
        with open(archivo, 'r') as f:
            lineas = f.readlines()

        for linea in lineas:
            instruccion, params = linea.strip().split(' ', 1)
            if instruccion == 'crear_producto':
                nombre, cantidad, precio_unitario, ubicacion = params.split(';')
                manejador_Inventario.crear_producto(nombre, cantidad, precio_unitario, ubicacion)
                    

    if __name__ == "__main__":
        root = tk.Tk()
        app = cargador(root)
        comida = app.select_file()
      
        cargar_inventario(comida)    

def agregar_Stock():
    def cargar_Stock(archivo):
        with open(archivo, 'r') as f:
            lineas = f.readlines()

        for linea in lineas:
            instruccion, params = linea.strip().split(' ', 1)
            if instruccion == 'agregar_stock':
                nombre, cantidad, ubicacion = params.split(';')
                manejador_Inventario.agregar_stock(nombre, cantidad, ubicacion)
            if instruccion == 'vender_producto':
                nombre, cantidad, ubicacion = params.split(';')
                manejador_Inventario.vender_stock(nombre, cantidad, ubicacion)                    

    if __name__ == "__main__":
        root = tk.Tk()
        app = cargador(root)
        comida2 = app.select_file_Mov()
      
        cargar_Stock(comida2)   


def ver_Inventario():
    manejador_Inventario.visualizar_stock()

def crear_archivo():
    print("")
    manejador_Inventario.guardar_inventario_en_archivo("ArchivoInventario.txt")

def mostrar_menu():
    print("")
    print("")
    print("-------Menú-----------")
    print("1. Cargar inventario Inicial")
    print("2. Cargar Instrucciones de Movimiento ")
    print("3. Crear informe de Inventario")
    print("4. ver Inventario")
    print("5. salir")
    opcion=input("Ingrese una opción del menú: ")
    while True:
        if opcion=="1":
            registrar_Producto()
        elif opcion=="2":
            agregar_Stock()
        elif opcion=="4":
            ver_Inventario()
        elif opcion=="3":
            crear_archivo()
        elif opcion=="5":
            print("Saliendo del programa, vuevla pronto")
            exit()
            break
        else:
            print("Indique una opción válida")
        mostrar_menu()
            

mostrar_menu()

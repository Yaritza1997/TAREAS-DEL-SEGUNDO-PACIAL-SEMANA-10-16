import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: El ID del producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
            self.guardar_en_archivo()
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

    def guardar_en_archivo(self):
        with open("inventario.json", "w") as archivo:
            json.dump({id: prod.to_dict() for id, prod in self.productos.items()}, archivo)

    def cargar_desde_archivo(self):
        try:
            with open("inventario.json", "r") as archivo:
                datos = json.load(archivo)
                self.productos = {id: Producto(**prod) for id, prod in datos.items()}
        except FileNotFoundError:
            self.productos = {}

# Menú Interactivo
def menu():
    inventario = Inventario()
    while True:
        print("\n1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                print(f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
            else:
                print("Producto no encontrado.")
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

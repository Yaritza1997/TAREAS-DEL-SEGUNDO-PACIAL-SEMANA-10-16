import pickle

class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_info(self):
        return f"ID: {self.producto_id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.producto_id not in self.productos:
            self.productos[producto.producto_id] = producto
        else:
            print("Producto con este ID ya existe.")

    def eliminar_producto(self, producto_id):
        if producto_id in self.productos:
            del self.productos[producto_id]
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, producto_id, nueva_cantidad=None, nuevo_precio=None):
        if producto_id in self.productos:
            producto = self.productos[producto_id]
            if nueva_cantidad:
                producto.actualizar_cantidad(nueva_cantidad)
            if nuevo_precio:
                producto.actualizar_precio(nuevo_precio)
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [producto.obtener_info() for producto in self.productos.values() if nombre.lower() in producto.nombre.lower()]
        return resultados

    def mostrar_inventario(self):
        return [producto.obtener_info() for producto in self.productos.values()]

def guardar_inventario(inventario, archivo):
    with open(archivo, 'wb') as f:
        pickle.dump(inventario.productos, f)

def cargar_inventario(archivo):
    try:
        with open(archivo, 'rb') as f:
            productos = pickle.load(f)
            inventario = Inventario()
            for prod_id, prod_data in productos.items():
                inventario.añadir_producto(Producto(prod_id, prod_data['nombre'], prod_data['cantidad'], prod_data['precio']))
            return inventario
    except FileNotFoundError:
        return Inventario()

def menu():
    inventario = cargar_inventario("inventario.pkl")
    while True:
        print("\n1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opción = input("Seleccione una opción: ")

        if opción == '1':
            producto_id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(producto_id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            guardar_inventario(inventario, "inventario.pkl")

        elif opción == '2':
            producto_id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(producto_id)
            guardar_inventario(inventario, "inventario.pkl")

        elif opción == '3':
            producto_id = input("ID del producto a actualizar: ")
            nueva_cantidad = int(input("Nueva cantidad: "))
            nuevo_precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(producto_id, nueva_cantidad, nuevo_precio)
            guardar_inventario(inventario, "inventario.pkl")

        elif opción == '4':
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            for resultado in resultados:
                print(resultado)

        elif opción == '5':
            productos = inventario.mostrar_inventario()
            for producto in productos:
                print(producto)

        elif opción == '6':
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()

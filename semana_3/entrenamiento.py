import time  # Importa el módulo time para pausar la ejecución con time.sleep()

# Diccionario que actuará como la base de datos temporal del inventario
inventario = {}

# Función que se ejecuta cuando se intenta consultar, actualizar o eliminar un producto inexistente
def producto_inexistente():
    print("❌ Ese producto no está en el inventario.")
    time.sleep(1)
    crear = input("¿Desea crearlo? (si/no): ").lower().strip()  # Se pregunta al usuario si desea crear el producto
    if crear == "si":
        entrada_datos()  # Si responde afirmativamente, se llama a la función que permite agregar productos
    else:
        print("🔙 Volviendo al menú principal...")
        time.sleep(1)

# Función para ingresar nuevos productos al inventario
def entrada_datos():
    producto = input("📦 Nombre del producto: ").lower().strip()  # Solicita el nombre del producto

    if producto in inventario:
        print("⚠️ Ese producto ya existe.")  # Verifica si ya está registrado
    else:
        # Solicita los datos del producto si no existe
        cantidad = float(input("🔢 Cantidad: "))
        precio = float(input("💰 Precio por unidad: "))
        # Guarda el producto en el inventario con su cantidad y precio
        inventario[producto] = {"cantidad": cantidad, "precio": precio}
        print("✅ Producto agregado.")
        time.sleep(1)

# Función para consultar la existencia y datos de un producto
def consulta():
    consulta = input("🔎 Nombre del producto a consultar: ").lower().strip()  # Solicita el nombre

    if consulta in inventario:
        datos = inventario[consulta]
        # Muestra la cantidad y precio del producto si existe
        print(f"📌 '{consulta}' → {datos['cantidad']} unidades • ${datos['precio']} c/u")
    else:
        producto_inexistente()  # Si no existe, se ofrece crearlo

# Función para actualizar el precio de un producto existente
def actualizar_precio():
    producto = input("✏️ Nombre del producto a actualizar: ").lower().strip()

    if producto in inventario:
        datos = inventario[producto]
        print(f"💡 Precio actual: ${datos['precio']}")  # Muestra el precio actual
        nuevo_precio = float(input("🔁 Nuevo precio: "))  # Solicita el nuevo precio
        datos['precio'] = nuevo_precio  # Actualiza el precio
        print("✅ Precio actualizado.")
        time.sleep(1)
    else:
        producto_inexistente()

# Función para eliminar un producto del inventario
def eliminar_producto():
    print("⚠️ Eliminar producto")
    time.sleep(1)
    eleccion = input("¿Seguro que desea eliminarlo? (si/no): ").lower().strip()

    if eleccion == "si":
        producto = input("❌ Nombre del producto: ").lower().strip()
        if producto in inventario:
            del inventario[producto]  # Elimina el producto del diccionario
            print("🗑️ Producto eliminado.")
            time.sleep(1)
        else:
            print("⚠️ Producto no encontrado.")  # Si no se encuentra, informa al usuario
            time.sleep(1)
    else:
        print("🔙 Cancelado. Volviendo al menú...")
        time.sleep(1)

# Función que calcula el valor total del inventario
def calcular_valor_total():
    if not inventario:
        print("📭 Inventario vacío.")  # Si no hay productos, informa
        return

    print("🧮 Calculando total del inventario...")
    time.sleep(1.5)

    # Usa una función lambda con map para calcular la suma del valor de todos los productos
    total = sum(
        map(lambda datos: datos["cantidad"] * datos["precio"], inventario.values())
    )

    # Muestra el valor total del inventario
    print(f"💰 Valor total: ${total:.2f}")
    time.sleep(1.5)

# Función principal que muestra el menú y gestiona la navegación del sistema
def main():
    while True:
        # Muestra las opciones disponibles del menú
        print("\n📋 MENÚ PRINCIPAL - Tienda La Esperanza 🛒")
        print("1️⃣ Agregar producto")
        print("2️⃣ Consultar producto")
        print("3️⃣ Actualizar precio")
        print("4️⃣ Eliminar producto")
        print("5️⃣ Calcular valor total")
        print("6️⃣ Salir")

        opcion = input("👉 Ingrese una opción (1-6): ").strip()

        # Diccionario que simula un switch-case asociando cada opción con su función correspondiente
        opciones = {
            "1": entrada_datos,
            "2": consulta,
            "3": actualizar_precio,
            "4": eliminar_producto,
            "5": calcular_valor_total,
            "6": lambda: print("👋 Saliendo del sistema... Hasta pronto!")  # Mensaje final al salir
        }

        if opcion in opciones:
            if opcion == "6":
                opciones[opcion]()  # Muestra mensaje de salida
                break  # Sale del bucle principal
            else:
                opciones[opcion]()  # Ejecuta la función correspondiente a la opción
        else:
            print("❗ Opción inválida. Intente de nuevo.")
            time.sleep(1.5)

# Punto de entrada del programa: se ejecuta cuando se corre este archivo directamente
if __name__ == "__main__":
    main()

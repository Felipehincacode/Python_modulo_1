#simulacro
biblioteca = {  
    "libros" :  []
}

generos_validos = ["religion","ciencia","ficcion", "niños", "avenutas"]

def agregar_libros():
    titulo = input("ingrese el nombre del libro")

    copias_disponibles = int(input("ingrese la cantidad de copias disponibles"))
    while True:
        genero = input("¿Cúal es el género de su libro").lower().strip()
        if genero not in generos_validos:
            print("por favor ingrese un genero válido")
        else: 
            print("perfecto, ese genero es una categoría válida")
            break
        
    creacion_libros = biblioteca["libros"]
    nuevo_libro = {"titulo":titulo , "copias_disponibles":copias_disponibles,"copias_totales":copias_disponibles, "genero":genero}
    creacion_libros.append(nuevo_libro)
    print(f"su libro {nuevo_libro} ha sido guardado con exito")

def buscar_por_titulo():
    query = input("ingrese el nombre del libro").lower().strip()
    busqueda_libros = biblioteca["libros"]
    for i in busqueda_libros:
         if query.lower().strip() == i["titulo"].lower().strip():
            print(f" el libro está en nuestro inventario tenemos  {i["copias_disponibles"]} copias disponibles")
            return
    print("ese libro no lo tenemos en nuestra biblioteca")

def prestar_libros():
    query = input("ingrese el titulo del libro que desea prestar")
    busqueda_libros = biblioteca["libros"]
    for i in busqueda_libros:
         if query.lower().strip() == i["titulo"].lower().strip():
            print(f" el libro está en nuestro inventario tenemos  {i["copias_disponibles"]} copias disponibles")
            if i ["copias_disponibles"] == 0:
                print("el libro que buscas no tiene copias disponibles")
                return
            else:
                i["copias_disponibles"] -= 1
                print(f"Su libro ha sido prestado con exito, en nuestro sistema quedan: {i["copias_disponibles"]} copias disponibles")
                return

    print("ese libro no lo tenemos en nuestra biblioteca")



def devolver_libros():
    query = input("ingrese el titulo del libro que desea devolver")
    busqueda_libros = biblioteca["libros"]
    for i in busqueda_libros:
         if query.lower().strip() == i["titulo"].lower().strip():
            i["copias_disponibles"] += 1
            print(f"Su libro ha sido devuelto con exito, en nuestro sistema quedan: {i["copias_disponibles"]} copias disponibles")
            return

    print("ese libro no lo tenemos en nuestra biblioteca")

def eliminar_libros():
    query = input("ingrese el titulo del libro que desea eliminar del sistema")
    busqueda_libros = biblioteca["libros"]
    for i in busqueda_libros:
         if query.lower().strip() == i["titulo"].lower().strip():
            if i["copias_disponibles"] == i["copias_totales"]:
                busqueda_libros.remove(i)
                print("el libro ha sido eliminado con exito")
                return
            else:
                print("no es posible borrar ese libro, porqué aún hay copias prestadas")
                return
    print("ese libro no lo tenemos en nuestra biblioteca")


def listar_libros_por_genero():
    while True:
        query = input("que genero literio desea leer").lower().strip()
        if query not in generos_validos:
            print("por favor ingrese un genero válido")
            
        else: 
            print("perfecto, ese genero es una categoría válida")
            break

    
    busqueda = biblioteca["libros"]
    for i in busqueda:
        if i["genero"] == query:
            print(i["titulo"])

def imprimir_inventario():
    inventario = biblioteca["libros"]
    print(inventario.items())

def main():
    while True: # El bucle que mantiene el menú activo
        print("\n--- Sistema de Gestión de Biblioteca ---")
        print("1. Agregar Libro")
        print("2. Buscar Libro por Título")
        print("3. Prestar Libro")
        print("4. Devolver Libro")
        print("5. Eliminar Libro")
        print("6. Listar Libros por Género")
        print("7. Salir") # Opción para terminar el programa

        opcion = input("Ingrese el número de su opción: ").strip() # Leer la opción del usuario

        if opcion == "1":
            agregar_libros()
        elif opcion == "2":
            buscar_por_titulo()
        elif opcion == "3":
            prestar_libros()
        elif opcion == "4":
            devolver_libros()
        elif opcion == "5":
            eliminar_libros()
        elif opcion == "6":
            listar_libros_por_genero()
        elif opcion == "7":
            print("¡Hasta luego!")
            break # Rompe el bucle while y termina la ejecución de la función main()
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

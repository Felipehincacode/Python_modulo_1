import time
import random # Se mantiene importado por si es necesario para futuros ejercicios

# --- Descripción de los Ejercicios ---
# Este script contiene funciones en Python para realizar operaciones básicas
# con calificaciones numéricas, como parte de un entrenamiento en programación.
# Los ejercicios se enfocan en estructuras condicionales (if, elif, else)
# y bucles (for, while).

# 1. Determinar el estado de aprobación:
#    - Solicitar al usuario ingresar una calificación numérica (0-100).
#    - Evaluar si está aprobada o reprobada.
# 2. Calcular el promedio:
#    - Permitir al usuario ingresar una lista de calificaciones.
#    - Calcular y mostrar el promedio.
# 3. Contar calificaciones mayores que un valor específico:
#    - Solicitar un valor numérico de comparación.
#    - Contar y mostrar cuántas calificaciones en la lista son mayores que ese valor.
# 4. Verificar y contar calificaciones específicas:
#    - Permitir al usuario ingresar una lista de calificaciones y una calificación específica.
#    - Contar y mostrar cuántas veces aparece dicha calificación.

# --- Funciones para cada Ejercicio (Consola) ---

# Función 1: Verificar estado de aprobación de una nota individual
def verificar_estado_aprobacion():
    """
    Solicita al usuario una calificación numérica (0-100), valida el rango
    y determina si la calificación está aprobada o reprobada.
    """
    print("\n✨ --- Verificar Estado de Aprobación --- ✨")

    while True:
        try:
            # Solicitar la calificación al usuario
            calificacion_str = input("😊 Por favor, ingresa la calificación (un número entre 0 y 100): ")

            # Validar si la entrada no está vacía
            if not calificacion_str.strip():
                 print("⚠️ Entrada vacía detectada. Intenta de nuevo.")
                 continue # Volver a pedir la entrada

            calificacion = float(calificacion_str) # Convertir a flotante para permitir decimales

            # Validar que la calificación esté en el rango de 0 a 100
            if 0 <= calificacion <= 100:
                break # Si la calificación es válida, salir del bucle de validación
            else:
                print("🚫 Calificación fuera de rango. Por favor, ingresa un número entre 0 y 100.")

        except ValueError:
            # Manejar el error si la entrada no es un número válido
            print("❌ Entrada no válida. Por favor, ingresa solo un número.")

    # Determinar si aprobó o reprobó (usando 70 como umbral)
    if calificacion >= 70:
        print(f"\n🎉 ¡Excelente! Con {calificacion}, has aprobado la materia. 👍")
    else:
        print(f"\n😞 Con {calificacion}, has reprobado la materia. Ánimo para la próxima. 👎")

    print("--- Fin Verificar Estado ---")
    time.sleep(2) # Pausa para visibilidad del resultado

# Función 2: Calcular el promedio de una lista de notas
def calcular_promedio():
    """
    Permite al usuario ingresar una lista de calificaciones una por una,
    calcula su promedio y lo muestra. Incluye validación y manejo de lista vacía.
    """
    print("\n📊 --- Calculadora de Promedios --- 📊")
    lista_notas = []

    print("📝 Ingresa las notas una por una para calcular el promedio.")
    print("👉 Escribe 'fin' y presiona Enter cuando termines.")

    # Bucle para solicitar y recolectar notas del usuario
    while True:
        entrada_usuario = input("➕ Ingresa una nota (o 'fin' para terminar): ")

        # Condición para salir del bucle de ingreso
        if entrada_usuario.lower() == 'fin':
            print("✅ Ingreso de notas finalizado.")
            time.sleep(1)
            break # Salir del bucle de ingreso

        # Intentar convertir la entrada a número y validar
        try:
            nota = float(entrada_usuario)

            
            if 0 <= nota <= 100:
                 lista_notas.append(nota) # Si es válida, añadir a la lista
                 print(f"✅ Nota {nota} guardada.")
            else:
                 print("⚠️ Nota fuera del rango común (0-100). Esta nota no será añadida.") # Informar al usuario
                 # No añadimos la nota si está fuera del rango

        except ValueError:
            # Manejar el error si la entrada no es un número
            print("❌ Entrada inválida. Por favor, ingresa un número o la palabra 'fin'.")

    # --- Calcular y mostrar el promedio (después del ingreso) ---
    print("\n--- Calculando Promedio ---")

    # Verificar si se ingresó al menos una nota antes de calcular para evitar división por cero
    if lista_notas:
        total_notas = sum(lista_notas) # Suma todos los elementos de la lista
        cantidad_notas = len(lista_notas) # Cuenta cuántos elementos hay

        promedio = total_notas / cantidad_notas # Calcular el promedio

        print(f"🔢 Notas ingresadas: {lista_notas}")
        print(f"📈 Total de notas ingresadas: {cantidad_notas}")
        print(f"✨ ¡El promedio de tus notas es: {promedio:.2f}! ✨") # Mostrar el promedio (formato a 2 decimales)

    else:
        # Mensaje si no se ingresaron notas
        print("😞 No se ingresó ninguna nota válida para calcular el promedio.")

    print("--- Fin Calculadora de Promedios ---")
    time.sleep(2) # Pausa

# Función 3: Contar notas superiores, menores o iguales a un valor dado
def contar_notas_comparacion():
    """
    Permite ingresar una lista de calificaciones, luego un valor de comparación,
    y cuenta cuántas notas en la lista son mayores, menores o iguales a ese valor.
    Incluye validación y manejo de lista vacía.
    """
    print("\n🔢 --- Contador de Notas por Comparación --- 🔢")
    lista_notas = []

    print("📝 Primero, ingresa la lista de notas para comparar.")
    print("👉 Escribe 'fin' y presiona Enter cuando termines.")

    # --- Parte 1: Ingresar la lista de notas ---
    while True:
        entrada_usuario = input("➕ Ingresa una nota (o 'fin' para terminar): ")

        if entrada_usuario.lower() == 'fin':
            print("✅ Ingreso de notas finalizado.")
            time.sleep(1)
            break

        try:
            nota = float(entrada_usuario)

             # Aplicar validación para notas individuales 
            if 0 <= nota <= 100:
                 lista_notas.append(nota)
                 print(f"✅ Nota {nota} guardada.")
            else:
                 print("⚠️ Nota fuera del rango común (0-100). Esta nota no será añadida.")

        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número o la palabra 'fin'.")

    # --- Parte 2: Pedir el valor de comparación (después de tener la lista) ---
    # Verificar si la lista no está vacía antes de pedir el valor de comparación y contar
    if not lista_notas:
        print("\n😞 No se ingresó ninguna nota en la lista. No se puede hacer la comparación.")
        print("--- Fin Contador por Comparación ---")
        time.sleep(2)
        return # Salir de la función si la lista está vacía

    print(f"\n🔢 Lista de notas ingresada: {lista_notas}")
    time.sleep(1)

    # Bucle para pedir y validar el valor de comparación
    while True:
        try:
            nota_comparar_str = input("🤔 Ahora, ingresa el valor de comparación: ")

            if not nota_comparar_str.strip():
                 print("⚠️ Entrada vacía detectada. Intenta de nuevo.")
                 continue

            nota_comparar = float(nota_comparar_str)
            print(f"✅ Valor de comparación {nota_comparar} registrado.")
            time.sleep(1)
            break # Salir del bucle de validación si es válido

        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número válido para comparar.")

    # --- Parte 3: Contar las notas según la comparación ---
    print(f"\n--- Contando notas respecto a {nota_comparar} ---")

    # Inicializar los contadores antes de empezar el bucle de conteo
    contador_mayores = 0
    contador_igual = 0
    contador_menores = 0

    # Recorrer cada nota en la lista y comparar
    for nota in lista_notas:
        if nota > nota_comparar: # Si la nota actual es MAYOR que el valor de comparación
            contador_mayores += 1
        elif nota == nota_comparar: # Si la nota actual es IGUAL que el valor de comparación
            contador_igual += 1
        else: # Si no es mayor ni igual, entonces es MENOR
            contador_menores += 1

    # --- Parte 4: Mostrar el resultado del conteo (una vez al final) ---
    print(f"\nResultados de la comparación con {nota_comparar}:")
    print(f"👉 Notas mayores: {contador_mayores} ⬆️")
    print(f"👉 Notas iguales: {contador_igual} ➡️")
    print(f"👉 Notas menores: {contador_menores} ⬇️")
    print("--- Fin Contador por Comparación ---")
    time.sleep(2) # Pausa

# Función 4: Verificar y contar calificaciones específicas
def contar_calificacion_especifica():
    """
    Permite al usuario ingresar una lista de calificaciones, luego una calificación
    específica a buscar, y cuenta cuántas veces aparece esa calificación en la lista.
    Incluye validación y manejo de lista vacía.
    """
    print("\n🔍 --- Contador de Calificación Específica --- 🔍")
    lista_notas = []

    print("📝 Primero, ingresa la lista de notas para buscar una específica.")
    print("👉 Escribe 'fin' y presiona Enter cuando termines.")

    # --- Parte 1: Ingresar la lista de notas ---
    while True:
        entrada_usuario = input("➕ Ingresa una nota (o 'fin' para terminar): ")

        if entrada_usuario.lower() == 'fin':
            print("✅ Ingreso de notas finalizado.")
            time.sleep(1)
            break

        try:
            nota = float(entrada_usuario)

            # Aplicar validación para notas individuales (ej: rango 0-100)
            if 0 <= nota <= 100:
                 lista_notas.append(nota)
                 print(f"✅ Nota {nota} guardada.")
            else:
                 print("⚠️ Nota fuera del rango común (0-100). Esta nota no será añadida.")

        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número o la palabra 'fin'.")

    # --- Parte 2: Pedir la calificación específica a buscar ---
    if not lista_notas:
        print("\n😞 No se ingresó ninguna nota en la lista. No se puede buscar una calificación específica.")
        print("--- Fin Contador Específico ---")
        time.sleep(2)
        return

    print(f"\n🔢 Lista de notas ingresada: {lista_notas}")
    time.sleep(1)

    # Bucle para pedir y validar la calificación específica a buscar
    while True:
        try:
            calificacion_buscar_str = input("🤔 Ahora, ingresa la calificación exacta que quieres buscar en la lista: ")

            if not calificacion_buscar_str.strip():
                 print("⚠️ Entrada vacía detectada. Intenta de nuevo.")
                 continue

            calificacion_buscar = float(calificacion_buscar_str)
            print(f"✅ Calificación {calificacion_buscar} a buscar registrada.")
            time.sleep(1)
            break # Salir del bucle de validación si es válido

        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número válido para buscar.")

    # --- Parte 3: Contar cuántas veces aparece la calificación específica ---
    print(f"\n--- Buscando {calificacion_buscar} en la lista ---")

    # Usamos el método count() de las listas, es eficiente para esto
    contador_ocurrencias = lista_notas.count(calificacion_buscar)

    # --- Parte 4: Mostrar el resultado ---
    print(f"\n🎉 La calificación {calificacion_buscar} aparece {contador_ocurrencias} vez(ces) en la lista.")
    print("--- Fin Contador Específico ---")
    time.sleep(2) # Pausa


# --- Función del Menú (Consola Gráfica) ---

def mostrar_menu():
    """
    Muestra un menú de opciones en la consola al usuario y solicita su elección.
    Incluye validación para asegurar una elección válida.
    """
    # Creamos un menú más visual con caracteres y emojis
    print("\n" + "═" * 40) # Borde superior
    print("📚✨ ¡Bienvenido a NotasApp! Tu aliado académico ✨📚")
    print("═" * 40)
    print("Por favor, selecciona una opción digitando el número:")
    print("────────────────────────────────────────") # Separador visual
    print(" 1️⃣: Verificar si ganaste o perdiste una materia")
    print(" 2️⃣: Calcular el promedio de tus notas")
    print(" 3️⃣: Contar notas mayores, menores o iguales a un valor")
    print(" 4️⃣: Contar cuántas veces aparece una nota específica")
    print(" 5️⃣: Salir de NotasApp 🚪") # Opción para salir
    print("═" * 40) # Borde inferior

    while True:
        try:
            # Pedimos la elección al usuario
            eleccion_str = input("👉 Ingresa el número de tu opción (1-5): ")

            # Validar si la entrada no está vacía
            if not eleccion_str.strip():
                print("⚠️ Por favor, ingresa un número de opción.")
                continue

            eleccion = int(eleccion_str) # Intentar convertir a entero

            # Validar si la elección está en el rango de opciones (1 a 5)
            if 1 <= eleccion <= 5:
                 return eleccion # Si es válida, devolver la elección y salir del bucle
            else:
                 print("🚫 Opción no válida. Por favor, ingresa un número del 1 al 5.")

        except ValueError:
            # Manejar el error si la entrada no es un número entero
            print("❌ Entrada inválida. Por favor, ingresa el número de la opción.")

# --- Programa Principal (Controla el flujo de la aplicación de consola) ---

# Este bloque se ejecuta automáticamente cuando el script es corrido directamente.
if __name__ == "__main__":
    print("🚀 Iniciando la aplicación NotasApp...")

    # Mapa o diccionario que asocia el número de opción del menú con la función a ejecutar
    # Esto simplifica la lógica de selección de la función.
    mapa_ejercicios = {
        1: verificar_estado_aprobacion,
        2: calcular_promedio,
        3: contar_notas_comparacion, # Renombrada
        4: contar_calificacion_especifica # Nueva función añadida
    }

    # Bucle principal que mantiene la aplicación corriendo hasta que el usuario elija salir
    while True:
        opcion_elegida = mostrar_menu() # Mostrar el menú y obtener la elección validada del usuario

        if opcion_elegida == 5:
            # Si la opción elegida es 'Salir'
            print("\n👋 ¡Gracias por usar NotasApp! Vuelve pronto. 👋")
            time.sleep(2)
            break # Salir del bucle principal para finalizar el programa

        elif opcion_elegida in mapa_ejercicios:
            # Si la opción elegida corresponde a uno de los ejercicios (1, 2, 3 o 4)
            # Obtener la función asociada desde el mapa
            funcion_a_ejecutar = mapa_ejercicios[opcion_elegida]
            # Llamar a la función para ejecutar el ejercicio seleccionado
            funcion_a_ejecutar()

        # Si la opción no fuera 5 y no estuviera en el mapa (lo cual no debería pasar
        # si mostrar_menu valida correctamente), un 'else' aquí podría manejarlo,
        # pero como mostrar_menu() solo devuelve 1-5, no es estrictamente necesario.

    print("✅ Aplicación NotasApp finalizada. ✅")

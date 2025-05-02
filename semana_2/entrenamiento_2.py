import time

'''1. Determinar el estado de aprobación:
a. Solicitar al usuario ingresar una calificación numérica (de 0 a 100).
b. Evaluar si está aprobada o reprobada basándose en la calificación
ingresada.
    2. Calcular el promedio:
    a. Permitir al usuario ingresar una lista de calificaciones (separadas por
    comas).
    b. Calcular y mostrar el promedio de las calificaciones en la lista.
        3. Contar calificaciones mayores que un valor específico:
        a. Solicitar al usuario un valor numérico.
        b. Contar y mostrar cuántas calificaciones en la lista son mayores que ese
        valor.
            4. Verificar y contar calificaciones específicas:
            a. Permitir al usuario ingresar una lista de calificaciones (separadas por
            comas) y una calificación específica.
            b. Contar y mostrar cuántas veces aparece dicha calificación en la lista.
            Instrucciones
            Paso 1: Análisis del problema y list'''

#verificar nota si aprobó o no

def verificacion(): 
       
        
    while True:
        try:
            numero = int(input("Ingrese un número entre 0 y 100 "))
            
            if numero> 100 or numero<0:
                print("por favor un ingrese un número dentro del rango")
                continue 
            else:
                break
        except ValueError: print("Error: Por favor, ingrese solo números enteros. 🚫")

    if numero >= 70:
                print(f"Su nota es {numero} por lo tanto aprobó la materia 👍")
    else:
                print(f"Su nota es {numero} por lo tanto reprobó la materia 👎")
            

    
def promedio():

    lista_notas = []
   
    print("Bienvenido a la calculadora de promedios")
    print("Ingrese las notas que quieras, para terminar de agregar nostas escriba fin ")
    
    while True:
        
        Entrada_usuario = input("Por favor ingrese una nota: ")

        if Entrada_usuario.lower() == 'fin':
            
            print("¡Listo! Has terminado de ingresar notas.")
            time.sleep(1) 
            break
        
        try: 
            nota = float(Entrada_usuario)
            print("Guardando su nota, por favor espere")
            time.sleep(1)

            print(f'Genial la nota: {nota} ha sido guardada exitosamente')
         

            lista_notas.append(nota)

        except ValueError: print("Uy te equivocaste, ingresa un número")

    

    resultado = sum(lista_notas)/len(lista_notas)

    print(f"Usted ingresó {len(lista_notas)} notas.  El promedio de estas notas  es:{resultado}")
    time.sleep(1)
    print(f"El promedio de estas notas  es:{resultado}")



def notas_superior():
         
    lista_notas = []
    contador_positivo = 0
    contador_negativo = 0
    contador_igual = 0
   
    print("Bienvenido al contador de notas superiores")
    print("Ingrese las notas que quieras, el sistema contará que notas son \nmayores para terminar de agregar nostas escriba fin o presione enter")
    
    while True:
        
        Entrada_usuario = input("Por favor ingrese una nota: ")

        if Entrada_usuario.lower() == 'fin':
            
            print("¡Listo! Has terminado de ingresar notas.")
            time.sleep(1) 
            break
        
        try: 
            nota = float(Entrada_usuario)
            print("Guardando su nota, por favor espere")
            time.sleep(1)

            print(f'Genial la nota: {nota} ha sido guardada exitosamente')
         

            lista_notas.append(nota)

        except ValueError: print("Uy te equivocaste, ingresa un número")

    while True:
        
        try:
            Nota_comparar = float(input("Ahora ingresa una nota que quieras comparar con las demás el sistema te dirá, cuantas notas mayores hay, cuantas son menores y cuantas iguales"))
            print(f"Perfecto, ahora el sistema determinará cuantas notas son mayores")
            time.sleep(1)
            break
        except  ValueError:print("Uy te equivocaste, ingresa un número")
        
    for puesto in lista_notas:

        if Nota_comparar< puesto:
                  contador_positivo += 1
        elif Nota_comparar == puesto:
                contador_igual += 1
        else:
                 contador_negativo += 1

    print(f"En comparación a la nota que ingresaste hay: {contador_positivo} notas mayores y {contador_negativo} notas menores y {contador_igual} son iguales")



def switcher():
       
     print("Bienvenido a tu Notica tu aliado en la u")
     print("por favor seleccione una opción según lo que desee de hacer")
     print("Digite el número uno para: ver si ganó o perdió")
     print("Digite el número dos para calcular su promedio")
     print("Digite el número tres para ver que notas ")
     print("Digite el número cuatro para salir ver que notas ")
     eleccion = int(input("ingrese un número segun la opcion que desee"))   
     return eleccion




while True:
    eleccion = switcher()
    if eleccion == 1:
        verificacion()
    elif eleccion == 2:
        promedio()
    elif eleccion == 3:
        notas_superior()
    else:
        break

    
    


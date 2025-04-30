

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
    print("Ingrese las notas que quieras, para terminar de agragar nostas escriba fin o presione entere")
    
    while True:
        
        Entrada_usuario = input("Por favor ingrese una nota")

        if Entrada_usuario.lower() == 'fin':
            
            print("¡Listo! Has terminado de ingresar notas.")
            break
        try: 
            nota = float(Entrada_usuario)
         

            lista_notas.append(nota)

        except ValueError: print("Uy te equivocaste, ingresa un número")

    



print(promedio())

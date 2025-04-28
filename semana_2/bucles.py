"""Ejercicios de Estructuras Condicionales y Bucles en Python Este archivo contiene ejercicios básicos diseñados para principiantes en Python, enfocados en practicar estructuras condicionales (if, elif, else) y bucles (for, while). Los ejercicios están pensados para un repositorio público, con enunciados claros para resolver.

Estructuras Condicionales Ejercicio 1: Clasificador de números Escribe un programa que pida al usuario un número entero y determine si es positivo, negativo o cero.

Ejercicio 2: Aprobado o reprobado Crea un programa que reciba la calificación de un estudiante (0 a 100) e indique si está aprobado (60 o más) o reprobado (menos de 60).

Bucles Ejercicio 3: Tabla de multiplicar Escribe un programa que muestre la tabla de multiplicar de un número ingresado por el usuario (del 1 al 10) usando un bucle for.

Ejercicio 4: Contador regresivo Crea un programa que pida un número positivo al usuario y haga una cuenta regresiva desde ese número hasta 0 usando un bucle while.

Ejercicio Combinado Ejercicio 5: Adivina el número Crea un programa que genere un número aleatorio entre 1 y 10, y le pida al usuario que lo adivine. El programa debe indicar si el número ingresado es mayor, menor o correcto. El usuario tiene hasta 3 intentos.

Instrucciones para el Repositorio

Resuelve los ejercicios: Implementa las soluciones en tu entorno de Python (como IDLE, VS Code o un notebook). Experimenta: Modifica los ejercicios, por ejemplo, cambiando los rangos, mensajes o condiciones. Contribuye: Si tienes ideas para más ejercicios, crea un pull request en el repositorio.



# Ejercicio 1: Clasificador de números

input = int(input("Ingrese un número entero: "))

if input > 0:
    print("El número es positivo.")

elif input < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
    """

# Ejercicio 2: Aprobado o reprobado
try:

    nota = float(input("Ingrese la calificación del estudiante (0 a 100): "))


    if nota> 100 or nota<0:
        print("por favor ingrese un número dentro del rango especificado") 
    elif  0<= nota > 60:
         print("Usted es un vago reprobó la materia")
    else:
         print("Maquina, ganaste la materia")



except ValueError:
        print("Porfavor ingrese un número")

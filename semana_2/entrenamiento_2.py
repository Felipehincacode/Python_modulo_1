
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
            

    

print(verificacion())

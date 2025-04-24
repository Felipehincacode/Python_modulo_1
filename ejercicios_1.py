## 1. Ingreso de datos por consola
  
""""Solicita el nombre y edad del usuario, luego imprime un saludo personalizado que incluya ambos datos.
    Pide al usuario que ingrese su comida favorita y su color favorito, luego imprime una frase con ambos.
    Solicita un número y muestra su doble y su triple."""




print("Bienvenido compañero, queremos darte una atención personalizada por favor indicanos los siguientes datos:")


nombre = input("Por favor ingresa tu nombre")

edad = input("Por favor ingresa tu edad")

print(f"Hola {nombre} tienes la edad de {edad} años")

comida = input("Por favor ingresa tu comida favorita")

color = input("Por favor ingresa tu color favorito")

print(f"tu comida favorita es:{comida} y tu color favorito es:{color}")


num = int(input("para terminar queremos que nos de un número, seremos capaces de mostrarle el doble y hasta el triple"))

print(f"su numero fue:{num} el doble de ese número es {num*2} y el triple de ese número es{num*3}")
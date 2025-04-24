import time #Modulo que contiene la funcion timesleep



#Calculadora de descuentos para la empresa "Tiendas D1"#
#Declaración de variables fijas

Nombre_producto:str=  0
Precio_unitario:float = 0
Cantidad:int = 0
Descuento:float = 0


#Bienvenida

print("-"*71)
print("||★★★★★★★★★★★ Bienvenido al sistema de inventarios del D1 ★★★★★★★★★★★||")
print("-"*71)

time.sleep(3) #tiempo de espera para una mejor lectura

print("-"*71)
print("\nA continuación se le pedirán datos de vital importancia para calcular el costo de los productos comprados\n\npor favor lea con atención y llene los datos con total honestidad  ")
print("-"*71)

time.sleep(3) #tiempo de espera para una mejor lectura

#Entrada de datos

#con modulo para arreglar errores



try:
                    Nombre_producto = input("Por favor ingrese el nombre de producto que comprará: \n ")   
                    
except ValueError:
                    print(" \n Error: ingresó un valor incorrecto o diferente al solicitado  por favor intentelo nuevamente \n")


#ingresa el precio unitario
try:
                    Precio_unitario= float(input("Por favor ingrese el valor unitario del producto \n"))
                    while(Precio_unitario < 0):
                        print ("ERROR: el valor del producto no puede ser negativo")
                        Precio_unitario= float(input("Por favor ingrese el valor unitario del producto \n"))
                    else: (print("Perfecto, vayamos al siguiente paso"))    
except ValueError:
                    print(" \n Error: ingresó un valor incorrecto o diferente al solicitado  por favor intentelo nuevamente \n")
                    Precio_unitario= float(input("Por favor ingrese el valor unitario del producto \n"))

#ingresa la cantidad de productos a comprar

try:
                    Cantidad = int(input("Por favor ingrese la cantidad  que comprará \n"))

                    while(Cantidad < 0):
                     print ("ERROR: el valor del producto no puede ser negativo")
                     Cantidad = int(input("Por favor ingrese un valor positivo para la cantidad \n"))
                    
except ValueError:
                    print(" \n Error: ingresó un valor incorrecto o diferente al solicitado  por favor intentelo nuevamente \n")
                    Cantidad = int(input("Por favor ingrese un valor positivo para la cantidad \n"))



# Ingresa el valor del descuento 
try:
                    Descuento = float(input("si el producto tiene un descuento, indique la cantidad, si no lo tiene escriba el numero 0 \n"))
                    while(Descuento > 100 or Descuento < 0):
                        print ("ERROR: el valor del descuento no puede ser mayor a 100 o negativo")
                        Descuento = float(input("si el producto tiene un descuento, indique la cantidad, si no lo tiene escriba el numero 0 \n"))
                    else:
                         print(" \n Perfecto, nuestro sistema está procesando sus entradas por favor espere")  
                         
                         time.sleep(3)             
                         
except ValueError:
                    print(" \n Error: ingresó un valor incorrecto o diferente al solicitado  por favor intentelo nuevamente \n")
                    Descuento = float(input("si el producto tiene un descuento, indique la cantidad, si no lo tiene escriba el numero 0 \n"))

                
            



precio_con_descuento = (Precio_unitario * Descuento)/100

if( Descuento == 0.0):
    print(f" \n\nEl nombre de su producto es: {Nombre_producto} \n usted adiquirió: {Cantidad} unidades \n el valor total de su compra es: {Precio_unitario*Cantidad} ")
else:
    print(f"\n\n El nombre de su producto es {Nombre_producto} \nS usted adiquirió {Cantidad}  \n el valor total de su compra  aplicando el descuento del {Descuento} % es: {Precio_unitario*Cantidad} ")
1 - Descuento / 100

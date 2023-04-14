import random
#la sentencia ramdom permite importar un módulo que contiene archivos y opciones útiles
def adivina_el_número(x):

    print("====================")
    print( " ¡Bienvenido(a) a mi juego! ")
    print("====================")
    print("Tu meta es adivinar el número generado por la computadora.")
#rand random int entero 
    número_aleatorio = random.randint(1, x) #Número aleatorio entre 1 y x.
     
    predicción = 0
    # el 0 es para gener una cantidad indefinida de interacciones
    
    while predicción != número_aleatorio:
        #El usuario ingresa un número.
        predicción = int(input(f"Adivina un número entre 1 y {x}: ")) #f-string #Permite reemplazar el valor de una variable o una cadena de manera más concisa {x}
        #int permite que el valor se convierta en entero 

        if predicción < número_aleatorio:
             print("Intenta otra vez.Este número es muy pequeño")
        elif predicción > número_aleatorio:
            print("Intenta otra vez . Este número es muy grande.")
    
    print(f"¡Felicitacionesss! Adivinaste el número {número_aleatorio} correctamente")


    adivina_el_número(100)



    

#numeros son valores numericos, no se expresan con "" como string
print(2)
print(2.5)
print(2.45667)

#Puedes convertir valores string a numericos con funcion int
num1 = "23"
print(int(num1))

num2 = "23.4"
print(float(num2))

#suma
print(2+2)

#resta
print (3-2)

#multiplicacion
print(3*4)


#division
print(10/2)

#residuo

print (10 % 3)

#Puedes almacenar numeros en variables

numero_a = 40
numero_b = 50
numero_d1 = 3.567
numero_d2 = 3.3

print(numero_a)
print(numero_a + numero_b)

#funciòn str = convierte un valor numerico en string
print(str(numero_a))

print("Mi numero favorito es " + str(numero_a + numero_b))


#pow: funcion potencia
print(pow(3,3))


#max: devuelve el mayor de la comparacion de dos numeros
print(max(3 , 6))
print(max(numero_a,numero_b))

#min: devuelve el menor de la comparaciòn de dos numeros
print(min(5,1))

#round: redondea a enteros el numero indicad
print(round(5.32))
print(round(numero_d1))
print(round(numero_d2))

#from math import * : esta libreria importara otras funciones matematicas que necesitaremos algpun dìa
from math import *

#floor: redondea un numero hacia abajo
print(floor(3.9))
print(floor(numero_d1))

#ceil: redondea un numero hacia arriba
print(floor(3.1))
print(ceil(numero_d2))

#srt: raiz cuadrada, ejercicio raiz cuadrada de 30 y redondea el resultado a entero
print(sqrt(144))
print(round(sqrt(30)))


#Programa arroje la raiz cuadrada de 30 en un print, despues otro print donde redondee hacia arriba el resultado y lo multiplique 
# por variable numero_2
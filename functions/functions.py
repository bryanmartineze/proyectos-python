#Las funciones personalizadas son funciones que han sido creadas por el programador para especificar una tarea
#Identacion es una sangria que se forma en automatico al construir una funcion
# def di_hola():
#     print("Hola Usuario")

# #Mandamos a llamar la funcion

# # di_hola()

# #Las funciones no tiene prioridad jerarquica
# print("arriba")
# di_hola()
# print("abajo")

#Podemos parametrizar las funciones
# def saluda(nombre):
#     print("Hola " + nombre)

# saluda("Alan")

# #Podemos definir varios parametro en una funcion
# def saluda(nombre, genero, edad):
#     print("Hola mi nombre es " + nombre + " soy " + genero + " y tengo " + edad + " años")

# saluda("Alan", "hombre", "17")

# print("Bienvenido al generador de saludos con función")
# def saludo(nombre1,apellido1,delegacion1):
#     print("Hola soy " + nombre1 + " " + apellido1 + " de " + delegacion1  + " y mando un saludo a ")
# nombre1 = input("Escribe el nombre del primer participante ")
# apellido1 = input("Escribe el nombre del primer participante: ")
# delegacion1 = input("Escribe la delegacion del segundo participante: ")

# saludo(nombre1,apellido1,delegacion1)
# saludo2(nombre2,apellido2,delegacion2)

#Las funciones pueden ser importadas entre archivos y pueden ser renombradas
from function_holamundo import hola_mundo as hello
hello()
 
















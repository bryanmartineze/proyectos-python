#La declaracion "if" condiciona la accion de un programa si cierto valor se cumple

# alan_es_hombre = True
# if alan_es_hombre:
#     print("Alan es hombre")

#La declaracion "else" se ejecuta despues de que un "if" no cumple con el valor que esperaba como condicion


# alan_es_hombre = False
# if alan_es_hombre:
#     print("Alan es hombre")
# else:
#     print("Alan es mujer pero tiene nombre raro")

#La declaracion "elif" se ejecuta cuando una condicion "if" no cumple, pero no termina el ciclo de decisión, va a seguir comparando segun
#la combinacion de condiciones

# alan_es_hombre = "si"
# alan_es_alto = "si"
# if alan_es_hombre == "si" and alan_es_alto == "si":
#     print("Alan es hombre y es alto")
# elif alan_es_hombre == "si" and alan_es_alto == "no":
#     print("Alan es hombre y es bajo")
# elif alan_es_hombre == "no" and alan_es_alto == "si":
#     print("Alan cambio de sexo")
# else:
#     print("Alan es mujer")

#Tambien podemos condicionar "if" a valores numericos y valores string
# alan_es_hombre = "si"

# if alan_es_hombre == "si":
#     print("Alan es hombre")
# else:
#     print("Alan no es hombre")


# #if con numeros

# cubo = 2

# if cubo == 3:
#     print(cubo*cubo*cubo)
# else:
#     print("Cubo necesita ser tres")


#Ejercicio 1: traslada el pseudocodigo de rutina del dia a codigo Python



#Comparadores logicos, vamos a compara 3 numeros, y vamos a imprimir el numero mayor

# num1 = 1
# num2= 5
# num3 = 4

# if num1 >= num2 and num1 >= num3:
#     print(num1)
# elif num2 >= num1 and num2 >= num3:
#     print(num2)
# else:
#     print(num3)

def num_mayor(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(num_mayor(1,3,4))

#Tarea: Hacer una mejor calculadora





































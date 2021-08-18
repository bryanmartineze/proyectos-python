#La declaracion IF condiciona la accion de un programa si cierto valor se cumple

# alan_es_hombre = True
# if alan_es_hombre:
#     print("Alan es hombre")

#La declaracion ELSE se ejecuta despues de que IF no cumple con el valor que esperaba como condicion

# alan_es_hombre = False

# if alan_es_hombre:
#     print("Alan es hombre")
# else:
#     print("Alan es mujer con nombre raro")

# #La declarcion ELIF se ejecuta cuando una condicion IF no cumple, pero no termina el ciclo del programa, puede seguir comparando

# alan_es_hombre = False
# alan_es_alto = False

# if alan_es_hombre and alan_es_alto:
#     print("Alan es hombre")
# elif alan_es_hombre and not(alan_es_alto):
#     print("Alan es hombre y es bajo")
# elif not(alan_es_hombre) and alan_es_alto:
#     print("Alan cambio de sexo")
# else:
#     print("Alan es mujer")

# #Tambien podemos condicionar IFs a valores numericos y valores string
# alan_es_hombre = "si"

# if alan_es_hombre == "si":
#     print("Alan es hombre")

# cubo = 3

# if cubo == 2:
#     print(cubo*cubo*cubo)
# else:
#     print("Cubo necesita ser tres")

#Ejercicio 1: traslada el pseudocodigo de rutina del dia a codigo Python


print("Este programa muestra la rutina de un developer en su dia a dia")
hambre = ""
lluvia = ""
carne = ""
verdura = ""

hambre = input("¿Cuando me levanto tengo hambre?: ")
if hambre=="si":
    print("Si tengo hambre, como desayuno")
else:
    print("Si no tengo hambre, y salgo sin desayunar")
lluvia = input("\nAl salir de mi casa ¿si esta lloviendo llevo paraguas?: ")
if lluvia=="si":
    print("Si está lloviendo llevo paraguas")
else:
    print("Si esta soleado llevo gorra")

print("\nEn la hora de mi comida llego a un restaurante:")
carne = input("¿Se me antoja carne?: ")
verdura = input ("¿Se me antoja la verdura?: ")
if carne=="si" and verdura=="si":
    print("Si quiero carne y ensalada, ordeno bistec y ensalada cesar")
elif carne=="si" and verdura=="no":
    print("Si quiero carne y no quiero verdura, ordeno spaghetti y albondigas")
else:
    print("Si no quiero carne pero si verdura, ordeno ensalada")



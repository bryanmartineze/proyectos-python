print("Este programa muestra los numeros consiguientes de un par dentro de 100")
ingresado=int(input("Por favor ingrese un numero par: "))


if ingresado % 2 == 0:
    while ingresado <= 100:
        if ingresado % 2 != 0:
            print(ingresado)
        ingresado += 1

    
else:
    print("Este numero no es par.")


# alan_es_hombre = True

# if alan_es_hombre != True:
#     print ("Alan es hombre")
# else:
#     print("Alan no es hombre")

# numero = 10

# if numero != 1:
#     print ("Alan es hombre")
# else:
#     print("Alan no es hombre")
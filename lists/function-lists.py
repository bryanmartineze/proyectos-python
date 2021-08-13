#listas tambien tienen funciones, como por ejemplo extend, que combina dos listas

amigos = ["Bryan","Carlos","Alan"]
nuevos_amigos = ["Gustavo", "Gaspar", "Juan"]

# amigos.extend(nuevos_amigos)
# print(amigos)

#lista.append() me permite agregar otro valor a mi lista
# amigos.append("Jose")

# print(amigos)

#lista.inser(posicion, valor) me permite insertar un valor en la posicion indicada

# amigos.insert(0,"Jose")
# amigos.insert(3, "Karla")

# print(amigos)

#lista.remove("valor") me permite eliminar un valor de la lista
# amigos.remove("Bryan")

# print(amigos)

#lista.pop() va a remover el ultimo elemento de la lista

# amigos.pop()

# print(amigos)

# lista.index("valor") me indica la posicion de un valor

# amigos.extend(nuevos_amigos)


# print(amigos.index("Gaspar"))

# print(amigos)

#lista.count("valor") me indica cuantos valores tengo con el mismo nombre
# amigos.extend(nuevos_amigos)

# amigos.append("Gaspar")

# print(amigos.count("Alan")+amigos.count("Gaspar"))

#lista.sort() ordena a mis valores en cierto orden, en vacio lo hace en orden natural

# amigos.extend(nuevos_amigos)

# amigos.append("Gaspar")

# amigos.sort()

# print(amigos)

# numeros_aleatorios = [30, 21, -1, 0, 99, 99.4]

# numeros_aleatorios.sort()

# print(numeros_aleatorios)

#lista.reverse() ordenar en reversa la posicion de los valores como original fueron insertados

# numeros_aleatorios = [30, 21, -1, 0, 99, 99.4]

# numeros_aleatorios2 = [1, 3, 4, 0]

# numeros_aleatorios.extend(numeros_aleatorios2)

# numeros_aleatorios.sort()

# numeros_aleatorios.reverse()

# print(numeros_aleatorios)

# #lista.copy() copiar los valores de una lista a otra lista

# numeros_aleatorios = [30, 21, -1, 0, 99, 99.4]

# numeros_aleatoriosV2 = numeros_aleatorios.copy()

# print(numeros_aleatoriosV2)



print("Este program recibe 3 numeros en una lista, los ordena de mayor a menor \ny los suma")

num1 = input("Teclee su primer numero: ")
num2 = input("Teclee su segundo numero: ")
num3 = input("Teclee su tercer numero: ")

lista_numeros = [float(num1), float(num2), float(num3)]


print("Su lista de numeros es: ")

lista_numeros.sort()

print(lista_numeros)

print("La suma de su lista es: ", sum(lista_numeros))











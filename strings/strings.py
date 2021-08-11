#\n vuelta de carro o nuevo renglon \ se llama escape
print("La jirafa es amarilla \n y Manchada")

print("Este maestro es muy \"manchado\" ")

frase = "El perico es verde"
#        0123456789
frase2 = " y come semillas"

print(frase + frase2)

#funcion upper(): hace que el string de una variable se convierta en mayusculas

print(frase.upper() + frase2.upper())

#funcion isupper(): compara el string de una variable para saber si son mayusculas

#frase verdadera, frase2 falso

print(frase.upper().isupper() + frase2.isupper())

# #1 es verdadero
# #0 es falso

# #frase verdadera, frase2 verdadera

print(frase.upper().isupper() + frase2.upper().isupper())

# #frase falso, frase2 falso


print(frase.isupper() + frase2.isupper())

#FUNCION LEN: contar los caracteres de un string

# cuenta el numero de cacteres de la variable frase
print(len(frase))

# cuenta el numero de caracteres de la variable frase2
print(len(frase2))


#suma el numero de caracteres de frase con frase2
print(len(frase) + len(frase2))

# transforma los caracteres de  frase y frase2 a mayusculas y compara si los caracteres de frase y frase2 son mayusculas, devuelve un valor booleano
print(frase.upper().isupper() + frase2.upper().isupper())

# finalmente suma el numero de caracteres de frase y frase2 junto con los valores booleanos de la comparaciòn de mayusculas de frase y frase2
print(len(frase) + len(frase2) + frase.upper().isupper() + frase2.upper().isupper())

#variable[] rastrear la posiciòn de un caracter alfanumerico
print(frase[9])

#Variable.index() indica un caracter existente en la oraciòn y python devuelve la posicion
print(frase.index("d"))

#variable.replace("palabra1 o caracter1", "palabra2 o caracter2") remplazarà la palabra indicada por otra
print(frase.replace("perico","quetzal"))

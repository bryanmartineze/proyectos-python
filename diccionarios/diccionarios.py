#Los diccionarios son varibles que guardaran un set de datos, en los que cada dato tendran una llave y un valor de forma
#que cuando se manden a llamar, hagan referencia uno del otro

# conversion_de_meses = {
#     #llave;#significado
#     "ene" : "enero",
#     "feb" : "febrero",
#     "mar" : "marzo",
#     "abr" : "abril",
#     "may" : "mayo",
#     "jun" : "junio",
#     "jul" : "julio",
#     "ago" : "agosto",
#     "sep" : "septiembre",
#     "oct" : "octubre",
#     "nov" : "noviembre",
#     "dic" : "diciembre"
# }

# print(conversion_de_meses["abr"])

# print(conversion_de_meses["abr"])

# #hay otra forma de hacerlo con .get

# print(conversion_de_meses.get("jul"))

# #Podemos hacer referencia a cualquier valor y que envie un valor que no exista

# print(conversion_de_meses.get("lol", "no existe"))




resultado = (input("Elija el numero de mes : "))

conversion_de_meses = {
    #llave;#significado
    "ene" : "enero",
    "feb" : "febrero",
    "mar" : "marzo",
    "abr" : "abril",
    "may" : "mayo",
    "jun" : "junio",
    "jul" : "julio",
    "ago" : "agosto",
    "sep" : "septiembre",
    "oct" : "octubre",
    "nov" : "noviembre",
    "dic" : "diciembre"
}

print(conversion_de_meses[resultado])

#ejercicio rapido, hacer un diccionario de meses donde en vez de abreviaciones, sean numeros las llaves, puedan ser buscadas por un usuario


#Las funciones personalizadas son funciones que han sido creadas por el programador para especificar una tarea
#Identacion
# def di_hola():
#     print("Hola Usuario")
# #mandamos a llamar la funcion
# di_hola()

# #Las funciones no tienen orden jerarquico
# print("Arriba")
# di_hola()
# print("Abajo")

#Podemos darle informacion a las funciones, despues que una funcion recibe informacion se llamaran Parametros
# def saluda(nombre):
#     print("Hola " + nombre)

# saluda("Alan")

# Podemos definir varios parametros para una funcion

# def saluda(nombre, genero, edad):
#     print("Hola " + nombre + " eres " + genero + " y tienes " + edad + " años")

# saluda("Alan", "hombre", "17")

# Crea un programa que invoque una funcion donde los parametros debe ser introducidos por el usuario

print("Bievenido al generador de saludos con funcion")
def saludo():
    nombre = input("Por favor indique el nombre del primer participante:")
    apellido = input("Por favor indique el apellido del primer participante: ")
    delegacion = input("Por favor indique la delegacion donde vive el primer participante: ")
    print("Hola soy " + nombre + " " + apellido + " de " + delegacion)

def dedicado():
    nombre =  input("Por favor indique el nombre del segundo participante:")
    apellido = input("Por favor indique el apellido del segundo participante: ")
    delegacion = input("Por favor indique la delegacion donde vive el segundo participante: ")
    print("Hola soy " + nombre + " " + apellido + " de " + delegacion)


saludo()

# Bienvenido al generador de saludos con funcion
# Por favor indique el nombre del primer participante: Alan
# Por favor indique el apellido del primer participante: Elizalde
# Por favor indique la delegacion donde vive el primer participante: Azcapotzalco
# Hola soy Alan Elizalde de Acapotzalco








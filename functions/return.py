#Las funciones casi siempre son acompañadas de un "Return",
#Return lo que hace es devolver un valor esperado del parametro de una funcion

def cubo(num):
    return num*num*num

print(cubo(3))

print("Bienvenido al generador de saludos con función")
def saludo(nombre1, apellido1, delegacion1):
    return "Hola soy " + nombre1 + " " + apellido1 + " de " + delegacion1
    

print(saludo("Alan","Elizalde","Azcapo"))

#Podemos devolver el resultado de una operacion en una variable y guardarlo

def cuadrado(num):
    return num*num

resultado = cuadrado(2.9)

print(resultado)


#Ejercicio 1, realiza una funcion con return donde el usuario introduzca dos numeros, una base y una potencia y la calcule
print("Bienvenido al programa que calcula potencias con funcion y return")

def potencias(base, potencia):
    return (float(base),float(potencia))

base = input("Por favor introduzca su base: ")


potencia = input("Por favor introduzca su potencia: ")


resultado = potencias(base,potencia)

print(resultado)

#Ejercicio 2, crea un archivo llamado function_pow.py e importa la funcion y mandala a llamar en otro archivo llamado exec_pow.py





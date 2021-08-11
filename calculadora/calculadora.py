nombre = input("Escribe tu nombre: ")
print("Bienvenido " + nombre + " al programa de calculadora")
print("Por favor escriba dos numeros a calcular")
operacion = input("Escriba la operacion que desee realizar (+ o - o * o /): ")
numero_a = input("Primer numero: ")
numero_b = input("Segundo numero: ")


result = float(numero_a) + float(operacion) + float(numero_b)

print("Resultado: ")
print("Bienvenido a la calculadora mejorada")

num1 = input("\nPor favor ingrese el primer numero a calcular: ")

operando = input("\nPor favor ingrese el operando que desea utilizar (+,-,*,/): ")

num2 = input("\nPor favor ingrese el segundo numero a operar: ")

print("\nEl resultado de su operacion es : ")

if operando == "+":
    print(num1 + " + " + num2 + " = ", float(num1) + float(num2))
elif operando == "-":
    print(num1 + " - " + num2 + " = ", float(num1) - float(num2))
elif operando == "*":
    print(num1 + " * " + num2 + " = ", float(num1) * float(num2))
elif operando == "/":
    print(num1 + " / " + num2 + " = ", float(num1) / float(num2))
else:
    print("El operando que usted ingreso no es reconocido.")


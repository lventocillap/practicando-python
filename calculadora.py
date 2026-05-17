num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")

operacion = input("Ingrese la operación a realizar (+, -, *, /): ")

# match operacion:
#     case "+":
#         resultado = float(num1) + float(num2)
#     case "-":
#         resultado = float(num1) - float(num2)
#     case "*":
#         resultado = float(num1) * float(num2)
#     case "/":
#         if float(num2) != 0:
#             resultado = float(num1) / float(num2)
#         else:
#             print("Error: División por cero no permitida")
#             resultado = 0

if (operacion == "+"):
    resultado = float(num1) + float(num2)
elif (operacion == "-"):
    resultado = float(num1) - float(num2)
elif (operacion == "*"):
    resultado = float(num1) * float(num2)
elif (operacion == "/"):
    if float(num2) != 0:
        resultado = float(num1) / float(num2)
    else:
        print("Error: División por cero no permitida")
        resultado = 0

print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
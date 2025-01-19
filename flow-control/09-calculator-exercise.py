""" Custom calculator """

## mensajes de bienvenida
print("Bienvenido a la calculadora\nPara salir escriba Salir")
print("Las operaciones son suma, multi, div y resta")

result = ""

while True:
    if not result:
        result = input("Ingrese un número: ")
        if result.lower() == "salir":
            break
        result = int(result)
    operator = input("Ingrese la operación: ")
    if operator.lower() == "salir":
        break
    n2 = input("Ingrese el siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if operator.lower() == "suma":
        result += n2
    elif operator.lower() == "resta":
        result -= n2
    elif operator.lower() == "div":
        result /= n2
    elif operator.lower() == "multi":
        result *= n2
    else:
        print("Operador no válido")

    print(f"El resultado es {result}")

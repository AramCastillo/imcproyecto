def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def obtener_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Por favor, ingrese un número positivo.")
            else:
                return valor
        except ValueError:
            print("Por favor, ingrese un número válido.")

nombre = input("Su nombre por favor: ").title()
apellido_paterno = input("Su apellido paterno por favor: ").title()
apellido_materno = input("Su apellido materno por favor: ").title()
edad = int(input("Su edad en años por favor: "))
peso = obtener_numero_positivo("Su peso en kilogramos por favor: ")
estatura = obtener_numero_positivo("Su estatura en metros por favor: ")

if nombre.strip() == "" or apellido_paterno.strip() == "" or apellido_materno.strip() == "":
    print("Por favor, complete todos los campos.")
else:
    imc = calcular_imc(peso, estatura)

    print("Nombre:", nombre, apellido_paterno, apellido_materno)
    print("Edad:", edad, "años")
    print("Peso:", peso, "kg")
    print("Estatura:", estatura, "m")
    print("IMC:", imc)

    if 0 <= imc <= 15.99:
        print("Delgadez severa")
    elif 16.00 <= imc <= 16.99:
        print("Delgadez moderada")
    elif 17.00 <= imc <= 18.49:
        print("Delgadez leve")
    elif 18.50 <= imc <= 24.99:
        print("Normal")
    elif 25.00 <= imc <= 29.99:
        print("Sobrepeso")
    elif 30.00 <= imc <= 34.99:
        print("Obesidad leve")
    elif 35.00 <= imc <= 39.00:
        print("Obesidad media")
    else:
        print("Obesidad mórbida")

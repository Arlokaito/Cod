#Conversor de C° a F° y F° a C°
#(°F - 32) x 5/9 =°C
#(°C x 9/5) + 32 =°F

def C(FT):
    C = ((FT - 32) * 5)/9
    return C

def F(CT):
    F = ((CT * 9)/5 + 32)
    return F


correcto = True
while correcto == True:

    print("Que operación desea realizar:\n1- Convertir de °C a °F\n2- Convertir de °F a °C")
    x=int(input("Ingrese número de operación: "))

    if x == 1 or x == 2:
        valor = int(input("ingrese el valor que desea transformar: "))

        if x == 1:
            print(valor,"°C son ",round(F(valor),2),"°F")
            correcto = False

        elif x == 2:
            print(valor,"°F son ",round(C(valor),2),"°C")
            correcto = False

    else:
        print("Se ingresó una operación inválida.\n\n")
        correcto = True
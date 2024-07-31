#Conversor de km-mt-cm-mm-milla-pies-yarda-pulgada
def dibTabla():
    print("|Kilometros \t- Km| \n|Metros \t- Mt| \n|Centimetros \t- Cm| \n|Milimetros \t- Mm| \n|Millas \t- mi| \n|Pies \t\t- ft| \n|Yardas \t- yd| \n|Pulgadas \t- in| \n--------------------")

def metroGeneral(valor1,U):
    if U == "centimetros" or U =="cm":
        valor1 = valor1 / 100
    
    elif U == "kilometros" or U =="km":
        valor1 = valor1 * 1000

    elif U == "milimetros" or U =="mm":
        valor1 = valor1 / 1000

    elif U == "milla" or U == "mi":
        valor1 = valor1 * 1609

    elif U == "pies" or U == "ft":
        valor1 = valor1 / 3.281
    
    elif U == "yarda" or U == "yd":
        valor1 = valor1 / 1.094

    elif U == "pulgada" or U == "in":
        valor1 = valor1 / 39.37

    return(valor1)


print("Indique la unidad de medida que desea transformar\n ___________________")
dibTabla()
UnidadI = input("ingresar dato: ").lower()
Valor = int(input("Ingrese el valor a transformar: "))

print("Indique la unidad de medida a la que desea transformar\n ___________________")
dibTabla()
unidadF=input("ingresar dato: ").lower()

if unidadF == "metros" or unidadF == "mt":
    print(metroGeneral(Valor,UnidadI))


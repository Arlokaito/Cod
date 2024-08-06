#Conversor de km-mt-cm-mm-milla-pies-yarda-pulgada
def dibTabla():
    print(" ___________________")
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
    
    elif U == "metros" or U == "mt":
        valor1

    return(valor1)


dibTabla()
print("Indique la unidad de medida que desea transformar")
UnidadI = input("ingresar dato: ").lower()
Valor = int(input("Ingrese el valor a transformar: "))

dibTabla()
print("Indique la unidad de medida a la que desea transformar")
unidadF=input("ingresar dato: ").lower()

if unidadF == "metros" or unidadF == "mt":
    print("De ",Valor, UnidadI, " a ", unidadF)
    print(round(metroGeneral(Valor,UnidadI),5))

elif unidadF != "metros" or unidadF != "mt":
    
    metro = metroGeneral(Valor,UnidadI)

    if unidadF == "centimetros" or unidadF =="cm":
        print("De ",Valor, UnidadI, " a ", unidadF)
        print(round((metro * 100, unidadF),5))
    
    elif unidadF == "kilometros" or unidadF =="km":
        print("De ",Valor, UnidadI, " a ", unidadF)
        print(round((metro / 1000, unidadF),5))

    elif unidadF == "milimetros" or unidadF =="mm":
        print("De ",Valor, UnidadI, " a ", unidadF)
        print(round((metro * 1000, unidadF),5))

    elif unidadF == "milla" or unidadF == "mi":
        print("De ",Valor, UnidadI, " a ", unidadF)
        print(round((metro / 1609, unidadF),5))

    elif unidadF == "pies" or unidadF == "ft":
        print("De ",Valor, UnidadI, " a ", unidadF)
        print(round((metro * 3.281, unidadF),5))
    
    elif unidadF == "yarda" or unidadF == "yd":
        print("De ",Valor, UnidadI, " a ", unidadF)
        print(round((metro * 1.094, unidadF),5))

    elif unidadF == "pulgada" or unidadF == "in":
        print("De ",Valor, UnidadI, " a ", unidadF)
        print(round((metro * 39.37, unidadF),5))
    
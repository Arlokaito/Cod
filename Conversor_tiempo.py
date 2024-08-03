#convertir el tiempo ingresado a horas, minutos, segundos

def tiempo(unidad,valor):
    if unidad == "hrs":
        valor1 = valor * 60
        valor2 = valor * 3600
        print(valor, unidad, " son")
        print(valor1, "minutos")
        print(valor2, "segundos")

    elif unidad == "ms" :
        valor1 = valor / 60
        valor2 = valor * 60
        print(valor, unidad, " son")
        print(int(valor1), "horas")
        print(valor2, "segundos")

    elif unidad == "seg":
        valor1= valor /3600
        valor2 = valor / 60
        print(valor, unidad, " son")
        print(int(valor1), "horas")
        print(int(valor2), "minutos")


correcto = False
while correcto == False:
    print("Ingresa la abreviación de la unidad que desea transformar, considera:")
    print(" ____________________\n|Horas\t\t- hrs|\n|Minutos\t- ms |\n|Segundos\t- seg|\n --------------------")

    t=input("Unidad: ").lower()
    if t == "hrs" or t == "ms" or t == "seg":
        v = float(input("Ingrese en valor que desea transforar: "))
        tiempo(t,v)
        correcto = True
    else:
        print("Se ingresó unidad inválida.")
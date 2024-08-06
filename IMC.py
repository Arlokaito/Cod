#Calcular el IMC con los datos que se ingresen

def IMC(x,y):
    total = (x / (y**2))
    return total

try:
    peso = float(input("Ingrese su peso en Kg: "))

    try:
        altura = float(input("Ingrese su altura en metros: "))

        print("Su IMC es ", round(IMC(peso,altura),1))

        if IMC(peso,altura) < 18.5 :
            print("Su IMC se encuentra bajo el rango saludable.")

        elif IMC(peso,altura) >= 18.5 and IMC(peso,altura) <= 24.9:
            print("Su IMC se encuentra en el rango saludable.")

        elif IMC(peso,altura) > 24.9:
            print("Su IMC se encuentra sobre el rango saludable.")


    except:
        print("Ingresó un valor inválido para la altura.")

except:
    print("Ingresó un valor inválido para el peso.")
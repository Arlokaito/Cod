#crear un generador de contraseña, indicando el largo minimo, largo maximo, caracteres especiales
from random import choice as ch

def crearContraseña(numero, validador):
    Contraseña = ""
    i = 1
    if validador == "no": #Se genera contraseña sin caracteres especiales
        while i <= numero:
            Contraseña = Contraseña + ch(ABCD)
            i += 1

    elif validador == "si": #Se genera contraseña con caracteres especiales
        dificil = ABCD+especial

        while i <= numero:
            Contraseña = Contraseña + ch(dificil)
            i += 1

    return(Contraseña)

especial =["!","¡","#","$","%","&","/","(",")","=","@","-","_","+","-","*",".",",","^"," ","ñ","Ñ","?","¿"]
ABCD =["A","a","B","b","C","c","D","d","E","e","F","f","H","h","I","i","J","j","K","k","L","l","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","X","x","Y","y","Z","z","0","1","2","3","4","5","6","7","8","9"]

try:
    maxLargo = int(input('Indica cual es el máximo de carácteres: '))
    correcto = False
    while correcto == False:
        esp = input("Con carácteres especiales, indique si o no: ")
        if esp == "si" or esp =="no":
            nuevaContraseña=crearContraseña(maxLargo,esp)
            print("La contraseña generada es : ", nuevaContraseña)
            print("El largo de la contraseña es :", len(nuevaContraseña))
            correcto = True
        else:
            print("Se ingresó una opción inválida, por favor vuelva a indicar si la contraseña debe contar")
            correcto = False

except ValueError:
    print("Se ingresó un número inválido de carácteres.")



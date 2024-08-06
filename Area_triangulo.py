#calcular el área de un triangulo

def area(x,h):
    a = (x*h)/2
    return a

try:
    base = float(input("Ingresa el valor de la base: "))
    altura = float(input("Ingresa el valor de la altura: "))

    print("El área de un tríangulo con base ", base, " y altura ", altura, " es de ", round(area(base,altura),2))
except:
    print("No se ingresó un valor válido.")
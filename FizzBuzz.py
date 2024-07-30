#Crear función FizzBuzz, mostrando por consola los numeros del 1 a N
#Los multiplos de 3 mostrarán "Fizz"
#Los multiplos de 5 mostrarán "Buzz"
#Los multiplos de ambos indicarán la palabra "FizzBuzz"

def fizzBuzz(numero): #en base al número máximo solicitado, realiza la iteración
    for i in range (1,numero+1,1):
        if i % 3 == 0 and i % 5 == 0 :
            print("FizzBuzz")

        elif i % 3 == 0:
            print("Fizz")

        elif i % 5 == 0:
            print("Buzz")

        else:
            print(i)

N = int(input("Indica el número máximo a mostrar: "))

fizzBuzz(N)


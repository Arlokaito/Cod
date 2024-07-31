#introducir en el imput una frase y contar cuantas palabras tiene.
frase = input("ingrese su frase: ")
oracion = frase.split() #split devuelve una lista de palabras indicando como argumento el separador, al dejar en blanco es equivalente a decir " ".

contador = 0
for i in oracion: #recorre la lista de palabras 
    contador += 1

print(contador) 
print(len(oracion)) #equivalente a indicar cuantas palabras tiene la lista oracion, ya trabajada con el separador indicado
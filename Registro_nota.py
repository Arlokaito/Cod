lista_alumnos = {   #Crea el diccionario de alumnos                          
            'carlos'    : {'Nombre': 'Carlos'   ,   'Notas': [], 'Promedio':'', 'Situacion':''},
            'ana'       : {'Nombre': 'Ana'      ,   'Notas': [], 'Promedio':'', 'Situacion':''},
            'maria'     : {'Nombre': 'Maria'    ,   'Notas': [], 'Promedio':'', 'Situacion':''},
            'gabriel'   : {'Nombre': 'Gabriel'  ,   'Notas': [], 'Promedio':'', 'Situacion':''},
            'elizabeth' : {'Nombre': 'Elizabeth',   'Notas': [], 'Promedio':'', 'Situacion':''},

}



correcto = True
while correcto == True: #Para seguir solicitando en caso de ingresar un nombre erróneo

    try:
        alumno = input("Ingrese en nombre del estudiante al que desea registrar calificación. ").lower() #Nombre a buscar en el diccionario de alumnos
        if alumno.isalpha() == True:

            if alumno in lista_alumnos: #Valida si el alumno se encuentra en sistema
                    try:
                        cant = int(input("Ingrese la cantidad de notas que registrará : ")) #Indicar cantidad de notas que se ingresarán
                        total = 0
                        contador = 1
                        while contador <= cant:
                            
                            try:
                                x = float(input("ingrese nota : ")) #Ingresa la nota
                                
                                if x > 0 and x <= 7:   #Evita que se registren notas neutras y negativas
                                    lista_alumnos[alumno]['Notas'].append(x) #la nota se agrega a la lista de notas

                                    total = total + x #calcula el total de las notas ingresadas
                                    contador+=1
                                elif x > 7:
                                    print("Ingresó nota inválida")
                                elif x == 0:
                                    print("No se puede registrar nota 0")

                                elif x < 0:
                                    print("Ingresó nota inválida")

                            except ValueError:
                                print("Se ingresó un carácter inválido")


                        promedio = total/cant #Se calcula promedio de notas ingresadas
                        lista_alumnos[alumno]['Promedio'] = round(promedio,1) #Se registra promedio

                        if round(promedio,1) >= 4.0:
                             lista_alumnos[alumno]['Situacion']= "Aprobado"
                        elif round(promedio,1) < 4.0:
                             lista_alumnos[alumno]['Situacion']= "Reprobado"

                        print(lista_alumnos[alumno]) #Muestra el registro del alumno

                        
                    
                    except ValueError:
                                print("Se ingresó un carácter inválido")
                            
            else:
                print("No se encontró al alumno en sistema") #En caso de no existir en el disccionario


            #Para continuar registrando
            otroRegistro = input("¿Desea realizar otro registro de notas? Ingrese N para finalizar, en caso contrario ingrese una letra distinta : ")

            if otroRegistro.lower() == "n" or otroRegistro.lower() == "no":
                print(lista_alumnos)
                correcto = False
        else:
             print("Se ha ingresado un caracter inválido en el nombre del alumno")

    except TypeError:
        print("Se ingresó un caracter inválido\nSe recomienda ingresar nuevamente el dato solicitado")


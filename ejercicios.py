# username = input('Ingrese su nombre: ')

# print(username.upper())

# print(username.lower())

# print(username.capitalize())

#------Ejercicio 2---------

# asignaturas = ['quimica', 'fisica', 'matematicas', 'sociologia']

# print(asignaturas)

#------Ejercicio 3---------

# alumno = {}

# while True:

#     if bool(alumno):

#         consulta = input('Desea agregar otra asignatura? (Y/N): ')

#         if consulta == 'Y' or consulta == 'y':
#             asignatura = input('Ingrese asignatura: ')

#             calificacion = input('Ingrese calificacion para {}'.format(asignatura))

#             alumno[asignatura] = float(calificacion)
            
#         elif consulta == 'N' or consulta == 'n':

#             print('Notas cargadas exitosamente.')

#             print(alumno)
            
#             break
#         else:

#             print('Opcion incorrecta, saliendo del programa...')

#             print('Notas cargadas exitosamente.')

#             print(alumno)

#             break
#     else:

#         asignatura = input('Ingrese asignatura: ')

#         calificacion = input('Ingrese calificacion para {}: '.format(asignatura))

#         alumno[asignatura] = float(calificacion) 

#------Ejercicio 4---------

# word = input('Ingrese una palabra: ')

# for x in range(20):
#     print(word)

#------Ejercicio 5---------

# edad = input('Ingrese su edad: ')

# if int(edad) < 18:
#     print('El usuario es menor de edad.')
# else:
#     print('El usuario es mayor de edad.')

#------Ejercicio 6---------

# dividendo = input('Ingrese dividendo: ')

# divisor = input('Ingrese divisor: ')

# try:
#     division = int(dividendo) / int(divisor)
    
#     print(f'El resultado de {dividendo} dividido {divisor} es: {division}')
# except:
#     print('Ingrese solo numeros (divisor distinto de 0).')


#------Ejercicio 7---------

numero = int(input('Ingrese un numero: '))

string = ''

for x in range (1, numero + 1):
    if x % 2 != 0:
        string = string + f'{x}, '

print(string)


                
                


                
        
    
    
    
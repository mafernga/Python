# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:33:22 2020

@author: Mario_Andres

PRINCIPALES METODOS DE CONTROL DE FLUJO EN PYTHON
"""
"""
******************************************************************************************
IF - ELSE
******************************************************************************************

Usamos if-else para tomar decisiones y ejecutar distintas partes del codigo rn funcion de 
una condición

NOTA: En Python, la manera de indicar si estamos dentro del bucle o una funcion  es mediante 
el indentado, es decir poniendo 4 espacios delante del codigo
(En Spyder presinando la tecla TAB automaticamente inserta 4 espacios)
"""

#%%
#La Manera mas sencilla de implementar una evaluacion  logica es con IF

Temperatura=21

if Temperatura<22:
    print("El día está fresco")
#%%
 #Si queremos tomar decisiones en funcion de una condicion ocurra u otra
 #podemos usar if-else   
Temperatura2=30

if Temperatura2<=22:
     Respuesta=("Es un día perfecto para ir de Picnic")
elif  Temperatura2<=28:
    Respuesta=("Es un día perfecto para ir a Piscinas")
else:
    Respuesta=("Es un buen día para ir a Playa")
        
print(Respuesta)         
#%%
 #Tambien podemos insertar if dentro de otros if esto se llama nestear  
Temperatura3=30
Lluvia=True

if 25<Temperatura3<31:
    if  not Lluvia:
        print("Es un día perfecto para ir de Picnic")
    if  Lluvia:
        print("No es un día perfecto para ir de Picnic")
#%%
"""
******************************************************************************************
BULES FOR (FOR LOOP)
******************************************************************************************

Los bucles For sirven para iterar entre los elementos de una lista uno por uno, o de cualquier elemento
de Python que soporte iteracion
"""
numeros=[1,2,3,4,5,6,8,34,56,9,10]

for numero in numeros:
    if numero<=10:
        print(f"Numero Valido {numero} ")
        
    else:
        print(f"ERROR! Numero {numero} mayor que 10")

#%%
"""
A veces queremos romper el bucle for si ocurre una condicion podemos romper el loop con Break
"""
numeros=[1,2,3,4,5,6,8,34,56,9,10]

for numero in numeros:
    if numero<=10:
        print(f"Numero Valido {numero} ")
        
    else:
        print(f"ERROR! Numero {numero} mayor que 10,|SALIENDO DEL BUCLE|")
        break

#%%
"""
Hay  veces que en vez de romper el bucle, simplemente queremos pararlo pero no queremos hacer nada en 
una iteracion en concreto, para esto podemos usar pass
"""
numeros=[1,2,3,4,5,6,8,34,56,9,10]

for numero in numeros:
    if numero<=10:
        print(f"Numero Valido {numero} ")
        
    else:
       #pass se usa en aquellos casos en los que hay que poner algo en un segmento del codigo pero no hace nada
        pass
#%%
"""
continue, al cotrario de pass nos lleva directamente a la siguoiente iteraccion del bucle
"""
numeros=[1,2,3,4,5,6,8,34,56,9,10]

for numero in numeros:
    if numero<=10:
        print(f"Numero Valido {numero} ")
        
    else:
       #pass se usa en aquellos casos en los que hay que poner algo en un segmento del codigo pero no hace nada
        continue
        print("Esto no se va a imprimir")
    
#%%
"""
Hay una manera mas simplificada de iterar los elemntos de una lista

"""
numeros=[1,2,3,4,5,6,8,34,56,9,10]
[numero for numero in numeros if numero<10]
#%%
#tambien Se le puede asignar a una variable
a=[numero for numero in numeros if numero<10]
print(a)

#%%
"""
Podemos iterar las claves de un diccionario con un for
"""
Mario_notas={
      "Calculo": 4.5,
      "Programacion": 3.5,
      "Algebra": 4.5,
       }
print(Mario_notas)
for materia in Mario_notas:
    print(materia)
#podemos iterar las claves y los valores de un diccionario a la vez en un bucle for usando items()
for materia, notas in Mario_notas.items():
    print(materia, notas)
    print("En la matería {} mi nota fue {}".format(materia, notas))
#%%
"""
No solo als lsitas son iterables(es decir soportan bucle for), lso string tambien 
"""

pais="Colombia"

for letra in pais:
    print("Dame una {}".format(letra))
    print(len(pais))
#%%

"""
******************************************************************************************
TRY EXCEPT
******************************************************************************************

En ocasiones los programas fallan lanzando excepciones, pero una forma de hacer que el programa siga
su funcionamiento pese a haber fallado es atrapando la excepcion.
En Python eso se hace mediante el bloque try-except.

siempre que atrapamos una excepcion , es importante por lo menos imprimir el mensaje de error 
Asi nos aseguramos de que nuestro programa no esta fallando catastroficamente sin que nos de os cuenta   
"""
numero_str=("4.5")
try:
    numero_int=int(numero_str)
except Exception as e:
    print("Error, el valor {} no se puede convertir a entero".format(numero_str))
    print("El mensaje de error es: {}: {}".format(type(e), e))
 #%%   
"""
El problema de capturar todos los errores de nuestro programa a ciegas es que podemos pasar
errores que hagan que todo falle de forma silenciosa, una forma mas efectiva de capturar esos errores
es capturar aquellos que conozcamos y fallar en caso d eun error que no conozcamos, 
es una buena manera de hacer control de los errores
"""
numero_str=("4.5")
try:
    numero_int=int(numero_str)
    print(type(numero_int))
except ValueError: #esto fallara para todo error que no sea un ValuError
    print("Error, el valor {} no se puede convertir a entero".format(numero_str))



#%%
    
#%%

"""
******************************************************************************************
BUCLE WHILE
******************************************************************************************

Los bucles WHILE siguen ejecutandose mientras una condicion se cumpla  
"""
n_elefantes=(2)

print("1 Elefante se balanceaba sobre la tela de una araña")
while n_elefantes<=10:
    print("{} Elefantes se balanceaba sobre la tela de una araña".format(n_elefantes))
    
    n_elefantes+=1
    
#%%
"""
Un uso comun del while es validar el input que nos da un usuario 
podemos obtener el input de un usuario usando la funcion input
"""

while 1:
    input_usuario=input("Digite un numero entre el 1 y el 10, para salir escriba 'exit' :")
    try:
        if input_usuario =="exit":
            print("Adios")
            break
        elif int(input_usuario)<=10:
            cuadrado=int(input_usuario) **2
            print("El cuadrado de {} es {}".format(input_usuario, cuadrado))
        else:
            print("El valor {} no es un valor valido".format(input_usuario))
    except ValueError:
        print("El valor ingresado '{}' no es valido, no se puede convertir a entero".format(input_usuario))
        
    
 #%%   

"""
******************************************************************************************
EJERCICIOS BUCLES
******************************************************************************************
"""
"""
Dado el diccionario, convertir todas las claves en mayuscula usando bucles, luego crear una lista con los 
dias de la semana que contengan "o"
"""
dias_semana={"Lunes": 1,
             "Martes": 2,
             "Miercoles": 3,
             "Jueves": 4,
             "Viernes": 5,
             "Sabado": 6,
             "Domingo": 7,
            }

dias_semana_mayusculas={} #primero creamos un diccionario vacio para guardar las claves en mayuscula

for clave, valor in dias_semana.items():
    dias_semana_mayusculas[clave.upper()]=valor
dias_semana=dias_semana_mayusculas
print(dias_semana)
#%%
#crear una lista con los dias de la semana que contengan "o"
dias_con_o=[]
for clave in dias_semana:
    if "O" in clave:  #La letra "O" en mayuscula porque en el ejercicio anterior las claves se habian convertido en mayusculas
        dias_con_o.append(clave)
print(dias_con_o)
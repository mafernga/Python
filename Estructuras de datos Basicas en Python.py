# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 14:12:35 2020

@author: Mario_Andres



LAS ESTRUCTURAS DE DATOS SON AQUELLOS OBJETOS QUE SE UTILIZAN PARA ALMACENAR INFORMACION
HAY MUCHOS TIPOS PERO ESTOS SON LOS MAS BASICOS

"""
#%%
"""
*******************************************************
LISTAS 
*******************************************************

Las listas son conjuntos de elementos ordenados donde cada elemento tiene una posicion 
"""

colores=["amarillo","azul","rojo","blanco","negro"]
print(colores)
print(type(colores))

#%%
#ACCEDEMOS A LOS ELEMENTOS DE UNA LISTA CON []
#EL INDICE DE LOS ELEMENTOS D EUNA LISTA EMPIEZA EN 0
#ESO QUIERE DECIR QUE AL PRIMER ELEMENTO S EACCEDE CON [0]

print(colores[0])

#asignarle el elemento de una lista a una variable
carro=(colores[1])
print(carro)

#Podemos acceder a un rango de elementos de una lista con [inicio:final-1:orden]
print(colores[:3])

#Podemos acceder a los elementos desde el 2 hasta el final
print(colores[2:])

#Podemos acceder a los 2 ultimos elementos de la lista utilizando  numeros negativos
print(colores[-2:])

#Podemos saltarnos elementos de n en n utilizando[::n], por ejemplo si queremos solo los elementos pares
print(colores[::2])

#Si el orden es un numero negativo nos devuelve la lista de manera inversa
print(colores[::-1])
#%%
#OTROS USOS

ciudades=["Monteria", "Sincelejo", "cartagena", "Medellin"]

#Podemos calcular el numero de elementos de una lista con len
print(len(colores))

#Podemos agregar Elementos a la lista con append 
colores.append("Morado")
print(colores)

#Podemos repetir una lista multiplicandola por un entero
print(colores * 2)

#Podemos concatenar listas con el simbolo +
print(colores + ciudades)

#Podemos modificar elementos de una lista
ciudades[0]="Cali"
print(ciudades)
print(len(ciudades))

#%%
#Podemos alargar la lista sin importar el tamaño inicial modificar con rangos
ciudades[2:]=["Valledupar", "Barranquilla","Pereira", "Manizales"]
print(ciudades)
print(len(ciudades))

#%%
#Podemos evaluar si un elemento existe en una lista
print(ciudades)
consulta1="Cali" in ciudades
print(consulta1)

print("Cali" in ciudades)
print("envigado" in ciudades)

#%%
#Podemos buscar la posicion de un elemento
print(ciudades)
print("La posicion en la lista de la palabra Prerira es {}".format(ciudades.index("Pereira")))

print("La posicion en la lista de la palabra Sincelejo es {}".format(ciudades.index("Sincelejo")))
#%%
#Podemos eliminar el elemento en una posicion concreta utilizando pop
print(ciudades)
ciudades.pop(2)
print(ciudades)
#%%
#Combinando index y pop podemos eliminar un elemento en concreto cunado no sabemos al posicion
print(ciudades)
ciudades.pop(ciudades.index("Manizales"))
print(ciudades)

#%%
#Podemos ordenar als listas con el metodo sort

lista1=[5,8,2,4,0,9,1,34,78,23,45,78,999]
print(lista1)
lista1.sort()
print(lista1)
ciudades.sort()
print(ciudades)

#%%
#Podemos generar listas de numeros con la funcion range()
range(10)
print(list(range(10)))

#%%
#Los string se pueden acceder de forma similar a las listas
palabra1="Cartagena"
print(palabra1[0])
print(palabra1[:4])
print(palabra1[2:])
#%%
"""
*******************************************************
TUPLAS (TUPLES)  se usan parentesis() en vez de corchetes[]
*******************************************************

Las TUPLAS son versiones de las listas que no se pueden modificar
"""

nombres=("Mario","Maria","Santiago","Mariana")
print(nombres)
print(type(nombres))

#Podemos acceder a los elementos de una tupla igual que en als listas
print(nombres[2:])
print(nombres[:2])

#Sin embargo no se podria modificar
nombres[2]="Laura"

#%%
"""
*******************************************************
DICCIONARIOS  dict
*******************************************************

Las DICCIONARIOS son un conjunto de claves (keys) asociadasa valores (values)
Sabiendo una clave podemos encontrar el valor de dicha clave
"""

inventario= {
       "Papas": 5,
       "Tomates": 8,
       "Naranjas": 10,
       "Mandarinas": 4,
        }

print(type(inventario))
print(inventario)

#%%
#Podemos ver las claves que tiene un diccionario con el metodo Keys()
print(inventario.keys())

#%%
#El metodo keys() nos devuelve una lista, si queremos acceder a las claves como una lista
#tenemos que convertirla a una
print(inventario.keys()[0]) # ejemplo de que no devuleve nada si no se convierte en lista
#%%
print(list(inventario.keys())[2])
#%%
#Podemos ver los valores que tiene un diccionario con el metodo values()
print(inventario.values())
#%%
#Accedemos a los elementos de un diccionario con[]
print(inventario["Naranjas"])
#%%
#Podemos evaluar si una clave existe en un diccionario 
print("Mandarinas" in inventario)
print("Mangos" in inventario)

#%%
#Podemos eliminar una clave en un diccionario con pop()
print(inventario)
kilos_mandarinas= inventario.pop("Mandarinas")
print("Tenemos {} kilos de Mandarinas".format(kilos_mandarinas))
print(inventario)

#%%
#CADA TIPO DE ESCTRUCTURA DE DATOS PUEDE ALMACENAR LOS OTROS 
#Una lista con listas dentro

lista_trayectos=[
        ["Cartagena", "Monteria"],
        ["Medellin", "Monteria"],
        ["Monteria", "Medellin"],
        ["Cali", "Monteria"]
        
        ]
        
print(lista_trayectos[1][0])
print(lista_trayectos[1][1])     
print(lista_trayectos[3][1])        
        
#%%
#UN DICCIONARIO CON TUPLAS COMO VALORES

dict_trayectos={
        "Medellin":("Monteria", "Cali"),
        "Monteria":("Medellin", "Cali"),
        "Cali":("Medellin", "Monteria"),
        }
        
print(dict_trayectos["Medellin"])
print(dict_trayectos["Cali"])   
print(dict_trayectos["Monteria"]) 

#%%
#UNA LISTA QUE CONTIENE DICCIONARIOS

lista_diccionarios=[
        {"Origen":"Medellin", "Destino": "Monteria"},
        {"Origen":"Cali", "Destino": "Medellin"},
        ]
        
print(lista_diccionarios)


#%%
#COMO AÑADIR ELEMENTOS A DICCIONARIOS

dias_semana={
        "Lunes": 1,
        "Martes": 2,
        "Miercoles": 3,
        }
        
print(dias_semana)
#Si queremos añadir el nuevo elemento "Jueves": 4, lo haríamos así:
dias_semana["Jueves"]=4
print(dias_semana)

"""
De forma similar podemos actualizar elementos de una lista
(que no ampliar, para añadir elementos adicionales 
habria que usar append). 
"""
#%%
frutas2= ["Naranja", "Pera","Mandarina","Manzana"]
#Si tenemos esta lista y quisieramos cambiar el segundo elemento (indice 1) 
#y cambiarlo por "sabado", lo haríamos así:

print(frutas2)
frutas2[1]="Mora"
print(frutas2)
frutas2[3]="Fresa"
print(frutas2)
#%%
"""
EJERCICIO
Crear un diccionario cuyas claves sean los primeros 3dias de la semana y su valor sea la posicion de dicho día
y Luego convertir todas las claves en mayusculas
"""
Semana={
       "Lunes":1,
       "Martes":2,
       "Miercoles":3       
       }
print(Semana)

Semana["LUNES"]=Semana.pop("Lunes")
Semana["MARTES"]=Semana.pop("Martes")
Semana["MIERCOLES"]=Semana.pop("Miercoles")
print(Semana)

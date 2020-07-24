# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:49:40 2020

COMO LEER Y ESCRIBIR ARCHIVOS EN PYTHON

@author: Mario
"""

#%%
"""
********************************************
CREACION DE CARPETAS
********************************************
"""
#Podemos crear directorios con os.makedirs()

import os
os.makedirs("C:/Users/Mayte/Documents/UDEMY/PYTHON/Prueba", exist_ok=False)
os.makedirs("./Prueba2", exist_ok=False)

#%%
"""
********************************************
LISTADO DE ARCHIVOS
********************************************
Con os.listdir nos muestra el lsitado de archivos de la carpeta actual
"""
archivos_carpeta_actual=os.listdir(".")
print(archivos_carpeta_actual)

#%%
"""
********************************************
ESCRITURA DE ARCHIVOS
********************************************
"""
#Podemos usar open para abrir un acrchivo, si eñ archivo no existe saldra un error

archivo_inexistente=open("./prueba1.txt")
#%%
#si queremos crear un archivo para escribir debemos especificar el metodo de escritura "w"
archivo_para_escribir=open("./prueba2.txt","w")
archivo_para_escribir.write("Hola ")
archivo_para_escribir.write("mundo")
archivo_para_escribir.close

#%%
#Se puede usar el metodo "a" para poder agregar sn  borrar lo que ya estaba
archivo_para_escribir=open("./prueba2.txt","a")
archivo_para_escribir.write(" Hola ")
archivo_para_escribir.write(" mundo2 ")
archivo_para_escribir.close

#%%
"""
********************************************
USAR EL METODO OPEN CLOSE NO ES EL IDEAL PORUQE LA INFORMACION S EGUARDA CUANDO EJECUTAMOS CLOSE
Y SI PASA ALGUN ERROR ENTRE OPEN Y CLOSE SE PUEDE PERDER AL INFORMACION

********************************************
La mejor manera de leer y escribir archivos es mediante el contexto with
"""
usuarios=["Mario","Andres","Fernandez","Garcia", "Mariana", "Mayte","Anaconda"]
with open("./prueba4.txt", "w") as archivo_escribir:
    for usuario in usuarios :
        archivo_escribir.write(usuario)
        archivo_escribir.write("\n")
        
#%%
"""
********************************************
LECTURA DE ARCHIVOS
********************************************
"""
#Aqui le vamos a asignar a una variable el conbtenido del archivo
with open ("./prueba3.txt") as archivo1:
    datos=archivo1.read()
print(datos)
print(type(datos))

#%%
"""
********************************************
USANDO PATHLIB
********************************************
En windows las carpetas se definen con / pero en MAC o Linux se usa \
Esto puede generar errores
Una manera de garantizar el acceso a las carpetas independientemente del sistema operativo
es usando el modulo  pathlib (disponible en python 3 en adelante)
"""

from pathlib import Path
carpeta= Path("./PYTHON/")
archivo=carpeta/"prueba5.txt"
print(type(archivo))
print(archivo.read_text())

#%% Con pathlib podemos escribir facilmente a un archivo

carpeta= Path("./PYTHON/")
archivo=carpeta/"prueba6.txt"
archivo.write_text("Hola")
print(archivo.read_text())
#%% Con pathlib podemos seguir usando with
usuarios1=["Maria","Mariana","Karina","Natalia"]
print(type(usuarios1))

carpeta=Path("./PYTHON/")
archivo=carpeta/"prueba6.txt"
with open(archivo,"a")as fname:
    for usuario in usuarios1:
        fname.write(usuario)
        fname.write("\n")
print(archivo.read_text())

#%%
"""
********************************************
EJERCICIOS INPUT Y OUTPUT
********************************************
1. HACER UNA FUNCION QUE DADO EL NOMBRE DE UN ARCHIVO, LO LEA Y DEVUELVA
LA LINEA CON LA MAYOR LONGITUD DEL ARCHIVO
"""
def linea_mas_larga(nombre):
    with open(nombre) as fname:
        lineas=[linea.strip("\n") for linea in fname.readlines()] #Usamos strip para eliminar caracteres al inicio y al final del string y usamos readlines para leer linea por linea de un archivo
    linea_mas_larga=lineas[0] #iniciamos la variable con el valor de la primer alinea
    for linea in lineas:
        if len(linea)>len(linea_mas_larga):
            linea_mas_larga=linea
    return linea_mas_larga

print(linea_mas_larga("./PYTHON/prueba6.txt"))
#%%
"""
********************************************
EJERCICIOS INPUT Y OUTPUT
********************************************
2. HACER UNA FUNCION QUE TENGA COMO ARGUMENTO  UN NOMBRE DE UN ARCHIVO Y UN NUMERO N
Y DEVUELVA LAS N ULTIMAS LINEAS
"""

def leer_n_ultimas(nombre,n):
    with open(nombre, "r")as fname:
        lineas=[linea.strip("\n") for linea in fname.readlines()]
    return lineas[-n:]

print(leer_n_ultimas("./PYTHON/prueba6.txt", 3))

#%%
"""
********************************************
EJERCICIOS INPUT Y OUTPUT
********************************************
3. HACER UNA FUNCION QUE DADO UN DICCIONARIO CREE UN ARCHIVO CSV  CIN LOS DATOS DDEL MISMO
LOS ARCHIVOS CSV(COMMA-SEPARATED-VALUES) SON UNA FORMA DE ALMACENAR DATOS CON CADA COLUMNA
SEPARADA POR UNA COMA

POR EJEMPLO SI TENEMOS EL SIGUIENTE DICCIONARIO

{
 "nombre":["Mario","Mayte", "Santiago", "Mariana"],
 "edad":["35","31", "8", "6"],
 "ciudad:["Monteria","Medellin", "Sampues", "Ayapel"],
 
 }

Dicho diccionario convertido en CSV tendria el siguiente formato:
    nombre,edad,ciudad
    Mario,35,Monteria
    Mayte,31,Medellin
    Santiago,8,Sampues
    Mariana,6,Ayapel
"""
datos={
       "nombre":["Mario","Mayte","Santiago","Mariana"],
       "edad":[35,31,8,6],
       "ciudad":["Montería","Medellín","Sampues","Ayapel"]
       }

def dict_a_csv(datos,nombre):
    claves=list(datos.keys())  #convierte el diccionario en una lista
    n_items=len(datos[claves[0]])#Cuenta la longitud de la primera clave de los datos
    with open(nombre,"w") as fname:
        fname.write(','.join(claves))
        fname.write("\n")
        for i in range (n_items):
            fila=",".join([str(datos[clave][i]) for clave in claves ])
            fname.write(fila)
            fname.write("\n")
dict_a_csv(datos,"./PYTHON/prueba8.csv")


            

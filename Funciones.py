# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:26:28 2020

@author: Mario_Andres
"""

"""
***********************************************************************
FUNCIONES
***********************************************************************

Los scripts en python se ejecutan linea a linea

Las funciones son la foram de separar la logica en piezas sin tener que ejecutarlas linea a linea,
y ademas permitir  reutilizar partes del codigo que se repiten.

Las funciones se definen de la forma:
    
def nombre_de_la_funcion(argumento1, argumento2,....):
    logica_de_la_funcion
"""
#%%
def saludar():
    print("Hola como estas: ")
    
#Al crear la funcion saludar ya no tenemos que escribir print cada vez
print(type(saludar))
saludar()

#%% Tambaien le podemos asignsar una variable
def saludar(nombre):
    print(f"Hola {nombre} como estas?")

saludar("Mariana")

#%% Tambaien le podemos asignsar un valor por defecto a la variable
def saludar(nombre="Amigo"):
    print(f"Hola {nombre} como estas?")

saludar("Mario") # aca se incluira en el resultado el nombre mario
saludar()  #aca como no se definio, el resultado será el que le dimos por defecto

#%% LAS FUNCIONES PUEDEN DEVOLVER UN VALOR
def suma(a, b):
    return a+b  #Las funciones solo pueden tener un  solo return, si s eolvida poner el return el resultado es none

suma(5,4)

resultado_suma1=suma(4,3.5)
resultado_suma2=suma(resultado_suma1,102) #podemos usar el resultado de la suma 1 como input
print(resultado_suma1)
print(resultado_suma2)
#%% LAS FUNCIONES TIENEN UN SOLO RETURN PERO S EPUEDEN DEVOLVER MULTIPLES COSAS, EN TUPLAS

def suma_resta (a,b):
    suma=a+b
    resta=a-b
    return suma, resta

resultado5=suma_resta(8,2)
print(resultado5)
print(type(resultado5))
#%% Podemos desempaquetar el resultado directamente
resultado_suma, resultado_resta=suma_resta(8,2)
print("El resultado de la suma es: {} ".format(resultado_suma))
print("El resultado de la resta es: {} ".format(resultado_resta))
#%%
"""
***********************************************************************
FUNCIONES LAMBDA O ANONIMAS
***********************************************************************

Existe otra forma de crear funciones, las llamadas lambda o funciones anonimas.

Las funciones lambda o anoonimas se definen de la forma:
    
func_lambda=lambda input: output

Las funciones lambda se suelen utilixar cuando queremos aplicar logica sencilla
para la cual definir una funcion oficial no es necesario
"""
suma_lambda= lambda a,b: a+b
resultadoX=suma_lambda(5,4)
print("El resultado de la suma es {}".format(resultadoX))
#%%
"""
***********************************************************************
EJERCICIOS CON FUNCIONES
***********************************************************************
"""
#CREAR UNA FUNCION RESTA, QUE RESTÉ 2 NUMEROS Y DEVUELVA EL RESULTADO
def resta(a,b):
    resultado_re=a-b
    return resultado_re
print("El resultado de la resta es: {}".format(resta(8,2)))

#%%
#CREAR UNA FUNCION  QUE CONVIERTA UN STRING EN MINUSCULAS
def minuscula(a=input("Digite la palabra que desea convertir en minuscula: ")):
    resultado=a.lower()
    return resultado
print("El resultado de convertir la palabra en minsucula es: {} ".format(minuscula()))

#%%
#CREAR UNA FUNCION LAMBDA QUE CONVIERTA UN STRING EN MINUSCULAS
strg_minuscula=lambda a=input("Digite la palabra que desea convertir en minuscula: "):a.lower()
print(strg_minuscula())
#%%
#CREAR UNA FUNCION QUE ACEPTA 3 ARGUMENTOS, 2 NUMEROS Y UN STRING, SI EL STRING ES "SUMA",
#DEVOLVER LA SUMA DE LOS 2 NUMEROS, SI EL STRING ES "RESTA", DEVOLVER AL RESTA D ELOS 2 NUMEROS

def suma_o_resta(a=input("Digite un numero: "),b=input("Digite otro numero: "), c=input("Escriba 'suma' o 'resta'")):
    try:
        if c=="suma":
            resultado_suma=int(a)+int(b)
            return resultado_suma
        elif c=="resta":
            resultado_resta=int(a)-int(b)
            return resultado_resta
        else:
            print("Ingresasté un valor errado")
    except ValueError:
        print("El valor ingresado  no es valido, por favor vuelva a intentarlo")
        
suma_o_resta()

#%%
#CREAR UNA FUNCION QUE PREGUNTE AL USUARIO UNA FRASE Y DEVUELVA DICHA FRASE CON PALABRAS EN 
#FORAM INVERSA, POR EJEMPLO SI EL USUARIO ESCRIBE"HOY ES DOMINGO" LA FUNCION DEVOLVERÁ
#"DOMINGO ES HOY"

def invertir_palabras (frase=input("DIGITE UNA FRASE: ")):
   
    palabras=frase.split(" ") #AQUI ESTAMOS DIVIDIENDO LA FRASE EN PALABRAS
    return " ".join(palabras[::-1]) #AQUI ESTAMOS INVIRTIENDO ALS PALABRAS

print(invertir_palabras())
        
    


#%%
#CREAR UNA FUNCION QUE DETECTE SI UAN PALABRA ES PALINDORA, OSEA QUE SE LEE IGUAL DE UN SENTIDO U OTRO
def es_palindromo(palabra):
    palabra_invertida=palabra[::-1]
    for i in range(len(palabra_invertida)): #aqui ylitizamos for y range para recorrer letra por letra
        if palabra[i]!=palabra_invertida[i]: #si al letra es diferente no es palindromo
            return False
        return True
    
es_palindromo("allivaramonynomaravilla")


#%%
#CREAR UNA FUNCION QUE DADA UN ALISTA DE LISTAS NOS DEVUELVA UAN LSITA SIMPLE(ES DECIR SIN NINGULA LISTA DENTRO)
#POR EJEMPLO SI HA DICHA FUNCION  LE PASAMOS EL ARGUMENTO
"""
lista_nesteada=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
]
"""

#LA FUNCION NOS DEVOLVERA LA LISTA ^[1,2,3,4,5,6,7,8,9]
def simplificar_lista(lista_nesteada):
    lista_simple= []
    for lista_interna in lista_nesteada:
        for elemento in lista_interna:
            lista_simple.append(elemento)
            return lista_simple
        
lista_nesteada=[
        [1,2,3],
        [4, 5, 6],
        [7,8,9]
]

simplificar_lista(lista_nesteada)           

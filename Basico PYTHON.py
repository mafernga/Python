# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:56:07 2019

@author: Mario_Andres
"""


#%%
nombre="MARIO"
ciudad="Medellín"
apellido="FERNANDEZ"

print(nombre +" "+ apellido + " "+ ciudad)
#%%

presenta= "Mi nombre es {} y soy de la ciudad de {}".format(nombre,ciudad)
print(presenta)

print(presenta.format(nombre,ciudad))

print (("Mi nombre es {}, mi apellido {} y estoy en la ciudad de {}").format(nombre, apellido, ciudad))

presenta2= f"Hola Mi nombre es {nombre}, mi apellido {apellido} y estoy en la ciudad de {ciudad}"
print(presenta2)

#%%
import math

pi_strg="El numero PI es {}".format(math.pi)
print(pi_strg)

pi_strg="Los primeros 2 decimales de PI son {:.2f}".format(math.pi)
print(pi_strg)

pi_strg="El numero  PI sin decimales es {:.0f}".format(math.pi)
print(pi_strg)

#%%
"""
OPERACIONES CON STRING
"""

palabra="el vehiculo es rojo"

print("Convertimos un string en mayuscula con UPPER")
print(palabra.upper())

print("Convertimos un string en mayuscula con lower")
print(palabra.lower())

print("Ponemos la primera letra en mayuscula con capitalize")
print(palabra.capitalize())
#%%
"""
OPERACIONES CON STRING
"""
palabra2=",mario,,"
palabra3="Mario"

print("Usamos strip para eliminar caracteres al inicio y al final del string")
print(palabra2.strip(","))

print("Usamos replace para reemplazar caracteres en el string")
print(palabra2.replace("rio", "riana"))

print("Usamos replace para reemplazar caracteres en el string")
print(palabra3.replace("Ma", "Sama"))

print("Todos los metodos se pueden encadenar")
print(palabra2.strip(",").upper().replace("MA", "Sama"))
#%%
"""
OPERACIONES CON STRING
"""
string3="Mario|ANDRES|FERNANDEZ|GARCIA"

print("Se puede separar un string en multiples con split")
print(string3.split("|"))

resultado=(string3.split("|"))
print(resultado)

#%%
"""
OPERACIONES CON NUMEROS
"""
print("Hay 2 tipos basicos de numeros en python int(enteros) y float(decimales)")

num1=45
num2=4.8
num3="25"
edad=35
print(type(num1))
print(type(num2))
print(type(5.1))
print(type(num3))
#%%
print("Podemos convertir numeros a string con str")
print(type(str(num1)))
print("dos +" + " " + str(num1))
#%%
edad=35
num4="2.5"
print("Podemos convertir string a numeros con int")
print(type(int(num3)))
print(num1+int(num3))

print("Podemos convertir string a numeros con float")
print(type(float(num4)))
resultado2=(edad + float(num4))
print(resultado2)

print(f"Hola mi nombre es {nombre} y tengo {edad} años")
#%%
"""
OPERACIONES CON NUMEROS
Podemos usar los simbolos basicos de aritmetica para hacer operaciones
"""
#SUMA
print("2 + 2 =", 2 + 2)

#RESTA
print("5 - 2 =", 5 - 2)

#MULTIPLICACION
print("4 * 2 =", 4 + 2)

#DIVISION
print("6 / 2 =", 6 / 2)
#%%
"""
OPERACIONES CON NUMEROS
Podemos hacer estas otras operaciones
"""
a=7
b=2
#MULTIPLO INFERIOR, REALIZAR LA DIVISION ELIMINANDO LOS DECIMALES
print(f"{a}//{b}=",a//b)

#MODULO, REALIZAR LA DIVISION Y MOSTRAR SOLO EL RESIDUO
print(f"{a}%{b}=",a%b)

#NEGACIOM, CAMBIAR EL SENTIDO DE UN VALOR
print(f"Negacion de {a} es=",-a)

#pPOTENCIAS, ELEVAR AL CUADRADO AL CUBO ETCC..
print(f"{a}**{b} es=",a**b)

#%%
"""
BOOLEANOS
Una variable Booleana es aquella que solo puede ser verdadera o falsa
"""
verdadero=True
falso=False

print(type(verdadero))

"""
BOOLEANOS
Como tipo de primitiva especial tenemos None que es la variable nula
"""
nulo=None
print(type(nulo))

#Cualquier tipo de variable se puede convertir en booleano, convirtiendose en True
print(bool("patatas"))

# Salvo None que se convierte a False
print(bool(nulo))

# 0 se convierte en False
print(bool(0))

#%%
"""
COMPARACIONES LOGICAS
Podemos hacer comparaciones entre variables, el resultado de estas comapraciones 
siempre es una variable booleana
"""
a=7
b=2
#a mayor que b
print(f"{a}>{b}",a>b)  #en este caso a es mayor que b debe dar como resultado True

#b menor o igual que b
print(f"{b}<={a}",b<=a)  #en este caso b es menor que a debe dar como resultado True

#b es igual a 2
print(f"{b}==2",b==2)  #en este caso b es igual que 2 a debe dar como resultado True

#a es distinto a 23
print(f"{a}!=23",a!=23)  #en este caso a es diferente a 23 debe dar como resultado True

#Podemos tener el opuesto de un resultado logico con not
print(f"not {a}!=23",not a!=23)  #en este caso a es diferente a 23 pero como buscamos el opuesto debe  dar como resultado false


#podemos evaluar que diferenctes condiciones se cumplan con and
print(f"{a}!=23 and {a}>{b}",a!=23 and a>b)  #en este caso a es diferente a 23 y a es mayor que b entonces debe dar como resultado True


#podemos usar or para evaluar si se cumple una condicion u otra
print(f"{a}!=7 or {a}>{b}",a!=7 or a>b)  #en este caso a es diferente a 7 y a es mayor que b entonces debe dar como resultado True

#%%
"""
COMPARACIONES LOGICAS
Para comparar si algo es verdadero o falso no usamos = sino que usamos is
siempre es una variable booleana
"""
condicion=True

print("condicion is True =",condicion is True)

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
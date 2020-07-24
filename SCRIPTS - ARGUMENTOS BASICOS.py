# -*- coding: utf-8 -*-
"""
Aqui se explica como añadir funcionalidad a los script

@author: Mario Andres Fernandez
"""
#Los imports se añaden al inicio del script
import sys
from Funciones import saludar

def parsear_argumentos_basico():
    argumentos=sys.argv[1:]
    return argumentos


def main(argumentos):
    """
    Aqui ponemos la funcionalidad principal d enuestro script
    """
    
    if argumentos[0]=="saludar":
        nombre=argumentos[1]
        saludar(nombre)
        
    
if __name__=="__main__":
    #Este codigo solo se ejecutará si ejecutamos este script directamente
    
    argumentos=parsear_argumentos_basico()
    print("Argumentos pasados al script: ",argumentos)
    main(argumentos)
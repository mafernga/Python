# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 15:59:18 2020

@author: Mario_Andres
"""

"""
********************************************************************************
CLASES
********************************************************************************

Python es un lenguaje orientado a objetos. ¿Eso que significa? que pese q que podemos programar de forma funcional
esto es simplemente enviando datos a traves de funciones, muchas de las ventajas de python esta en su uso de clases.

Las clases en Python se definen asi: (python 3)

Class clase:
    def metodo1(self) ---> TODOS LOS METODOS DE CLASE TOMAS self COMO PRIMER ARGUMENTO
        #METODO QUE TIENEN LOS OBJETOS DE LA CLASE
    
    def metodo2(self)
        #OTRO METODO QUE TIENEN LOS OBJETOS DE LA CLASE
    
"""
#%%
#POR EJEMPLO PODEMOS CREAR UNA CLASE COCHE
class CocheBasico:
    def girar_a_la_izquierda(self):
        print("Girando a la Izquierda")
    
    def girar_a_la_derecha(self):
        print("Girando a la Derecha")
    
    def acelerar(self):
        #Podemos usar pass cuando definimos una funcion, para que no haga nada
        pass
        
    def frenar(self):
        pass

print(CocheBasico)

#%%
"""
HEMOS GENERADO UNA CLASE COCHE. LAS CLASES SE PUEDEN CONSIDERAR COMO PLANTILLAS QUE SE PUEDEN USAR
PARA GENERAR OBJETOS. POR EJEMPLO LA PLANTILLA(CLASE) COCHE NOS DA INSTRUCCIONES  PARA FABRICAR UN COCHE
EN JERGA DE DESARROLLO SE LE LLEMA "INSTANCIAR UNA CLASE", ES DECIR CREAMOS UNA INSTANCIA(OBJETO) DE LA CALSE
COCHE

"""
coche_manuel=CocheBasico()
print(coche_manuel)
#%%
#Este objeto  coche es un Coche, es decir es un objeto de la clase Coche
print(type(coche_manuel)==CocheBasico)  #debe devolver un True ya que el tipo de coche_manuel es icual al CocheBasico
#%%
#El coche de manuel tambien tiene todas las carcteristicas de CocheBasico
coche_manuel.girar_a_la_izquierda()
coche_manuel.girar_a_la_derecha()

#%%
"""
AL IGUAL QUE LAS FUNCIONES, GENERALMENTE QUEREMSO QUE LOS OBJETOS QUE CREEMOS TENGAN UNAS CARCTERISTICAS
DEFINIDAS DE FORMA VARIABLE.
CON AL CLASE COCHE QUE TENEMOS, TODOS LOS COCHES QUE CREEMOS SERAN 100% DEL MSIMO COLOR
¿COMO PODRIAMOS CREAR COCHES DE DISTINTOS COLORES POR EJEMPLO?

PARA ESO DEBEMOS USAR EL METODO __init__ QUE SE EJECUTA CUANDO SE CREA UN OBJETO DE UNA CLASE

UNA DE LAS VENTAJAS DE LAS CLASES ES QUE PUEDEN GUARDAR EL ESTDO DE LAS COSAS EN EL TIEMPO
"""
class CocheConColor:
    
    def __init__(self, color):
        self.color=color #Esto es un atributo
        
    def describir(self):
        print("Coche de Color: {}".format(self.color))   
        
    def girar_a_la_izquierda(self):
        print("Girando a la Izquierda")
    
    def girar_a_la_derecha(self):
        print("Girando a la Derecha")
    
    def acelerar(self):
        #Podemos usar pass cuando definimos una funcion, para que no haga nada
        pass
        
    def frenar(self):
        pass

coche_rojo=CocheConColor(color="ROJO")
coche_rojo.describir()
print(coche_rojo.color) #atributo del objeto
#%%
#TAMBIEN PODEMOS AÑADIR ATRIBUTOS A INSTANCIAS
coche_rojo.matricula="MHL138"
print (coche_rojo.matricula)
#%%
#AHORA AL CREAR UN CocheConColor TENEMSO QUE ESPECIFICAR UN COLOR, PROQUE SINO SALE ERROR
coche_sin_color=CocheConColor()
coche_sin_color.color
#%%
#PODEMOS EVITAR ESTOS ERRORRES ASIGNANDO UN COLOR POR DEFECTO EN EL METODO __init__
class CocheConColor:
    
    def __init__(self, color="Amarillo"):
        self.color=color #Esto es un atributo
        
    def describir(self):
        print("Coche de Color: {}".format(self.color))   
        
    def girar_a_la_izquierda(self):
        print("Girando a la Izquierda")
    
    def girar_a_la_derecha(self):
        print("Girando a la Derecha")
    
    def acelerar(self):
        #Podemos usar pass cuando definimos una funcion, para que no haga nada
        pass
        
    def frenar(self):
        pass

coche_sin_color=CocheConColor()
coche_sin_color.describir()

#%%
#DE IGUAL MANERA PODEMOS DEFINIR TODAS ALS VARIABLES QUE NECESITAMOS PARA DEFINIR UN OBJETO
class CocheVariable:
    
    def __init__(self, modelo, velocidad_maxima, color="Amarillo"):
        self.color=color #Esto es un atributo
        self.modelo=modelo #Esto es un atributo
        self.velocidad_maxima=velocidad_maxima #Esto es un atributo
        self.velocidad=  0 #El coche empieza parado
        
    def describir(self):
        print("Coche Modelo: {}. Velocidad Maxima: {}. Color: {}".format(self.modelo, self.velocidad_maxima, self.color ))   
  
    def describir_estado(self):
        if self.velocidad== 0:
            print("El Coche está parado")
        else:
            print("El Coche va a {} kilometros por hora".format(self.velocidad))
               
    def girar_a_la_izquierda(self):
        print("Girando a la Izquierda")
    
    def girar_a_la_derecha(self):
        print("Girando a la Derecha")
    
    def acelerar(self):
        #Podemos usar pass cuando definimos una funcion, para que no haga nada
        pass
        
    def frenar(self):
        pass

coche1=CocheVariable(modelo="Ferrari",velocidad_maxima=120)
coche1.describir()
coche1.describir_estado()
#%%
#PODEMOS EN CUALQUIER MOMENTO CAMBIAR EL ATRIBUTO DE UN OBJETO
coche1.velocidad=120
coche1.describir_estado()

#%%
#CUANDO USAS EL PRINT PARA IMPRIMIR ALGO EN ESTE CASO NO ES TAN DESCRIPTIVO
print(coche1)

#%%
"""
Uno de los principales usos de las clases  es conservar el estado de un objeto.
si no usamos clases para almacenar la velocidad de un coche, tendriamos que tener un diccionario con los 
identificadores de los coches y su velocidad, y cada vez que cambiramos de velocidad
tendriamos que cambiar el diccionario.

Ahora nos falta simplemente añadir las funciones para acelerar y tendremos un vehiculo completo
"""
class vehiculo:
    
    def __init__(self, modelo, velocidad_maxima, color="Plateado"):
        self.color=color #Esto es un atributo
        self.modelo=modelo #Esto es un atributo
        self.velocidad_maxima=velocidad_maxima #Esto es un atributo
        self.velocidad=  0 #El coche empieza parado
        
    def describir(self):
        descripcion= "Vehiculo Modelo: {}. Velocidad Maxima: {} km/h. Color: {}".format(
                self.modelo, self.velocidad_maxima, self.color )
        return descripcion  
    
 #El metodo __repr__ es un metodo magico que se una cuando queremos representaralgo con el metodo (print)
 #ya que sin este al representar algo con el metodo print, el resultado no es tan decriptivo    
    def __repr__(self):
        return self.describir()
        
    def describir_estado(self):
        if self.velocidad== 0:
            print("El Coche está parado")
        elif self.velocidad>0:
            print("El Vehiculo va a {} kilometros por hora".format(self.velocidad))
        else:
            print("El vehiculo va marcha atras {} kilometros por hora".format(self.velocidad))
               
    def girar_a_la_izquierda(self):
        print("Girando a la Izquierda")
    
    def girar_a_la_derecha(self):
        print("Girando a la Derecha")
    
    def acelerar(self, diferencia_velocidad):
        print("Acelerando {} km/h".format(diferencia_velocidad))
        # abs conveirte en positivo los numeros negativos
        self.velocidad+=abs(diferencia_velocidad)
        
        # min devuelve el valor minimo de una lista de numeros
        #esta funcion se la aplicamos a velocidad para que en caso de que alguien digite que 
        #acelero 1 millon de km/hora la velocidad tome el valor de velocidad maxima y no el que se digito
        #porque se entiende que el vehiculo no puede superar la velocidad maxima
        self.velocidad=min(self.velocidad, self.velocidad_maxima)
       
        
    def frenar(self, diferencia_velocidad):
        print("frenando {} km/h".format(diferencia_velocidad))
        # abs conveirte en positivo los numeros negativos
        self.velocidad-=abs(diferencia_velocidad) #igual que acelerar pero en vez de sumar resta para frenar
        
        # max devuelve el valor maximo de una lista de numeros
        #esta funcion se la aplicamos a velocidad para que en caso de que alguien digite que 
        #frenó 1 millon de km/hora la velocidad tome el valor de velocidad maxima y no el que se digito
        #porque se entiende que el vehiculo no puede superar la velocidad -5 en este caso
        self.velocidad=max(self.velocidad, -5)
        
coche_mario=vehiculo(modelo="Chevrolet Tracker", velocidad_maxima=200, color="Plateado")
print(coche_mario) #en este caso podemos usar print porque incluimos en la clase el metodo __repr__
coche_mario.describir_estado()
coche_mario.acelerar(60)
coche_mario.describir_estado()     
coche_mario.acelerar(80)
coche_mario.describir_estado()  
coche_mario.frenar(50)
coche_mario.describir_estado() 
#%%
"""
HERENCIA DE CLASES

Una de als principales ventajas de usar clases  es que se pueden crear clases usando como plantillas
otras clases(Se dice que una clase hereda de otra)

Ésto nos permite crear una clase base con funcionalidades genericas y despues crear clases avanzadas
con diversas funcionalidades mas especificas.

POR EJEMPLO PODEMOS CREAR UNA CLASE  AUTOBUS, QUE NO TIENE MARCHA ATRAS Y TIENE UN LIMITE DE VELOCIDAD DE 100KM/H
"""
#%%
class Autobus(vehiculo): #Esto indica que Autobus hereda vehiculo
    def acelerar(self, diferencia_velocidad):
        print("Autobus acelerando a:{} Km/h".format(diferencia_velocidad))
        
        # abs conveirte en positivo los numeros negativos
        self.velocidad+=abs(diferencia_velocidad)
        
        # min devuelve el valor minimo de una lista de numeros
        #esta funcion se la aplicamos a velocidad para que en caso de que alguien digite que 
        #acelero 1 millon de km/hora la velocidad tome el valor de velocidad maxima y no el que se digito
        #porque se entiende que el vehiculo no puede superar la velocidad maxima
        self.velocidad=min(self.velocidad, 100)
        
    def frenar(self, diferencia_velocidad):
        print("Autobus Frenando {} km/h".format(diferencia_velocidad))
        # abs conveirte en positivo los numeros negativos
        self.velocidad-=abs(diferencia_velocidad) #igual que acelerar pero en vez de sumar resta para frenar
        
        # max devuelve el valor maximo de una lista de numeros
        #esta funcion se la aplicamos a velocidad para que en caso de que alguien digite que 
        #frenó 1 millon de km/hora la velocidad tome el valor de velocidad maxima y no el que se digito
        #porque se entiende que el vehiculo no puede superar la velocidad -5 en este caso
        self.velocidad=max(self.velocidad, 0)
        
autobus1=Autobus(modelo="MERCEDES BENZ", velocidad_maxima=100, color="Azul")
print(autobus1)
autobus1.describir_estado()
autobus1.acelerar(80)
autobus1.describir_estado()
autobus1.acelerar(40)
autobus1.describir_estado()
autobus1.frenar(80)
autobus1.describir_estado()
autobus1.frenar(80)
autobus1.describir_estado()
autobus1.acelerar(40)
print(autobus1)
autobus1.describir_estado()
autobus1.acelerar(100)
autobus1.describir_estado()
autobus1.frenar(50) 
autobus1.describir_estado()

#%%
"""
***************************************************************************************
EJERCICIOS CON CLASES

***************************************************************************************
Crear una clase taxi que herede de vehiculo y que pueda cobrarnos un trayecto.
Tiene que tneer un atributo "distancia_recorrida" y tres metodos adicionales:
    - Metodo cobrar, donde se imprime la cantidad a cobrar(3 euros por kilometro recorrido)
    - Metodo "Añadir_distancia", donde se suma la distancia recorridam un numero de kilometros
    - Metodo "Añadir_tiempo", donde dado un tiempo (en horas) se añade distancia en funcion de la velocidad actual
"""
#%%
class taxi(vehiculo):  #aca hay que volver a poner todos los atributos de __init__ porque vamos a agregar mas atributos
    def __init__(self, modelo, velocidad_maxima):
        self.color="amarillo" #Esto es un atributo
        self.modelo=modelo #Esto es un atributo
        self.velocidad_maxima=velocidad_maxima #Esto es un atributo
        self.velocidad=  0 #El coche empieza parado
        self.distancia_recorrida=  0 #El coche empieza parado
        self.tarifa=  3 #El coche empieza parado

    def cobrar(self):
        print("El total a cobrar es {} Euros".format(self.distancia_recorrida*self.tarifa))
        
    def añadir_distancia(self, distancia):
        self.distancia_recorrida+=distancia           
    
    def añadir_tiempo(self, tiempo):
        self.añadir_distancia(tiempo*self.velocidad)      
        
taxi1=taxi(modelo="Mercedes Benz",velocidad_maxima=100)
print(taxi1)
taxi1.acelerar(80)
taxi1.añadir_tiempo(6)
taxi1.cobrar()


#%%
"""
***************************************************************************************
OTRA FORMA DE HACER EL EJERCICIO SIN TENER QUE VOLVER A PONER TODOS LOS ATRIBUTOS DE __init__ 
DE LA CLASE HEREDADA VEHICULO, UTILIZANDO *args, **kwargs y la funcion super()
***************************************************************************************
"""
class taxi2(vehiculo):
    def __init__(self, tarifa, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.distancia_recorrida=0
        self.tarifa= tarifa
        
    def cobrar(self):
        print("El total es: {} Euros".format(self.distancia_recorrida*self.tarifa))
        
    def añadir_distancia(self, distancia):
        self.distancia_recorrida+=distancia
        
    def añadir_tiempo(self, tiempo):
        self.añadir_distancia(tiempo*self.velocidad)
        
taxi=taxi2(tarifa=3, modelo="TOYOTA", velocidad_maxima=200, color="AMARILLO")
print(taxi)
taxi.describir_estado()
taxi.acelerar(50)  
taxi.describir_estado()
taxi.añadir_tiempo(8)
taxi.añadir_tiempo(3)
taxi.cobrar()

#%%
"""
***************************************************************************************
EJERCICIO 2

Crear una clase Parking, donde puedan aparcar un limite determinado de vehiculos (solo vehiculos)
y donde se pueda validar si un vehiculo esta aparcado o no.
***************************************************************************************
"""
class parking:
    def __init__(self, capacidad):
        self.capacidad=capacidad
        self.vehiculos=[]
        
    def nivel_ocupacion(self):
        return len(self.vehiculos)/self.capacidad
    
    def __repr__(self):
        return "Parking con capacidad de {} vehiculos. Nivel de ocupacion {:.2f}".format(self.capacidad, self.nivel_ocupacion())
    
    def aparcar_vehiculo(self, Vehiculo):
        if not type(Vehiculo)==vehiculo or Vehiculo in self.vehiculos:
            print("Solo se admiten vehiculos qeu no esten aparcados")
        
        elif len(self.vehiculos)<self.capacidad:
            print("Aparcando vehiculo {}".format(Vehiculo))
            self.vehiculos.append(Vehiculo)
        
    def sacar_vehiculo(self, Vehiculo):
        if Vehiculo in self.vehiculos:
            print("Sacando el vehiculo {} ".format(Vehiculo))
            self.vehiculos.pop(self.vehiculos.index(Vehiculo))
        
        else: 
            print("El vehiculo {} no esta aparcado".format(Vehiculo))
            
parking_medellin=parking(50)
print(parking_medellin)

vehiculo_mario=vehiculo(modelo="CHEVROLET", velocidad_maxima=100, color="GRIS")
print(vehiculo_mario)

parking_medellin.aparcar_vehiculo(vehiculo_mario)
parking_medellin.aparcar_vehiculo(vehiculo_mario)

vehiculo_mariana=vehiculo(modelo="TOYOTA", velocidad_maxima=120, color="Verde")

parking_medellin.aparcar_vehiculo(vehiculo_mariana)
print(parking_medellin)

taxi3=taxi(modelo="Mercedes", velocidad_maxima=80)

print(taxi3)

parking_medellin.aparcar_vehiculo(taxi3)    

parking_medellin.sacar_vehiculo(vehiculo_mariana)
print(parking_medellin)
        
  
parking_medellin.sacar_vehiculo(vehiculo_mario)
print(parking_medellin)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
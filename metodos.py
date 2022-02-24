# -*- coding: utf-8 -*-
"""
String Methods examples
Created on Fri Feb 11 08:04:40 2022

@author: angel
"""
# 
txt='Esto es el Texto que se va a usar de Ejemplo'
# ejemplo para método join, sin aplicar listas
a='Aprender'
b='a programar'
c= 'Python'
d= 'es . . . .'
e= " _".join([a,b,c,d])
print(e)

lp=['La','legibilidad','es','importante']
R=" ".join(lp)
print(R)

#
rdo=txt.upper() # Método poner todas en mayusculas
rdo=txt[5:16].upper() # Pone en mayusculas posición 5 a 15 >>> ES EL TEXTO
rdo=txt.lower() # Método todo en minusulas
rdo=txt.split() # separa el texto en  elementos y los guarda dentro de una LISTA
rdo=txt.split('s') # separa, pero tomando la "s" como separador, envez del espacio
rdo=txt.find('T') # método de busqueda, devuelve la posición de  "T" (si no encuentra devuelve "-1")
rdo=txt.find('usar') # >>> 29 (a partir de la posición 29)
rdo=txt.find('u',10,25) # busca "u" desde la posición 10 a la 24 >>> 18
rdo=txt.replace('el Texto', 'la Frase') # método para remplazar  
rdo=txt.replace('e', 'X') # remplaza "e" por "X"
txt='Si la implementación es difícil de explicar, puede que sea una mala idea.'
R1=txt.replace('difícil','fácil')
R2=R1.replace('mala', 'buena')
print (R2)
            
#
print(rdo)
#
'''
rdo.txt.split() >>> ['Esto', 'es', 'el', 'Texto', 'que', 'se', 'va', 'a', 'usar', 'de', 'Ejemplo']
rdo=txt.split('s') >>> ['E', 'to e', ' el Texto que ', 'e va a u', 'ar de Ejemplo']

rdo=txt.replace('el Texto', 'la Frase') >>> Esto es la Frase que se va a usar de Ejemplo
rdo=txt.replace('e', 'X') >>> Esto Xs Xl TXxto quX sX va a usar dX EjXmplo

'''

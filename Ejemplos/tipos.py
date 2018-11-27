#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

def imprime_var(tipo, v):
    """
    Imprime los dos argumentos recibidos. 
    Recibe:
        tipo (str) - descripci√n del tipo de dato
        v (any) - variable a imprimir
    Regresa:
        nada (None)
    """
    print 'Variable de tipo %s:\t%s' % (tipo,v)
    print type(v)
    print '\n'


#Numeros
#Enteros en base 10
i1 = 2017
imprime_var('entero en base 10', i1)


#Enteros en base 2
i2 = 0b11111100001
imprime_var('entero en base 2', i2)


#Enteros en base 16
i3 = 0x07e1
imprime_var('entero en base 16', i3)


#Reales con punto decimal
r1 = 0.001
imprime_var('real', r1)

#Complejos
c1 = 1 + 4j
imprime_var('complejo', c1)


#Reales en notacion cintifica
r2 = 0.1e-3
imprime_var('real en notacion centifica', r2)


#Cadenas
#Cadenas con comilla doble
c1 = "Becarios 12g"
imprime_var('cadena usando doble comilla', c1)


#Cadenas con comilla simple
c2 = 'Becarios 12g'
imprime_var('cadena usando doble comilla', c2)


#Cadenas multilinea
c3 = '''
    Becarios 
    12g'''
imprime_var('cadena multilinea',c3)


#Booleanos
b1 = True
imprime_var('booleano (verdadero)', b1)

b2 = False
imprime_var('booleano (falso)', b2)

#Tipo de dato None (Nulo)
n1 = None
imprime_var('None (nulo)', n1)


#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

def saluda1(sujeto):
    """
    Imprime un saludo usando el valor del argumento "sujeto" concatenando las cadenas
    Args:
        sujeto (string) se concatena al saludo
    Returns:
        nada (None)
    """
    print 'Hola '+sujeto+' !!'


def saluda2(sujeto):
    """
    Imprime un saludo usando el valor del argumento "sujeto" usando formato de cadenas
    Args:
        sujeto (string) se formatea en la cadena del saludo
    Returns:
        nada (None)
    """
    print 'Hola %s !!' % sujeto

saluda1('Mundo')
saluda2('Mundo')

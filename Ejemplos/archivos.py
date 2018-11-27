#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from sys import argv
from random import choice

calificaciones = (0,1,2,3,4,5,6,7,8,9)
becarios = ['Cervantes Varela Juan Manuel',
            'Leal González Ignacio',
            'Ortiz Velarde Valeria',
            'Martínez Salazar Luis Antonio',
            'Rodríguez Gallardo Pedro Alejandro',
            'Tadeo Guillén Diana Guadalupe',
            'Ferrusca Ortiz Jorge Luis',
            'Juárez Méndez Jesika',
            'Pacheco Franco Jesús Enrique',
            'Vallejo Fernández Rafael Alejandro',
            'López Fernández Servando Miguel',
            'Hernández González Ricardo Omar',
            'Acevedo Gómez Laura Patricia',
            'Manzano Cruz Isaías Abraham',
            'Espinosa Curiel Oscar',
            ]

def asigna_calificaciones(archivo):
    with open(archivo,'w') as asignacion:
        for becario in becarios:
            asignacion.write('%s:%s\n' % (becario,choice(calificaciones)))


def califica_becarios(archivo):
    with open(archivo,'r') as calificaciones:
        for linea in calificaciones:
            linea = linea.split(':')
            nombre_becario = linea[0]
            calificacion = int(linea[1])
            if calificacion >= 8:
                print '%s RIFA MUCHO\n' % nombre_becario.upper()
            elif calificacion >= 6:
                print '%s DEBE MEJORAR\n' % nombre_becario.upper()
            else:
                print '%s NO TERMINARÁ EL PLAN\n' % nombre_becario.upper()


asigna_calificaciones(argv[1])
califica_becarios(argv[1])

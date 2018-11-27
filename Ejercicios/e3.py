#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice

calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Juan Manual',
            'Ignacio',
            'Valeria',
            'Luis Antonio',
            'Pedro Alejandro',
            'Diana Guadalupe',
            'Jorge Luis',
            'Jesika',
            'Jesús Enrique',
            'Rafael Alejandro',
            'Servando Miguel',
            'Ricardo Omar',
            'Laura Patricia',
            'Isaías Abraham',
            'Oscar']

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

def rep_apro(calificacion_alumno):
    aprobados = []
    reprobados = []
    for alumno in calificacion_alumno:
        if calificacion_alumno[alumno] >= 8:
            aprobados.append(alumno)
        else:
            reprobados.append(alumno)
    return tuple(aprobados),tuple(reprobados)

def promedio(calificacion_alumno):
    suma = 0
    for alumno in calificacion_alumno:
        suma += calificacion_alumno[alumno]
    return float(suma)/len(calificacion_alumno)

def conjunto_cal(calificacion_alumno):
    conjunto = set()
    for alumno in calificacion_alumno:
        conjunto.add(calificacion_alumno[alumno])
    return conjunto
    
    


asigna_calificaciones()
imprime_calificaciones()

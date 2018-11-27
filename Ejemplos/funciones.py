#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

aprobados = []

def aprueba_becario(nombre_completo):
    nombre_separado = nombre_completo.split()
    for n in nombre_separado:
        if n in ['Manuel', 'Valeria', 'Alejandro', 'Luis', 'Enrique','Omar','Abraham','Oscar']:
            return False
    aprobados.append(nombre_completo)
    return True


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
            'Valle Juarez Pedro Angel',
            'Espinosa Curiel Oscar']
for b in becarios:
    if aprueba_becario(b):
        print 'APROBADOO: ' + b
    else:
        print 'REPROBADO: ' + b


#print becarios
